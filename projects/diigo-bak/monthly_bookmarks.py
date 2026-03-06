#!/usr/bin/env python3
"""Generate monthly shared-bookmark roundup posts.

Usage:
    monthly_bookmarks.py [--repo-root DIR] [--input FILE]
                         [--min-tag-freq N] [--dry-run]
"""

from __future__ import annotations

import html
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime
from io import TextIOBase
from pathlib import Path as Path_T
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
TAG_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9 +._:/-]{0,47}$")
DEFAULT_INPUT = "projects/diigo-bak/diigo-bookmarks-shared.ndjson"
USAGE = (
    "usage: monthly_bookmarks.py [--repo-root DIR] [--input FILE] "
    "[--min-tag-freq N] [--dry-run]"
)
# Canonical mixed-case tags from page frontmatter on the main site branch.
# Keep this list in sync using check_mixed_case_tags.py.
MIXED_CASE_FRONTMATTER_TAGS = (
    "AAAI",
    "Agoric",
    "Austin",
    "BOS",
    "Boulder",
    "DEN",
    "Duke",
    "EDI",
    "HTML",
    "IndieWeb",
    "Internet",
    "Internet Computer",
    "KC",
    "NCE",
    "RChain",
    "RDU",
    "RdfAndSql",
    "SEA",
    "SFO",
    "SeedApplications",
    "URI",
    "UriSchemes",
    "VBA",
    "Web history",
    "hCard",
    "seL4",
)
MIXED_CASE_BY_FOLD = {
    tag.casefold(): tag for tag in MIXED_CASE_FRONTMATTER_TAGS
}


@dataclass(frozen=True)
class Bookmark:
    created: datetime
    title: str
    url: str
    tags: tuple[str, ...]
    desc: str
    annotations: tuple[tuple[str, str], ...]

    @property
    def ym(self) -> str:
        return self.created.strftime("%Y-%m")


@dataclass(frozen=True)
class Config:
    repo_root: str
    input_path: str
    min_tag_freq: int
    dry_run: bool


@dataclass(frozen=True)
class RenderedPost:
    relpath: str
    text: str


def parse_tags(raw: str | None) -> tuple[str, ...]:
    if not raw:
        return tuple()
    out: list[str] = []
    for piece in raw.split(","):
        src = piece.strip()
        if not src:
            continue
        tag = MIXED_CASE_BY_FOLD.get(src.casefold(), src.lower())
        if tag:
            out.append(tag)
    return tuple(out)


def parse_cli(argv: list[str]) -> Config:
    repo_root = "."
    input_path = DEFAULT_INPUT
    min_tag_freq = 5
    dry_run = False

    it = iter(argv[1:])
    for token in it:
        if token in {"-h", "--help"}:
            raise ValueError(USAGE)
        if token == "--dry-run":
            dry_run = True
            continue
        if token == "--repo-root":
            repo_root = next(it)
            continue
        if token == "--input":
            input_path = next(it)
            continue
        if token == "--min-tag-freq":
            min_tag_freq = int(next(it))
            continue
        raise ValueError(f"unknown option: {token}\n{USAGE}")

    return Config(
        repo_root=repo_root,
        input_path=input_path,
        min_tag_freq=min_tag_freq,
        dry_run=dry_run,
    )


def load_bookmarks(src: Path_T) -> list[Bookmark]:
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
            annotations_raw = row.get("annotations") or []
            annotations = tuple(
                (
                    str(a.get("content") or "").strip(),
                    str(a.get("comments") or "").strip(),
                )
                for a in annotations_raw
            )
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


def get_theme_terms(
    month_items: Iterable[Bookmark],
    month_tags: Counter[str],
) -> list[str]:
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


def yaml_scalar(value: str) -> str:
    """Render a YAML-safe quoted scalar."""
    return json.dumps(value, ensure_ascii=False)


def compact_text(text: str) -> str:
    """Collapse multiline / irregular spacing into one readable line."""
    return re.sub(r"\s+", " ", text).strip()


