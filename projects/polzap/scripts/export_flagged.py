#!/usr/bin/env python3
# SPDX-License-Identifier: CC0-1.0
"""Export flagged political texts since a date as CSV, for complaints and letters."""
import argparse
import csv
import json
import logging
import re
from collections.abc import Callable, Iterable
from dataclasses import asdict, dataclass, fields
from datetime import datetime, timedelta, timezone

from scorer import is_political


def cli(path) -> argparse.ArgumentParser:
    """path: designation -> path, e.g. cwd.joinpath"""
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    ap.add_argument("msgs", type=path, help="parsed SMS dump, e.g. eval/msgs.json")
    ap.add_argument("db", type=path, help="polzap's index, e.g. device/polzap_index.db")
    ap.add_argument("--since", default="2026-08-01", help="first day, YYYY-MM-DD")
    ap.add_argument("--app-start", default="2026-09-01",
                    help="first day to take from the index instead of the dump")
    ap.add_argument("--until", default="9999-12-31", help="day after the last one")
    return ap


@dataclass(frozen=True)
class FlaggedText:
    """One flagged political text; also the output: one CSV row each, these
    fields as columns in this order."""
    date: str
    source: str
    sender: str
    domains: str
    signer: str
    body: str

    @classmethod
    def of(cls, when: datetime, source: str, sender: str | None, body: str) -> "FlaggedText":
        sig = SIGNER_RE.search(body)
        return cls(
            date=when.strftime("%Y-%m-%dT%H:%M"),
            source=source,
            sender=norm_sender(sender),
            domains=" ".join(sorted(set(DOMAIN_RE.findall(body.lower())))),
            signer=sig.group(1) if sig else "",
            body=body,
        )

    @classmethod
    def from_dump(cls, msgs: list[dict], since: str, until: str,
                  local: Callable[[int], datetime]) -> list["FlaggedText"]:
        """Messages from parse_sms.py that scorer.py flags, since <= day < until.

        local: epoch millis -> local time
        """
        return [
            cls.of(when, "sms-dump", m.get("address"), m["body"])
            for m in msgs
            if since <= day(when := local(m["date"])) < until and is_political(m["body"])
        ]

    @classmethod
    def from_index(cls, records: Iterable[tuple[int, str, str]], since: str, until: str,
                   local: Callable[[int], datetime]) -> list["FlaggedText"]:
        """(timestamp, sender, body) records from polzap's index, since <= day < until.

        local: epoch millis -> local time
        """
        return [
            cls.of(when, "polzap-index", sender, body)
            for ts, sender, body in records
            if since <= day(when := local(ts)) < until
        ]


DOMAIN_RE = re.compile(r"(?:https?://)?((?:[a-z0-9-]+\.)+[a-z]{2,})(?:/|\b)")
SIGNER_RE = re.compile(r"\b(?:[Ii]t'?s|[Tt]his is) ([A-Z][a-z]+ [A-Z][a-z]+)")


def day(when: datetime) -> str:
    return when.strftime("%Y-%m-%d")


def local_time(localtime) -> Callable[[int], datetime]:
    """Attenuate time.localtime to: epoch millis -> aware local datetime."""
    def at(ms: int) -> datetime:
        t = localtime(ms // 1000)
        return datetime(*t[:6], tzinfo=timezone(timedelta(seconds=t.tm_gmtoff), t.tm_zone))
    return at


def norm_sender(s: str | None) -> str:
    """10-digit US number when it looks like one; otherwise as given."""
    if not s:
        return ""
    digits = re.sub(r"\D", "", s)
    return digits[-10:] if len(digits) >= 10 else s


def index_records(con):
    """(timestamp, sender, body) for each message in polzap's index."""
    return con.execute(
        "SELECT intercept_timestamp, sender_identity, message_payload"
        " FROM indexed_political_messages ORDER BY intercept_timestamp")


def main(argv, cwd, stdout, connect, localtime) -> int:
    args = cli(cwd.joinpath).parse_args(argv[1:])
    msgs = json.load(args.msgs.open(encoding="utf-8"))
    index = connect(args.db)
    # some payloads hold invalid UTF-8; keep them, marked with U+FFFD
    index.text_factory = lambda b: b.decode("utf-8", "replace")
    local = local_time(localtime)

    # polzap's index began on app_start; the SMS dump covers the days before
    texts = FlaggedText.from_dump(msgs, args.since, min(args.app_start, args.until), local)
    texts += FlaggedText.from_index(index_records(index),
                                    max(args.since, args.app_start), args.until, local)
    texts.sort(key=lambda t: t.date)
    out = csv.DictWriter(stdout, fieldnames=[f.name for f in fields(FlaggedText)])
    out.writeheader()
    out.writerows(asdict(t) for t in texts)
    logging.info("%d flagged messages", len(texts))
    return 0


if __name__ == "__main__":
    def _script_io() -> int:
        import sqlite3
        import sys
        import time
        from pathlib import Path

        logging.basicConfig(stream=sys.stderr, level=logging.INFO, format="%(message)s")
        return main(
            argv=list(sys.argv),
            cwd=Path.cwd(),
            stdout=sys.stdout,
            connect=sqlite3.connect,
            localtime=time.localtime,
        )
    raise SystemExit(_script_io())
