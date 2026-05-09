#!/usr/bin/env python3
"""Expand t.co URLs in bookmark sources or rendered blog items.

Usage:
    expand_tco_urls.py --input PATH [--cache FILE] [--next N] [--dry-run]

Input mode:
- If PATH is a .ndjson file, each JSON line is updated in-place for fields:
  - url
  - desc
  - annotations[].content
  - annotations[].comments
- If PATH is a directory, all *.md files below it are updated in-place.
"""

from __future__ import annotations

import json
import re
import time
from dataclasses import dataclass
from io import TextIOBase
from typing import TYPE_CHECKING, Any, Callable, Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

if TYPE_CHECKING:
    from pathlib import Path as Path_T
else:
    Path_T = Any

URL_RE = re.compile(r"https?://[^\s<>()]+")
DEFAULT_CACHE = "projects/diigo-bak/tco-expansions.json"
USAGE = (
    "usage: expand_tco_urls.py --input PATH [--cache FILE] "
    "[--next N] [--dry-run]"
)


@dataclass(frozen=True)
class Config:
    input_path: str
    cache_path: str
    next_count: int | None
    dry_run: bool


@dataclass(frozen=True)
class Stats:
    files_changed: int = 0
    lines_changed: int = 0
    urls_seen: int = 0
    urls_expanded: int = 0
    cache_added: int = 0


def parse_cli(argv: list[str]) -> Config:
    input_path = ""
    cache_path = DEFAULT_CACHE
    next_count: int | None = None
    dry_run = False

    it = iter(argv[1:])
    for token in it:
        if token in {"-h", "--help"}:
            raise ValueError(USAGE)
        if token == "--dry-run":
            dry_run = True
            continue
        if token == "--input":
            input_path = next(it)
            continue
        if token == "--cache":
            cache_path = next(it)
            continue
        if token == "--next":
            next_count = int(next(it))
            if next_count < 1:
                raise ValueError(f"--next must be >= 1\n{USAGE}")
            continue
        raise ValueError(f"unknown option: {token}\n{USAGE}")

    if not input_path:
        raise ValueError(f"missing --input\n{USAGE}")

    return Config(
        input_path=input_path,
        cache_path=cache_path,
        next_count=next_count,
        dry_run=dry_run,
    )


def load_cache(path: Path_T) -> dict[str, str]:
    if not path.exists():
        return {}
    raw = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(raw, dict):
        return {str(k): str(v) for k, v in raw.items()}
    return {}


