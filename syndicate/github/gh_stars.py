#!/usr/bin/env python3
import json
import subprocess
import sys
from pathlib import Path
import time
import logging

log = logging.getLogger(__name__)

OUT = Path(sys.argv[1] if len(sys.argv) > 1 else "github-stars.ndjson")

QUERY = """
query($cursor: String) {
  viewer {
    starredRepositories(
      first: 100
      after: $cursor
      orderBy: {field: STARRED_AT, direction: DESC}
    ) {
      pageInfo {
        hasNextPage
        endCursor
      }
      edges {
        starredAt
        node {
          id
          name
          nameWithOwner
          url
          description
          homepageUrl
          stargazerCount
          forkCount
          diskUsage
          isArchived
          isDisabled
          isEmpty
          isFork
          isMirror
          isPrivate
          isTemplate
          createdAt
          updatedAt
          pushedAt
          primaryLanguage {
            name
            color
          }
          licenseInfo {
            key
            name
            spdxId
            url
          }
          repositoryTopics(first: 20) {
            nodes {
              topic {
                name
              }
            }
          }
        }
      }
    }
  }
}
"""


def gh_graphql(cursor, retries=6):
    args = ["gh", "api", "graphql", "-f", f"query={QUERY}"]
    args += ["-F", "cursor=" if cursor is None else f"cursor={cursor}"]

    for attempt in range(retries):
        try:
            p = subprocess.run(  # XXX AMBIENT
                args,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            return json.loads(p.stdout)

        except subprocess.CalledProcessError as e:
            msg = e.stderr.strip()
            transient = (
                "HTTP 502" in msg
                or "HTTP 503" in msg
                or "HTTP 504" in msg
                or "secondary rate limit" in msg.lower()
            )

            if not transient or attempt == retries - 1:
                raise RuntimeError(f"gh api failed: {msg}") from e

            delay = 2**attempt
            log.info(f"warning: {msg}; retrying in {delay}s")
            time.sleep(delay)


def existing_watermark(path):
    if not path.exists():
        return None

    newest = None
    with path.open() as f:
        for line in f:
            if not line.strip():
                continue
            item = json.loads(line)
            starred_at = item["starredAt"]
            if newest is None or starred_at > newest:
                newest = starred_at

    return newest


def simplify(edge):
    repo = edge["node"]
    topics = repo.pop("repositoryTopics", {"nodes": []})
    repo["topics"] = [node["topic"]["name"] for node in topics.get("nodes", [])]
    repo["starredAt"] = edge["starredAt"]
    return repo


def main():
    since = existing_watermark(OUT)
    cursor = None
    added = 0

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)sZ %(levelname)s %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    page = 1
    with OUT.open("a") as out:
        while True:
            log.info(f"page: {page}; cursor: {cursor}")
            data = gh_graphql(cursor)
            stars = data["data"]["viewer"]["starredRepositories"]

            for edge in stars["edges"]:
                starred_at = edge["starredAt"]

                if since is not None and starred_at <= since:
                    log.info(f"added {added} new stars")
                    return

                out.write(json.dumps(simplify(edge), separators=(",", ":")) + "\n")
                added += 1

            if not stars["pageInfo"]["hasNextPage"]:
                break

            cursor = stars["pageInfo"]["endCursor"]
            page += 1

    log.info(f"added {added} new stars")


if __name__ == "__main__":
    main()
