#!/usr/bin/env python3
"""Incrementally export GitHub stars from the ``gh`` CLI to NDJSON.

Usage:
    python3 syndicate/github/gh_stars.py [stars.json]
"""

import json
import logging
from subprocess import PIPE

log = logging.getLogger(__name__)

# This script follows DisciplinedPython style:
# https://github.com/dckc/awesome-ocap/wiki/DisciplinedPython
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


def is_transient_graphql_error(error):
    msg = str(error)
    return (
        "HTTP 502" in msg
        or "HTTP 503" in msg
        or "HTTP 504" in msg
        or "secondary rate limit" in msg.lower()
    )


def with_retries(action, is_transient, sleep, retries=6):
    for attempt in range(retries):
        try:
            return action()

        except RuntimeError as e:
            if not is_transient(e) or attempt == retries - 1:
                raise

            delay = 2**attempt
            log.info(f"warning: {e}; retrying in {delay}s")
            sleep(delay)


class MyStars:
    def __init__(self, run, sleep):
        self.__run = run
        self.__sleep = sleep

    def query(self, cursor):
        args = ["gh", "api", "graphql", "-f", f"query={QUERY}"]
        args += ["-F", "cursor=" if cursor is None else f"cursor={cursor}"]

        def request():
            p = self.__run(
                args,
                check=True,
                stdout=PIPE,
                stderr=PIPE,
                text=True,
            )
            return json.loads(p.stdout)

        return with_retries(
            request,
            is_transient_graphql_error,
            self.__sleep,
        )


def try_ndjson(path):
    try:
        with path.open("r", encoding="utf-8") as f:
            yield from (json.loads(line) for line in f if line.strip())
    except FileNotFoundError:
        return


def simplify(edge):
    repo = edge["node"]
    topics = repo.get("repositoryTopics", {"nodes": []})
    return {
        **{key: value for key, value in repo.items() if key != "repositoryTopics"},
        "topics": [node["topic"]["name"] for node in topics.get("nodes", [])],
        "starredAt": edge["starredAt"],
    }


def fetch_new_stars(my_stars, since):
    cursor = None

    while True:
        data = my_stars.query(cursor)
        stars = data["data"]["viewer"]["starredRepositories"]
        edges = stars["edges"]
        new_stars = (
            edges
            if since is None
            else [edge for edge in edges if edge["starredAt"] > since]
        )

        yield new_stars

        if len(new_stars) < len(edges):
            break

        if not stars["pageInfo"]["hasNextPage"]:
            break

        cursor = stars["pageInfo"]["endCursor"]


def main(argv, cwd, run, sleep):
    fname = argv[1] if len(argv) > 1 else "stars.json"
    out = cwd / fname

    since = max((item["starredAt"] for item in try_ndjson(out)), default=None)
    added = 0

    each_page = fetch_new_stars(MyStars(run, sleep), since)
    with out.open("a", encoding="utf-8") as f:
        for page, new_stars in enumerate(each_page, 1):
            log.info(f"page: {page}; new stars: {len(new_stars)}")
            for edge in new_stars:
                ndjson = json.dumps(simplify(edge)) + "\n"
                f.write(ndjson)
                added += 1

    log.info(f"added {added} new stars")


if __name__ == "__main__":

    def _script_io():
        import logging
        from subprocess import run
        from sys import argv
        from time import sleep
        from pathlib import Path

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)sZ %(levelname)s %(message)s",
            datefmt="%Y-%m-%dT%H:%M:%S",
        )

        return main(
            argv=list(argv),
            cwd=Path.cwd(),
            run=run,
            sleep=sleep,
        )

    raise SystemExit(_script_io())