def safe_md_text(text: str) -> str:
    """Escape risky markdown / html characters for inline list rendering."""
    clean = compact_text(html.unescape(text))
    clean = re.sub(r"<[^>]*>", "", clean)
    clean = html.escape(clean, quote=False)
    clean = clean.replace("[", r"\[").replace("]", r"\]")
    return clean


def annotation_html(text: str) -> str:
    """Trusted annotation HTML content rendered inside <blockquote>."""
    return compact_text(html.unescape(text))


def inline_html_text(text: str) -> str:
    """Trusted plain text for inline HTML nodes."""
    return html.escape(compact_text(html.unescape(text)), quote=False)


def visible_tags(tags: tuple[str, ...]) -> list[str]:
    """Tags shown in post body; hide Diigo sentinel tag."""
    return [tag for tag in tags if tag != "no_tag"]


def group_bookmarks_by_month(
    bookmarks: Iterable[Bookmark],
) -> dict[str, list[Bookmark]]:
    by_month: dict[str, list[Bookmark]] = defaultdict(list)
    for bm in bookmarks:
        by_month[bm.ym].append(bm)
    return by_month


def body_for_month(ym: str, month_items: list[Bookmark]) -> str:
    """Render monthly bookmarks body with HTML list layout.

    Regression coverage for malformed source text:
    - multiline descriptions should stay on one list line
    - broken title fragments like "<meta ..." should be dropped

    >>> bm = Bookmark(
    ...     created=datetime.strptime("2021/01/07 00:00:00 +0000", DATE_FMT),
    ...     title='Remove Trump Tonight - The Atlantic<meta property="x"',
    ...     url="https://example.com",
    ...     tags=("tweet",),
    ...     desc="line1\\n\\nline2",
    ...     annotations=(("quoted\\ntext", "note\\ntext"),),
    ... )
    >>> out = body_for_month("2021-01", [bm])
    >>> "The Atlantic<meta" in out
    False
    >>> "Remove Trump Tonight - The Atlantic" in out
    True
    >>> "description:" in out
    False
    >>> "annotations:" in out
    False
    >>> "2021-01-07 tweet<br>" in out
    True
    >>> '<p class="bm-desc">line1 line2</p>' in out
    True
    >>> "<blockquote>quoted text</blockquote>" in out
    True
    >>> "<blockquote><p><strong>note:</strong> note text</p></blockquote>" in out
    True
    """
    month_label = datetime.strptime(f"{ym}-01", "%Y-%m-%d").strftime("%B %Y")
    lines = [f"Shared bookmarks saved in {month_label}.", ""]
    lines.append(f"- total bookmarks: {len(month_items)}")
    ann = sum(len(item.annotations) for item in month_items)
    lines.append(f"- total annotations captured: {ann}")
    lines.append("")
    lines.append("## Links")
    lines.append("")
    lines.append('<ul class="bookmarks">')
    for bm in sorted(month_items, key=lambda b: (b.created, b.title), reverse=True):
        day = bm.created.strftime("%Y-%m-%d")
        raw_title = bm.title
        if "<" in raw_title:
            raw_title = raw_title.split("<", 1)[0].rstrip()
        title = inline_html_text(raw_title) or bm.url
        url = html.escape(bm.url, quote=True)
        tags = visible_tags(bm.tags[:6])
        tag_text = " ".join(tags)
        lines.append("  <li>")
        lines.append(f'    <a href="{url}">{title}</a><br>')
        if tag_text:
            lines.append(f"    {day} {inline_html_text(tag_text)}<br>")
        else:
            lines.append(f"    {day}<br>")
        if bm.desc:
            lines.append(
                f'    <p class="bm-desc">{inline_html_text(bm.desc)}</p>'
            )
        if bm.annotations:
            for content, comments in bm.annotations:
                if content:
                    lines.append(
                        f"    <blockquote>{annotation_html(content)}</blockquote>"
                    )
                if comments:
                    lines.append(
                        "    <blockquote><p><strong>note:</strong> "
                        f"{annotation_html(comments)}</p></blockquote>"
                    )
        lines.append("  </li>")
    lines.append("</ul>")
    lines.append("")
    return "\n".join(lines)