def save_cache(path: Path_T, cache: dict[str, str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    ordered = {k: cache[k] for k in sorted(cache)}
    path.write_text(
        json.dumps(ordered, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def expand_tco(url: str, cache: dict[str, str]) -> str:
    hit = cache.get(url)
    if hit:
        return hit

    if urlparse(url).netloc.lower() != "t.co":
        cache[url] = url
        return url

    expanded = url
    try:
        req = Request(url, method="HEAD")
        with urlopen(req, timeout=3) as res:
            expanded = res.geturl()
    except (HTTPError, URLError, TimeoutError, ValueError):
        try:
            req = Request(url, method="GET")
            with urlopen(req, timeout=5) as res:
                expanded = res.geturl()
        except (HTTPError, URLError, TimeoutError, ValueError):
            expanded = url

    cache[url] = expanded
    return expanded


def expand_text(text: str, cache: dict[str, str]) -> tuple[str, int, int]:
    """Expand t.co URLs in text.

    Returns (new_text, urls_seen, urls_changed).

    >>> out, seen, changed = expand_text(
    ...     "see https://t.co/abc and https://example.org.",
    ...     {"https://t.co/abc": "https://final.example/x"},
    ... )
    >>> out
    'see https://final.example/x and https://example.org.'
    >>> (seen, changed)
    (2, 1)
    """
    seen = 0
    changed = 0
    parts: list[str] = []
    i = 0

    for m in URL_RE.finditer(text):
        parts.append(text[i:m.start()])
        raw_url = m.group(0)
        url = raw_url.rstrip(".,);:!?")
        trail = raw_url[len(url):]
        seen += 1
        expanded = expand_tco(url, cache)
        if expanded != url:
            changed += 1
        parts.append(expanded)
        parts.append(trail)
        i = m.end()

    parts.append(text[i:])
    return "".join(parts), seen, changed


def expand_ndjson(path: Path_T, cache: dict[str, str], dry_run: bool) -> Stats:
    files_changed = 0
    lines_changed = 0
    urls_seen = 0
    urls_expanded = 0

    out_lines: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        src = line.strip()
        if not src:
            continue

        row = json.loads(src)
        changed = False

        for key in ("url", "desc"):
            value = str(row.get(key) or "")
            new_value, seen, expanded = expand_text(value, cache)
            urls_seen += seen
            urls_expanded += expanded
            if new_value != value:
                row[key] = new_value
                changed = True

        ann = row.get("annotations") or []
        for idx, note in enumerate(ann):
            if not isinstance(note, dict):
                continue
            for key in ("content", "comments"):
                value = str(note.get(key) or "")
                new_value, seen, expanded = expand_text(value, cache)
                urls_seen += seen
                urls_expanded += expanded
                if new_value != value:
                    ann[idx][key] = new_value
                    changed = True

        if changed:
            lines_changed += 1
        out_lines.append(json.dumps(row, ensure_ascii=False))

    if lines_changed:
        files_changed = 1
        if not dry_run:
            path.write_text("\n".join(out_lines) + "\n", encoding="utf-8")

    return Stats(
        files_changed=files_changed,
        lines_changed=lines_changed,
        urls_seen=urls_seen,
        urls_expanded=urls_expanded,
        cache_added=0,
    )


def urls_in_text(text: str) -> list[str]:
    return [m.group(0).rstrip(".,);:!?") for m in URL_RE.finditer(text)]


def iter_row_text_values(row: dict[str, object]) -> Iterable[str]:
    yield str(row.get("url") or "")
    yield str(row.get("desc") or "")
    ann = row.get("annotations") or []
    if isinstance(ann, list):
        for note in ann:
            if not isinstance(note, dict):
                continue
            yield str(note.get("content") or "")
            yield str(note.get("comments") or "")


def expand_next_tco_from_ndjson(
    path: Path_T,
    cache: dict[str, str],
    next_count: int,
    progress: Callable[[str], None] | None = None,
) -> Stats:
    """Resolve next uncached t.co URLs from ndjson into cache.

    >>> rows = [
    ...     '{"url":"https://t.co/a","desc":"x","annotations":[]}',
    ...     (
    ...         '{"url":"https://example.org",'
    ...         '"desc":"see https://t.co/b","annotations":[]}'
    ...     ),
    ... ]
    >>> from pathlib import Path
    >>> p = Path("/tmp/expand_tco_urls-doctest.ndjson")
    >>> _ = p.write_text("\\n".join(rows) + "\\n", encoding="utf-8")
    >>> cache = {
    ...     "https://t.co/a": "https://final/a",
    ... }
    >>> s = expand_next_tco_from_ndjson(p, cache, 1)
    >>> (s.cache_added, s.urls_seen) == (1, 3)
    True
    >>> "https://t.co/b" in cache
    True
    """
    urls_seen = 0
    urls_expanded = 0
    to_expand: list[str] = []
    queued: set[str] = set()

    for line in path.read_text(encoding="utf-8").splitlines():
        src = line.strip()
        if not src:
            continue
        row = json.loads(src)
        if not isinstance(row, dict):
            continue
        for text in iter_row_text_values(row):
            for url in urls_in_text(text):
                urls_seen += 1
                if urlparse(url).netloc.lower() != "t.co":
                    continue
                if url in cache or url in queued:
                    continue
                to_expand.append(url)
                queued.add(url)
                if len(to_expand) >= next_count:
                    break
            if len(to_expand) >= next_count:
                break
        if len(to_expand) >= next_count:
            break

    total = len(to_expand)
    for done, short_url in enumerate(to_expand, start=1):
        expanded = expand_tco(short_url, cache)
        if expanded != short_url:
            urls_expanded += 1
        if progress is not None:
            progress(
                "fetched {}/{} urls_expanded={} cache_added={}".format(
                    done,
                    total,
                    urls_expanded,
                    total,
                )
            )

    return Stats(
        files_changed=0,
        lines_changed=0,
        urls_seen=urls_seen,
        urls_expanded=urls_expanded,
        cache_added=len(to_expand),
    )


def markdown_files(root: Path_T) -> Iterable[Path_T]:
    for p in sorted(root.rglob("*.md")):
        if p.is_file():
            yield p


def expand_directory(root: Path_T, cache: dict[str, str], dry_run: bool) -> Stats:
    files_changed = 0
    lines_changed = 0
    urls_seen = 0
    urls_expanded = 0

    for path in markdown_files(root):
        src = path.read_text(encoding="utf-8")
        out, seen, expanded = expand_text(src, cache)
        urls_seen += seen
        urls_expanded += expanded
        if out == src:
            continue
        files_changed += 1
        lines_changed += 1
        if not dry_run:
            path.write_text(out, encoding="utf-8")

    return Stats(
        files_changed=files_changed,
        lines_changed=lines_changed,
        urls_seen=urls_seen,
        urls_expanded=urls_expanded,
        cache_added=0,
    )


def merge_stats(a: Stats, b: Stats) -> Stats:
    return Stats(
        files_changed=a.files_changed + b.files_changed,
        lines_changed=a.lines_changed + b.lines_changed,
        urls_seen=a.urls_seen + b.urls_seen,
        urls_expanded=a.urls_expanded + b.urls_expanded,
        cache_added=a.cache_added + b.cache_added,
    )


def run(
    cfg: Config,
    cwd: Path_T,
    stdout: TextIOBase | None = None,
) -> tuple[Stats, Path_T, Path_T]:
    src = cwd / cfg.input_path
    cache_path = cwd / cfg.cache_path

    if not src.exists():
        raise FileNotFoundError(str(src))

    cache = load_cache(cache_path)

    if src.is_dir():
        if cfg.next_count is not None:
            raise ValueError("--next is only supported when --input is .ndjson")
        stats = expand_directory(src, cache, cfg.dry_run)
    elif src.suffix == ".ndjson":
        if cfg.next_count is not None:
            progress: Callable[[str], None] | None = None
            if stdout is not None:
                last_report = [time.monotonic()]

                def report(msg: str) -> None:
                    now = time.monotonic()
                    if now - last_report[0] > 5:
                        print(msg, file=stdout)
                        last_report[0] = now

                progress = report
            stats = expand_next_tco_from_ndjson(
                src,
                cache,
                cfg.next_count,
                progress=progress,
            )
        else:
            stats = expand_ndjson(src, cache, cfg.dry_run)
    else:
        raise ValueError("--input must be a directory or .ndjson file")

    if not cfg.dry_run:
        save_cache(cache_path, cache)

    return stats, src, cache_path


def main(argv: list[str], stdout: TextIOBase, cwd: Path_T) -> int:
    try:
        cfg = parse_cli(argv)
    except (StopIteration, ValueError) as err:
        print(err, file=stdout)
        return 2

    try:
        stats, src, cache_path = run(
            cfg=cfg,
            cwd=cwd,
            stdout=stdout,
        )
    except (FileNotFoundError, ValueError) as err:
        print(err, file=stdout)
        return 2

    print(
        (
            "input={} cache={} files_changed={} records_changed={} "
            "urls_seen={} urls_expanded={} cache_added={}"
        ).format(
            src,
            cache_path,
            stats.files_changed,
            stats.lines_changed,
            stats.urls_seen,
            stats.urls_expanded,
            stats.cache_added,
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
