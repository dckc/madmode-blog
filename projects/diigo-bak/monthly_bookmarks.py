#!/usr/bin/env python3
"""Generate monthly bookmark roundup posts from Diigo shared export."""

from __future__ import annotations

import argparse
import html
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable
from urllib.parse import urlparse


DATE_FMT = "%Y/%m/%d %H:%M:%S %z"
STOP_TAGS = {
    "article",
    "no_tag",
    "problem",
    "tweet",
    "web",
    "toread",
    "todo",
    "someday",
    "readlater",
    "***",
    "****",
}
STOP_WORDS = {
    "amp",
    "about",
    "after",
    "article",
    "also",
    "another",
    "blog",
    "bookmark",
    "bookmarks",
    "com",
    "could",
    "free",
    "from",
    "google",
    "have",
    "http",
    "https",
    "into",
    "just",
    "link",
    "more",
    "most",
    "news",
    "org",
    "open",
    "page",
    "pages",
    "post",
    "problem",
    "quot",
    "read",
    "some",
    "that",
    "their",
    "there",
    "these",
    "they",
    "this",
    "those",
    "using",
    "what",
    "when",
    "where",
    "which",
    "will",
    "with",
    "www",
    "your",
    "untitled",
}
WORD_RE = re.compile(r"[A-Za-z][A-Za-z0-9_+-]{2,}")
TAG_RE = re.compile(r"^[a-z0-9][a-z0-9 +._:/-]{0,47}$")


@dataclass(frozen=True)
class Bookmark:
    created: datetime
    title: str
    url: str
    tags: tuple[str, ...]
    desc: str
    annotations: int

    @property
    def ym(self) -> str:
        return self.created.strftime("%Y-%m")


def parse_tags(raw: str | None) -> tuple[str, ...]:
    if not raw:
        return tuple()
    out: list[str] = []
    for piece in raw.split(","):
        tag = piece.strip().lower()
        if tag:
            out.append(tag)
    return tuple(out)


def load_bookmarks(src: Path) -> list[Bookmark]:
    items: list[Bookmark] = []
    with src.open(encoding="utf-8") as fp:
        for line in fp:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            created = datetime.strptime(row["created_at"], DATE_FMT)
            title = str(row.get("title") or row.get("url") or "").strip()
            desc = str(row.get("desc") or "").strip()
            tags = parse_tags(row.get("tags"))
            annotations = len(row.get("annotations") or [])
            items.append(
                Bookmark(
                    created=created,
                    title=title,
                    url=str(row["url"]).strip(),
                    tags=tags,
                    desc=desc,
                    annotations=annotations,
                )
            )
    return items


def keep_tag(tag: str, global_counts: Counter[str], min_freq: int) -> bool:
    if len(tag) < 2:
        return False
    if tag in STOP_TAGS:
        return False
    if len(tag) > 48:
        return False
    if not TAG_RE.match(tag):
        return False
    if global_counts[tag] < min_freq:
        return False
    return True


def short_host(url: str) -> str:
    host = urlparse(url).netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    return host


