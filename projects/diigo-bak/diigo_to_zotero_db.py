#!/usr/bin/env python3
"""Convert Diigo bookmark export (ndjson) into a Zotero SQLite database.

Builds a fresh DB from Zotero source schema SQL and imports bookmarks as
`webpage` items with URL/title/date/tags. Description goes to abstractNote,
and annotations are stored as child note items.

Usage:
  diigo_to_zotero_db.py --zotero-source DIR --input FILE --output FILE
"""

from __future__ import annotations

import hashlib
import json
import sqlite3
from dataclasses import dataclass
from datetime import UTC, datetime
from html import escape
from io import TextIOBase
from pathlib import Path as Path_T

DATE_FMT = "%Y/%m/%d %H:%M:%S %z"
USAGE = (
    "usage: diigo_to_zotero_db.py --zotero-source DIR "
    "--input FILE --output FILE"
)


@dataclass(frozen=True)
class Config:
    zotero_source: str
    input_path: str
    output_path: str


def parse_cli(argv: list[str]) -> Config:
    zotero_source = ""
    input_path = ""
    output_path = ""

    it = iter(argv[1:])
    for token in it:
        if token in {"-h", "--help"}:
            raise ValueError(USAGE)
        if token == "--zotero-source":
            zotero_source = next(it)
            continue
        if token == "--input":
            input_path = next(it)
            continue
        if token == "--output":
            output_path = next(it)
            continue
        raise ValueError(f"unknown option: {token}\n{USAGE}")

    if not (zotero_source and input_path and output_path):
        raise ValueError(f"missing required options\n{USAGE}")

    return Config(
        zotero_source=zotero_source,
        input_path=input_path,
        output_path=output_path,
    )


def read_sql(path: Path_T) -> str:
    return path.read_text(encoding="utf-8")


def init_db(conn: sqlite3.Connection, zotero_source: Path_T) -> None:
    schema_dir = zotero_source / "resource" / "schema"
    for name in ["userdata.sql", "system.sql", "system-107.sql", "triggers.sql"]:
        sql_path = schema_dir / name
        if not sql_path.exists():
            raise FileNotFoundError(str(sql_path))
        conn.executescript(read_sql(sql_path))

    # In Zotero runtime these are populated on startup.
    conn.execute("DELETE FROM itemTypesCombined")
    conn.execute(
        """
        INSERT INTO itemTypesCombined (itemTypeID, typeName, display, custom)
        SELECT itemTypeID, typeName, COALESCE(display, 1), 0 FROM itemTypes
        """
    )
    conn.execute("DELETE FROM fieldsCombined")
    conn.execute(
        """
        INSERT INTO fieldsCombined (fieldID, fieldName, label, fieldFormatID, custom)
        SELECT fieldID, fieldName, fieldName, fieldFormatID, 0 FROM fields
        """
    )
    conn.execute("DELETE FROM itemTypeFieldsCombined")
    conn.execute(
        """
        INSERT INTO itemTypeFieldsCombined (itemTypeID, fieldID, hide, orderIndex)
        SELECT itemTypeID, fieldID, hide, orderIndex FROM itemTypeFields
        """
    )
    conn.execute("DELETE FROM baseFieldMappingsCombined")
    conn.execute(
        """
        INSERT INTO baseFieldMappingsCombined (itemTypeID, baseFieldID, fieldID)
        SELECT itemTypeID, baseFieldID, fieldID FROM baseFieldMappings
        """
    )

    # Minimal local library and schema version metadata.
    conn.execute(
        """
        INSERT OR REPLACE INTO libraries
            (libraryID, type, editable, filesEditable, version, storageVersion,
             lastSync, archived)
        VALUES (1, 'user', 1, 1, 0, 0, 0, 0)
        """
    )
    conn.execute(
        "INSERT OR REPLACE INTO version(schema, version) VALUES ('userdata', 123)"
    )


def parse_tags(raw: str | None) -> list[str]:
    if not raw:
        return []
    out: list[str] = []
    for part in raw.split(","):
        tag = part.strip()
        if tag:
            out.append(tag)
    return out


def key_for(row: dict[str, object]) -> str:
    seed = "|".join(
        [
            str(row.get("url") or ""),
            str(row.get("created_at") or ""),
            str(row.get("title") or ""),
        ]
    )
    return hashlib.sha1(seed.encode("utf-8")).hexdigest()[:8].upper()


def dt_sql(s: str | None) -> str:
    if not s:
        return datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S")
    return datetime.strptime(s, DATE_FMT).strftime("%Y-%m-%d %H:%M:%S")


def ensure_item_data_value(conn: sqlite3.Connection, value: str) -> int:
    conn.execute("INSERT OR IGNORE INTO itemDataValues(value) VALUES (?)", (value,))
    row = conn.execute(
        "SELECT valueID FROM itemDataValues WHERE value = ?", (value,)
    ).fetchone()
    if not row:
        raise RuntimeError("failed to resolve itemDataValues.valueID")
    return int(row[0])


def ensure_tag(conn: sqlite3.Connection, tag_name: str) -> int:
    conn.execute("INSERT OR IGNORE INTO tags(name) VALUES (?)", (tag_name,))
    row = conn.execute("SELECT tagID FROM tags WHERE name = ?", (tag_name,)).fetchone()
    if not row:
        raise RuntimeError("failed to resolve tags.tagID")
    return int(row[0])


