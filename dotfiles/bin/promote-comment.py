#!/usr/bin/env python3
"""Promote a GitHub issue comment to a blog post.

Usage: promote-comment.py <comment-url>
Example: promote-comment.py https://github.com/dckc/madmode-blog/issues/237#issuecomment-4228178391
"""

import os
import re
import subprocess
import sys
import json
from datetime import datetime
from pathlib import Path

BLOG_ROOT = Path("/home/connolly/projects/madmode-blog")
PAGES_DIR = BLOG_ROOT / "pages"

URL_RE = re.compile(
    r"^https://github\.com/([^/]+)/([^/]+)/issues/([0-9]+)#issuecomment-([0-9]+)$"
)


def gh_api(endpoint: str) -> dict:
    """Run a gh api command and return parsed JSON."""
    result = subprocess.run(
        ["gh", "api", endpoint],
        capture_output=True,
        text=True,
        check=True,
    )
    return json.loads(result.stdout)


def main():
    if len(sys.argv) < 2:
        print("Usage: promote-comment.py <comment-url>")
        sys.exit(1)

    comment_url = sys.argv[1]
    match = URL_RE.match(comment_url)
    if not match:
        print("Error: Invalid comment URL format")
        print("Expected: https://github.com/<owner>/<repo>/issues/<issue>#issuecomment-<id>")
        sys.exit(1)

    owner, repo, issue_num, comment_id = match.groups()

    print(f"Fetching comment {comment_id} from {owner}/{repo}#{issue_num}...")

    comment = gh_api(f"repos/{owner}/{repo}/issues/comments/{comment_id}")
    issue = gh_api(f"repos/{owner}/{repo}/issues/{issue_num}")

    body = comment["body"]
    created_at = comment["created_at"]
    issue_title = issue["title"]

    dt = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
    year = dt.strftime("%Y")
    month = dt.strftime("%m")
    day = dt.strftime("%d")
    date_str = f"{year}-{month}-{day}"

    out_dir = PAGES_DIR / year / month
    out_dir.mkdir(parents=True, exist_ok=True)

    filename = f"{repo}-{issue_num}-issuecomment-{comment_id}.md"
    filepath = out_dir / filename

    if filepath.exists():
        print(f"Error: File already exists: {filepath}")
        sys.exit(1)

    title = f"{issue_title} (comment)"
    summary = body.lstrip("#").strip().split("\n")[0][:120]

    frontmatter = (
        f"---\n"
        f"title: \"{title}\"\n"
        f"date: {date_str}\n"
        f"tags: [\"github\", \"syndicated\"]\n"
        f"published: true\n"
        f"summary: \"{summary}\"\n"
        f"---\n"
    )

    syndication = (
        f"\n---\n\n"
        f"*Originally appeared as [a comment on {issue_title}]({comment_url}).*\n"
    )

    filepath.write_text(frontmatter + "\n" + body + syndication, encoding="utf-8")

    print(f"Created blog post: {filepath}")
    print(f"URL will be: /{year}/{month}/{filename}")
    print()
    print("Next steps:")
    print("1. Review and edit the file if needed")
    print("2. Adjust tags and summary as appropriate")
    print("3. Commit and deploy")


if __name__ == "__main__":
    main()