def render_month_post(
    ym: str,
    month_items: list[Bookmark],
    global_tags: Counter[str],
    min_tag_freq: int,
) -> RenderedPost:
    """Render one monthly markdown page with YAML frontmatter.

    The title commonly contains a colon ("Bookmarks: ..."), so frontmatter
    serialization must quote it.

    >>> bm = Bookmark(
    ...     created=datetime.strptime("2024/02/01 00:00:00 +0000", DATE_FMT),
    ...     title="A page title",
    ...     url="https://example.com",
    ...     tags=("security",),
    ...     desc="",
    ...     annotations=(),
    ... )
    >>> post = render_month_post(
    ...     ym="2024-02",
    ...     month_items=[bm],
    ...     global_tags=Counter({"security": 1}),
    ...     min_tag_freq=1,
    ... )
    >>> import yaml
    >>> meta = yaml.safe_load(post.text.split("---", 2)[1])
    >>> "Bookmarks:" in meta["title"]
    True
    """
    year, mon = ym.split("-")
    month_tags = Counter(
        t
        for bm in month_items
        for t in bm.tags
        if keep_tag(t, global_tags, min_tag_freq)
    )
    tag_union = sorted(month_tags)
    tag_union = ["bookmarks", "diigo", "shared"] + [
        t for t in tag_union if t not in {"bookmarks", "diigo", "shared"}
    ]

    title = month_title(ym, month_items, month_tags)
    date = f"{ym}-01"
    relpath = f"pages/{year}/{mon}/bookmarks-{ym}.md"
    text = "\n".join(
        [
            "---",
            f"title: {yaml_scalar(title)}",
            f"date: {date}",
            "published: true",
            f"tags: {yaml_list(tag_union)}",
            "---",
            "",
            body_for_month(ym, month_items),
        ]
    )
    return RenderedPost(relpath=relpath, text=text)


def write_month_posts(
    bookmarks: list[Bookmark],
    repo_root: Path_T,
    *,
    min_tag_freq: int,
    dry_run: bool = False,
) -> int:
    global_tags: Counter[str] = Counter(t for bm in bookmarks for t in bm.tags)
    by_month = group_bookmarks_by_month(bookmarks)

    written = 0
    for ym, month_items in sorted(by_month.items()):
        post = render_month_post(
            ym=ym,
            month_items=month_items,
            global_tags=global_tags,
            min_tag_freq=min_tag_freq,
        )
        dst = repo_root / post.relpath
        if not dry_run:
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_text(post.text, encoding="utf-8")
        written += 1
    return written


def main(
    argv: list[str],
    stdout: TextIOBase,
    cwd: Path_T,
) -> int:
    try:
        cfg = parse_cli(argv)
    except (StopIteration, ValueError) as err:
        print(err, file=stdout)
        return 2

    repo_root = Path_T(cfg.repo_root)
    if not repo_root.is_absolute():
        repo_root = (cwd / repo_root).resolve()

    src = (repo_root / cfg.input_path).resolve()
    bookmarks = load_bookmarks(src)
    wrote = write_month_posts(
        bookmarks=bookmarks,
        repo_root=repo_root,
        min_tag_freq=cfg.min_tag_freq,
        dry_run=cfg.dry_run,
    )
    print(f"loaded={len(bookmarks)} monthly_posts={wrote} input={src}", file=stdout)
    return 0


if __name__ == "__main__":
    def _script_io() -> int:
        from pathlib import Path
        from sys import argv, stdout

        return main(argv=list(argv), stdout=stdout, cwd=Path("."))

    raise SystemExit(_script_io())