def add_note_item(
    conn: sqlite3.Connection,
    *,
    parent_item_id: int,
    key_seed: str,
    note_html: str,
    date_added: str,
) -> None:
    note_key = hashlib.sha1((key_seed + "|note").encode("utf-8")).hexdigest()[:8]
    note_key = note_key.upper()
    cur = conn.execute(
        """
        INSERT INTO items
            (itemTypeID, dateAdded, dateModified, clientDateModified,
             libraryID, key, version, synced)
        VALUES (1, ?, ?, ?, 1, ?, 0, 0)
        """,
        (date_added, date_added, date_added, note_key),
    )
    note_item_id = int(cur.lastrowid)
    conn.execute(
        "INSERT INTO itemNotes(itemID, parentItemID, note, title) VALUES (?, ?, ?, ?)",
        (note_item_id, parent_item_id, note_html, "Diigo Annotations"),
    )


def add_bookmark(conn: sqlite3.Connection, row: dict[str, object]) -> None:
    title = str(row.get("title") or row.get("url") or "").strip()
    url = str(row.get("url") or "").strip()
    created = dt_sql(str(row.get("created_at") or ""))
    key = key_for(row)

    cur = conn.execute(
        """
        INSERT INTO items
            (itemTypeID, dateAdded, dateModified, clientDateModified,
             libraryID, key, version, synced)
        VALUES (13, ?, ?, ?, 1, ?, 0, 0)
        """,
        (created, created, created, key),
    )
    item_id = int(cur.lastrowid)

    # title fieldID=110, url fieldID=1, accessDate fieldID=27,
    # abstractNote fieldID=90
    for field_id, value in [
        (110, title),
        (1, url),
        (27, datetime.now(UTC).strftime("%Y-%m-%d")),
        (90, str(row.get("desc") or "").strip()),
    ]:
        if not value:
            continue
        value_id = ensure_item_data_value(conn, value)
        conn.execute(
            (
                "INSERT OR REPLACE INTO itemData(itemID, fieldID, valueID) "
                "VALUES (?, ?, ?)"
            ),
            (item_id, field_id, value_id),
        )

    for tag_name in parse_tags(str(row.get("tags") or "")):
        tag_id = ensure_tag(conn, tag_name)
        conn.execute(
            "INSERT OR IGNORE INTO itemTags(itemID, tagID, type) VALUES (?, ?, 0)",
            (item_id, tag_id),
        )

    annotations = row.get("annotations") or []
    if isinstance(annotations, list) and annotations:
        parts: list[str] = []
        for ann in annotations:
            if not isinstance(ann, dict):
                continue
            content = str(ann.get("content") or "").strip()
            comments = str(ann.get("comments") or "").strip()
            if content:
                parts.append(f"<blockquote>{escape(content)}</blockquote>")
            if comments:
                parts.append(f"<p><strong>Note:</strong> {escape(comments)}</p>")
        if parts:
            add_note_item(
                conn,
                parent_item_id=item_id,
                key_seed=key,
                note_html="\n".join(parts),
                date_added=created,
            )


def convert(
    input_path: Path_T,
    output_path: Path_T,
    zotero_source: Path_T,
) -> dict[str, int]:
    if output_path.exists():
        output_path.unlink()

    conn = sqlite3.connect(str(output_path))
    conn.execute("PRAGMA foreign_keys = ON")
    init_db(conn, zotero_source)

    bookmarks = 0
    with input_path.open(encoding="utf-8") as fp:
        for line in fp:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            if not isinstance(row, dict):
                continue
            add_bookmark(conn, row)
            bookmarks += 1

    conn.commit()
    tables = ["items", "itemData", "tags", "itemTags", "itemNotes"]
    counts = {
        t: conn.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0] for t in tables
    }
    conn.close()
    counts["bookmarks"] = bookmarks
    return counts


def main(argv: list[str], stdout: TextIOBase, cwd: Path_T) -> int:
    try:
        cfg = parse_cli(argv)
    except (StopIteration, ValueError) as err:
        print(err, file=stdout)
        return 2

    zotero_source = Path_T(cfg.zotero_source)
    if not zotero_source.is_absolute():
        zotero_source = (cwd / zotero_source).resolve()

    input_path = Path_T(cfg.input_path)
    if not input_path.is_absolute():
        input_path = (cwd / input_path).resolve()

    output_path = Path_T(cfg.output_path)
    if not output_path.is_absolute():
        output_path = (cwd / output_path).resolve()

    try:
        counts = convert(input_path, output_path, zotero_source)
    except Exception as err:  # pragma: no cover
        print(f"conversion failed: {err}", file=stdout)
        return 1

    print(
        (
            "zotero_source={} input={} output={} bookmarks={} items={} itemData={} "
            "tags={} itemTags={} itemNotes={}"
        ).format(
            zotero_source,
            input_path,
            output_path,
            counts["bookmarks"],
            counts["items"],
            counts["itemData"],
            counts["tags"],
            counts["itemTags"],
            counts["itemNotes"],
        ),
        file=stdout,
    )
    return 0


if __name__ == "__main__":
    def _script_io() -> int:
        from pathlib import Path
        from sys import argv, stdout

        return main(argv=list(argv), stdout=stdout, cwd=Path("."))

    raise SystemExit(_script_io())
