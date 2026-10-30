#!/usr/bin/env python3
"""Import a post's CSL-JSON sources into a named collection in the running Zotero."""

import argparse
import json
import logging
from dataclasses import dataclass
from urllib.error import HTTPError
from urllib.parse import quote, urlencode, urljoin
from urllib.request import Request

from csl_bib import publishable


def cli(argv: list[str]) -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("sources", help="CSL-JSON file, e.g. pages/2026/llm-scrapers-references.json")
    ap.add_argument("collection", help="Zotero collection name, e.g. ai-scrape26")
    ap.add_argument("--zotero", default="http://127.0.0.1:23119/",
                    help="Zotero desktop's HTTP server: connector and local API")
    return ap.parse_args(argv[1:])


@dataclass(frozen=True)
class Existing:
    """What the library already has in the collection."""
    urls: frozenset[str]
    titles: frozenset[str]

    def has(self, entry: dict) -> bool:
        return entry.get("URL") in self.urls or entry["title"] in self.titles


# Zotero's CSL JSON import translator rejects a whole batch if any item's
# type is missing from its list, which predates CSL 1.0.2's "software".
DETECTABLE_TYPE = {"software": "document"}


def importable(entry: dict) -> dict:
    """An entry the CSL JSON translator will recognize, with finished notes only.

    >>> importable({"type": "software", "title": "Anubis"})
    {'type': 'document', 'title': 'Anubis'}
    """
    entry = publishable(entry)
    return {**entry, "type": DETECTABLE_TYPE.get(entry["type"], entry["type"])}


def tree_view_id(targets: list[dict], name: str) -> str:
    """Zotero's connector names save targets by tree view id: L1 for a library, C42 for a collection."""
    found = [t["id"] for t in targets if t["id"].startswith("C") and t["name"] == name]
    if len(found) != 1:
        raise LookupError(f"need exactly one collection named {name!r} in Zotero; found {len(found)}")
    return found[0]


def collection_key(collections: list[dict], name: str) -> str | None:
    keys = [c["key"] for c in collections if c["data"]["name"] == name]
    return keys[0] if keys else None


class WebPath:
    def __init__(self, base_url: str, urlopen):
        self.base_url = base_url
        self.__urlopen = urlopen

    def __truediv__(self, relative_url: str) -> "WebPath":
        return WebPath(urljoin(self.base_url, relative_url), self.__urlopen)

    def get_json(self):
        with self.__urlopen(self.base_url) as resp:
            return json.load(resp)

    def post(self, body: bytes, content_type: str):
        req = Request(self.base_url, data=body, method="POST",
                      headers={"Content-Type": content_type})
        with self.__urlopen(req) as resp:
            return resp.status, json.load(resp)


class LocalLibrary:
    """Zotero desktop's local API: the Web API, served from the local database,
    so it shows the library as it is now, no waiting for sync. It's off unless
    "Allow other applications on this computer to communicate with Zotero" is on.

    Not to be confused with the connector server (/connector/..., see Connector),
    though both listen on port 23119.

    https://www.zotero.org/support/dev/web_api/v3/local_api
    https://www.zotero.org/support/dev/client_coding/connector_http_server

    TODO: consider updating and deleting through the local API (e.g. to fix
    a source's fields in place, or merge duplicates) instead of deleting by
    hand and re-importing. Zotero 10+ supports POST/PUT/PATCH/DELETE there,
    with a local API key: see "Authorizing Writes" on the local API page.
    """

    def __init__(self, root: WebPath):
        self.__root = root

    def existing(self, name: str) -> Existing:
        key = collection_key((self.__root / "collections?limit=100").get_json(), name)
        if key is None:
            return Existing(frozenset(), frozenset())
        items = (self.__root / f"collections/{quote(key)}/items/top?limit=100").get_json()
        data = [i["data"] for i in items]
        return Existing(frozenset(d.get("url", "") for d in data) - {""},
                        # a case's title is its caseName; a statute's, its nameOfAct
                        frozenset(d.get("title") or d.get("caseName") or d.get("nameOfAct") or ""
                                  for d in data) - {""})


class Connector:
    """Zotero desktop's connector server: the same door the browser extension uses."""

    def __init__(self, root: WebPath):
        self.__root = root

    def target(self, name: str) -> str:
        _status, selected = (self / "getSelectedCollection").post(b"{}", "application/json")
        return tree_view_id(selected["targets"], name)

    def import_into(self, entries: list[dict], target: str, session: str) -> int:
        """Import lands in whatever is selected in the Zotero window;
        updating the session then files the items under target, as the connector popup does."""
        body = json.dumps(entries).encode("utf-8")
        # text/plain: Zotero's server would parse an application/json body
        # into an object, and the import translators need the text.
        try:
            _status, items = (self / f"import?{urlencode({'session': session})}").post(body, "text/plain")
        except HTTPError as e:
            # 400 with an empty body: no import translator recognized the data
            detail = e.read().decode("utf-8", errors="replace") or "no import translator recognized the data"
            raise RuntimeError(f"Zotero import failed: HTTP {e.code}: {detail}") from e
        update = {"sessionID": session, "target": target, "tags": []}
        (self / "updateSession").post(json.dumps(update).encode("utf-8"), "application/json")
        return len(items)

    def __truediv__(self, endpoint: str) -> WebPath:
        return self.__root / f"connector/{endpoint}"


def main(argv: list[str], cwd, urlopen, uuid4) -> int:
    args = cli(argv)
    entries = [importable(e) for e in json.loads((cwd / args.sources).read_text(encoding="utf-8"))]
    zotero = WebPath(args.zotero, urlopen)
    connector = Connector(zotero)
    library = LocalLibrary(zotero / "api/users/0/")

    target = connector.target(args.collection)
    existing = library.existing(args.collection)
    todo = [e for e in entries if not existing.has(e)]
    logging.info("%d sources; %d already in %s; importing %d",
                 len(entries), len(entries) - len(todo), args.collection, len(todo))
    if todo:
        n = connector.import_into(todo, target, uuid4().hex)
        logging.info("imported %d items into %s (%s)", n, args.collection, target)
    return 0


if __name__ == "__main__":
    def _script_io() -> int:
        from pathlib import Path
        from sys import argv
        from urllib.request import urlopen
        from uuid import uuid4

        logging.basicConfig(level=logging.INFO, format="%(message)s")
        return main(list(argv), Path.cwd(), urlopen, uuid4)

    raise SystemExit(_script_io())