def get_theme_terms(month_items: Iterable[Bookmark], month_tags: Counter[str]) -> list[str]:
    weighted = Counter(month_tags)
    title_words: Counter[str] = Counter()
    hosts: Counter[str] = Counter()

    for bm in month_items:
        hosts[short_host(bm.url)] += 1
        for m in WORD_RE.findall(html.unescape(bm.title).lower()):
            if m in STOP_WORDS or len(m) < 4:
                continue
            title_words[m] += 1

    for word, count in title_words.items():
        if count >= 2:
            weighted[word] += count

    for host, count in hosts.items():
        if count >= 6 and host:
            stem = host.split(".")[0]
            if (
                stem
                and len(stem) >= 3
                and stem not in STOP_WORDS
                and stem not in {"twitter", "youtube", "wikipedia"}
            ):
                weighted[stem] += max(1, count // 4)

    picks: list[str] = []
    for term, _ in weighted.most_common():
        if term in STOP_TAGS or term == "bookmarks":
            continue
        if term in picks:
            continue
        picks.append(term)
        if len(picks) >= 3:
            break
    return picks


def month_title(ym: str, month_items: list[Bookmark], month_tags: Counter[str]) -> str:
    year, mon = ym.split("-")
    month_label = datetime.strptime(f"{ym}-01", "%Y-%m-%d").strftime("%B %Y")
    themes = get_theme_terms(month_items, month_tags)
    if not themes:
        return f"{month_label} Bookmarks"
    if len(themes) == 1:
        bits = themes[0]
    elif len(themes) == 2:
        bits = f"{themes[0]} and {themes[1]}"
    else:
        bits = f"{themes[0]}, {themes[1]}, and {themes[2]}"
    return f"{month_label} Bookmarks: {bits}"


def yaml_list(items: list[str]) -> str:
    if not items:
        return "[]"
    quoted = [json.dumps(x, ensure_ascii=False) for x in items]
    return "[{}]".format(", ".join(quoted))


def body_for_month(ym: str, month_items: list[Bookmark]) -> str:
    month_label = datetime.strptime(f"{ym}-01", "%Y-%m-%d").strftime("%B %Y")
    lines = [f"Shared bookmarks saved in {month_label}.", ""]
    lines.append(f"- total bookmarks: {len(month_items)}")
    ann = sum(item.annotations for item in month_items)
    lines.append(f"- total annotations captured: {ann}")
    lines.append("")
    lines.append("## Links")
    lines.append("")
    for bm in sorted(month_items, key=lambda b: (b.created, b.title), reverse=True):
        day = bm.created.strftime("%Y-%m-%d")
        title = bm.title.replace("\n", " ").strip() or bm.url
        tags = ", ".join(bm.tags[:6]) if bm.tags else ""
        if tags:
            lines.append(f"- {day}: [{title}]({bm.url})  _(tags: {tags})_")
        else:
            lines.append(f"- {day}: [{title}]({bm.url})")
    lines.append("")
    return "\n".join(lines)


def write_month_posts(
    bookmarks: list[Bookmark],
    out_pages: Path,
    *,
    min_tag_freq: int,
    dry_run: bool = False,
) -> int:
    global_tags: Counter[str] = Counter(
        t for bm in bookmarks for t in bm.tags
    )

    by_month: dict[str, list[Bookmark]] = defaultdict(list)
    for bm in bookmarks:
        by_month[bm.ym].append(bm)

    written = 0
    for ym, month_items in sorted(by_month.items()):
        year, mon = ym.split("-")
        month_tags = Counter(
            t for bm in month_items for t in bm.tags if keep_tag(t, global_tags, min_tag_freq)
        )
        tag_union = sorted(month_tags)
        tag_union = ["bookmarks", "diigo", "shared"] + [t for t in tag_union if t not in {"bookmarks", "diigo", "shared"}]

        title = month_title(ym, month_items, month_tags)
        date = f"{ym}-01"
        rel = Path("pages") / year / mon / f"bookmarks-{ym}.md"
        dst = out_pages.parent / rel
        text = "\n".join(
            [
                "---",
                f"title: {title}",
                f"date: {date}",
                "published: true",
                f"tags: {yaml_list(tag_union)}",
                "---",
                "",
                body_for_month(ym, month_items),
            ]
        )
        if not dry_run:
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_text(text, encoding="utf-8")
        written += 1
    return written


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--input",
        default="projects/diigo-bak/diigo-bookmarks-shared.ndjson",
        help="Path to shared bookmark NDJSON export.",
    )
    p.add_argument(
        "--repo-root",
        default=".",
        help="Path to madmode-blog repo root.",
    )
    p.add_argument(
        "--min-tag-freq",
        type=int,
        default=5,
        help="Exclude tags that occur fewer than this count globally.",
    )
    p.add_argument("--dry-run", action="store_true")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()
    src = (repo_root / args.input).resolve()
    pages_dir = repo_root / "pages"

    bookmarks = load_bookmarks(src)
    wrote = write_month_posts(
        bookmarks,
        pages_dir,
        min_tag_freq=args.min_tag_freq,
        dry_run=args.dry_run,
    )
    print(f"loaded={len(bookmarks)} monthly_posts={wrote} input={src}")


if __name__ == "__main__":
    main()
