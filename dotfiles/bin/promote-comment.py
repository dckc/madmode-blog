#!/usr/bin/env python3
"""Promote a GitHub issue comment to a blog post.

Usage: promote-comment.py <comment-url>
Example: promote-comment.py https://github.com/dckc/madmode-blog/issues/237#issuecomment-4228178391
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path as Path_T
from typing import Callable, TextIO

URL_RE = re.compile(
    r"^https://github\.com/([^/]+)/([^/]+)/issues/([0-9]+)#issuecomment-([0-9]+)$"
)


@dataclass(frozen=True)
class CommentInfo:
    owner: str
    repo: str
    issue_num: str
    comment_id: str


@dataclass(frozen=True)
class GitHubData:
    body: str
    created_at: str
    issue_title: str


GhApi = Callable[[str], dict]


def parse_comment_url(url: str) -> CommentInfo | None:
    match = URL_RE.match(url)
    if not match:
        return None
    owner, repo, issue_num, comment_id = match.groups()
    return CommentInfo(owner, repo, issue_num, comment_id)


def fetch_github_data(info: CommentInfo, gh_api: GhApi) -> GitHubData:
    comment = gh_api(f"repos/{info.owner}/{info.repo}/issues/comments/{info.comment_id}")
    issue = gh_api(f"repos/{info.owner}/{info.repo}/issues/{info.issue_num}")
    return GitHubData(
        body=comment["body"],
        created_at=comment["created_at"],
        issue_title=issue["title"],
    )


def parse_date(created_at: str) -> tuple[str, str, str, str]:
    dt = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
    year = dt.strftime("%Y")
    month = dt.strftime("%m")
    day = dt.strftime("%d")
    date_str = f"{year}-{month}-{day}"
    return year, month, day, date_str


def build_frontmatter(issue_title: str, date_str: str, summary: str) -> str:
    return (
        f"---\n"
        f'title: "{issue_title} (comment)"\n'
        f"date: {date_str}\n"
        f'tags: ["github", "syndicated"]\n'
        f"published: true\n"
        f'summary: "{summary}"\n'
        f"---\n"
    )


def build_syndication(issue_title: str, comment_url: str) -> str:
    return (
        f"\n---\n\n"
        f"*Originally appeared as [a comment on {issue_title}]({comment_url}).*\n"
    )


def build_post_content(body: str, issue_title: str, comment_url: str, date_str: str) -> str:
    summary = body.lstrip("#").strip().split("\n")[0][:120]
    frontmatter = build_frontmatter(issue_title, date_str, summary)
    syndication = build_syndication(issue_title, comment_url)
    return frontmatter + "\n" + body + syndication


def promote_comment(
    comment_url: str,
    *,
    blog_root: Path_T,
    gh_api: GhApi,
    stdout: TextIO,
) -> int:
    info = parse_comment_url(comment_url)
    if info is None:
        print("Error: Invalid comment URL format", file=stdout)
        print("Expected: https://github.com/<owner>/<repo>/issues/<issue>#issuecomment-<id>", file=stdout)
        return 1

    print(f"Fetching comment {info.comment_id} from {info.owner}/{info.repo}#{info.issue_num}...", file=stdout)

    data = fetch_github_data(info, gh_api)
    year, month, day, date_str = parse_date(data.created_at)

    out_dir = blog_root / "pages" / year / month
    out_dir.mkdir(parents=True, exist_ok=True)

    filename = f"{info.repo}-{info.issue_num}-issuecomment-{info.comment_id}.md"
    filepath = out_dir / filename

    if filepath.exists():
        print(f"Error: File already exists: {filepath}", file=stdout)
        return 1

    content = build_post_content(data.body, data.issue_title, comment_url, date_str)
    filepath.write_text(content, encoding="utf-8")

    print(f"Created blog post: {filepath}", file=stdout)
    print(f"URL will be: /{year}/{month}/{filename}", file=stdout)
    print(file=stdout)
    print("Next steps:", file=stdout)
    print("1. Review and edit the file if needed", file=stdout)
    print("2. Adjust tags and summary as appropriate", file=stdout)
    print("3. Commit and deploy", file=stdout)
    return 0


if __name__ == "__main__":
    def script_entry() -> int:
        import json
        import subprocess
        import sys
        from pathlib import Path

        # minor: attentuation should happen in main()
        # we should pass subprocess.run , a stdlib object
        def gh_api(endpoint: str) -> dict:
            result = subprocess.run(
                ["gh", "api", endpoint],
                capture_output=True,
                text=True,
                check=True,
            )
            return json.loads(result.stdout)

        # arg parsing / checking should be in main()
        # script_entry() should perform no effects other than import
        if len(sys.argv) < 2:
            print("Usage: promote-comment.py <comment-url>", file=sys.stderr)
            return 1

        # we should call main(...) here
        return promote_comment(
            sys.argv[1],
            # attenuation from home() should be in main()
            blog_root=Path.home() / "projects" / "madmode-blog",
            gh_api=gh_api,
            # should use logging; stdout is for data
            stdout=sys.stdout,
        )

    raise SystemExit(script_entry())
