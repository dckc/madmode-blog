#!/usr/bin/env python3
"""Check non-lowercase page tags against the canonical allowlist.

Usage:
    check_mixed_case_tags.py [--repo-root DIR] [--pages-dir DIR]
"""

from __future__ import annotations

import re
from io import TextIOBase
from typing import TYPE_CHECKING, Any

from monthly_bookmarks import MIXED_CASE_FRONTMATTER_TAGS

USAGE = "usage: check_mixed_case_tags.py [--repo-root DIR] [--pages-dir DIR]"

if TYPE_CHECKING:
    from pathlib import Path as Path_T
else:
    Path_T = Any


def parse_cli(argv: list[str]) -> tuple[str, str]:
    repo_root = "."
    pages_dir = "pages"

    it = iter(argv[1:])
    for token in it:
        if token in {"-h", "--help"}:
            raise ValueError(USAGE)
        if token == "--repo-root":
            repo_root = next(it)
            continue
        if token == "--pages-dir":
            pages_dir = next(it)
            continue
        raise ValueError(f"unknown option: {token}\n{USAGE}")

    return repo_root, pages_dir


def top_meta_block(lines: list[str]) -> list[str]:
    """Return top metadata block for either style (yaml fence or loose header)."""
    if lines and lines[0].strip() == "---":
        out: list[str] = []
        for line in lines[1:]:
            if line.strip() == "---":
                break
            out.append(line)
        return out

    out: list[str] = []
    for line in lines:
        if not line.strip():
            break
        out.append(line)
    return out


def extract_nonlower_tags(path: Path_T) -> set[str]:
    out: set[str] = set()
    text = path.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    for line in top_meta_block(lines):
        m = re.match(r"^tags:\s*\[(.*)\]\s*$", line.strip())
        if not m:
            continue
        for piece in m.group(1).split(","):
            tag = piece.strip().strip('"\'')
            if tag and tag != tag.lower():
                out.add(tag)
    return out


def find_nonlower_tags(pages_root: Path_T) -> set[str]:
    tags: set[str] = set()
    for page in sorted(pages_root.rglob("*.md")):
        if page.is_file():
            tags.update(extract_nonlower_tags(page))
    return tags


def main(argv: list[str], stdout: TextIOBase, cwd: Path_T) -> int:
    try:
        repo_root_raw, pages_dir_raw = parse_cli(argv)
    except (StopIteration, ValueError) as err:
        print(err, file=stdout)
        return 2

    repo_root = cwd / repo_root_raw
    pages_root = repo_root / pages_dir_raw

    if not pages_root.exists():
        print(f"missing pages dir: {pages_root}", file=stdout)
        return 2

    found = find_nonlower_tags(pages_root)
    expected = set(MIXED_CASE_FRONTMATTER_TAGS)

    extra = sorted(found - expected, key=str.casefold)
    missing = sorted(expected - found, key=str.casefold)

    if extra or missing:
        print("mixed-case tag mismatch", file=stdout)
        if extra:
            print("extra tags in pages (not in allowlist):", file=stdout)
            for tag in extra:
                print(f"- {tag}", file=stdout)
        if missing:
            print("missing tags in pages (still in allowlist):", file=stdout)
            for tag in missing:
                print(f"- {tag}", file=stdout)
        return 1

    print(f"ok: {len(found)} mixed-case tags match allowlist", file=stdout)
    return 0


if __name__ == "__main__":
    def _script_io() -> int:
        from pathlib import Path
        from sys import argv, stdout

        return main(argv=list(argv), stdout=stdout, cwd=Path("."))

    raise SystemExit(_script_io())
