#!/usr/bin/env python3
# SPDX-License-Identifier: CC0-1.0
"""Parse adb content query output for SMS/MMS into a unified JSON message array.

SMS and MMS are stored in separate Android content providers.  SMS carries its
body directly; MMS carries text parts in content://mms/part keyed by the MMS
_id (mid).  This script merges both into a single JSON array of messages with a
common schema:

  { "id": int, "kind": "sms"|"mms", "address": str, "body": str, "date": int }

For MMS, "address" is currently omitted because the addr table was not dumped;
the body is assembled from text/plain parts.

Usage:
  parse_sms.py --sms sms-dump.txt --mms sms-mms.txt > msgs.json
  parse_sms.py --sms sms-dump.txt --strip-row    # normalized SMS text only
  parse_sms.py --sms sms-dump.txt --filter-addr +17314326576
  parse_sms.py --sms sms-dump.txt --strip-row --filter-addr +17314326576
"""
import argparse
import json
import re


DATE_RE = re.compile(r", date=(\d+)\n")
HEAD_RE = re.compile(r"Row: \d+ _id=(\d+), address=(.*?), body=(.*)$", re.S)
ROW_RE = re.compile(r"^Row: \d+ _id=\d+, ")
MMS_HEAD_RE = re.compile(r"Row: \d+ _id=(\d+), date=(\d+), sub=(?:NULL|[^,]*), ct_t=(.*?), ct_l=(?:NULL|.*)$", re.S)
PART_HEAD_RE = re.compile(
    r"Row: \d+ _id=(\d+), mid=(\d+), ct=(.*?), text=(.*)$",
    re.S,
)


def _split_sms_records(text: str) -> list[tuple[str, str]]:
    """Split SMS adb output into (record_head, date) pairs.

    The ', date=<n>\n' terminator is the reliable boundary; message bodies
    can contain lines that look like new records.
    """
    parts = DATE_RE.split(text)
    records = []
    for i in range(0, len(parts) - 1, 2):
        records.append((parts[i], parts[i + 1]))
    return records


def _split_rows(text: str) -> list[str]:
    """Split adb output on Row boundaries.

    SMS bodies may contain lines that look like Row: headers, so SMS uses
    _split_sms_records.  The MMS section and MMS part section have real
    Row: boundaries and may contain embedded newlines in text fields, so we
    split on the Row prefix instead.
    """
    rows = re.split(r"\n(?=Row: \d+ _id=)", text.strip())
    return [r for r in rows if r]


def parse_sms(text: str) -> list[dict]:
    msgs = []
    for head, date in _split_sms_records(text):
        m = HEAD_RE.match(head)
        if m:
            msgs.append({
                "id": int(m.group(1)),
                "kind": "sms",
                "address": m.group(2),
                "body": m.group(3).strip(),
                "date": int(date),
            })
    return msgs


def parse_mms(text: str) -> list[dict]:
    if "---MMS_PARTS---" not in text:
        return []
    mms_section, part_section = text.split("---MMS_PARTS---", 1)

    mms_rows = {}
    for row in _split_rows(mms_section):
        m = MMS_HEAD_RE.match(row)
        if m:
            mid = int(m.group(1))
            # MMS date is epoch seconds; SMS date is epoch millis. Normalize to millis.
            mms_rows[mid] = {
                "id": mid,
                "kind": "mms",
                "address": "",
                "body": "",
                "date": int(m.group(2)) * 1000,
            }

    # Assemble text/plain parts by mid.  Some carriers emit a duplicate empty
    # text/plain part after the real one; keep the first non-empty text part.
    bodies: dict[int, list[str]] = {mid: [] for mid in mms_rows}
    for row in _split_rows(part_section):
        m = PART_HEAD_RE.match(row)
        if not m:
            continue
        pid, mid, ct, body_text = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)
        if ct != "text/plain":
            continue
        if mid not in bodies:
            # Part without a matching MMS header; ignore.
            continue
        if body_text is not None and body_text != "NULL":
            body_text = body_text.strip()
            if body_text:
                bodies[mid].append(body_text)

    for mid, parts in bodies.items():
        non_empty = [p for p in parts if p]
        mms_rows[mid]["body"] = non_empty[0] if non_empty else ""

    return list(mms_rows.values())


def normalize_sms(text: str, filter_addr: str | None = None) -> str:
    parts = DATE_RE.split(text)
    out = []
    for i in range(0, len(parts) - 1, 2):
        head, date = parts[i], parts[i + 1]
        if filter_addr and f"address={filter_addr}" in head:
            continue
        head = ROW_RE.sub("", head, count=1)
        out.append(head + ", date=" + date + "\n")
    return "".join(out)


def build_arg_parser(cwd) -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        description="Parse SMS/MMS adb dumps into a unified JSON message array."
    )
    ap.add_argument("--sms", type=cwd.joinpath, help="path to sms-dump.txt (content://sms)")
    ap.add_argument("--mms", type=cwd.joinpath, help="path to sms-mms.txt (content://mms + parts)")
    ap.add_argument(
        "--strip-row",
        action="store_true",
        help="strip Row:N _id=N prefix for stable diff output (SMS only)",
    )
    ap.add_argument(
        "--filter-addr",
        metavar="ADDR",
        help="exclude records from this address (SMS only)",
    )
    return ap


def main(argv, stdout, stderr, cwd) -> int:
    ap = build_arg_parser(cwd)
    args = ap.parse_args(argv[1:])

    if not args.sms:
        print("--sms is required", file=stderr)
        return 2

    sms_text = args.sms.read_text(encoding="utf-8")

    if args.strip_row:
        try:
            stdout.write(normalize_sms(sms_text, args.filter_addr))
        except BrokenPipeError:
            return 0
        return 0

    msgs = parse_sms(sms_text)
    if args.mms:
        msgs.extend(parse_mms(args.mms.read_text(encoding="utf-8")))

    if args.filter_addr:
        msgs = [m for m in msgs if m.get("address") == args.filter_addr]

    msgs.sort(key=lambda m: m["date"])
    json.dump(msgs, stdout, indent=2)
    return 0


if __name__ == "__main__":
    def _script_io() -> int:
        from pathlib import Path
        from sys import argv, stdout, stderr

        return main(list(argv), stdout, stderr, Path.cwd())

    raise SystemExit(_script_io())
