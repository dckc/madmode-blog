#!/usr/bin/env python3
# SPDX-License-Identifier: CC0-1.0
"""Parse sms-dump.txt (adb content query output) into JSON messages.

Format: each record is `Row: N _id=<id>, address=<addr>, body=<body>, date=<ms>`
where <body> may span multiple lines (embedded newlines). The record boundary
is the `, date=<ms>` terminator, NOT the `Row:` prefix (bodies can contain
lines that look like `Row: ...`).

Usage: parse_sms.py sms-dump.txt > msgs.json
"""
import json
import re
import sys

DATE_RE = re.compile(r", date=(\d+)\n")
HEAD_RE = re.compile(r"Row: \d+ _id=(\d+), address=(.*?), body=(.*)$", re.S)


def parse(text: str) -> list[dict]:
    parts = DATE_RE.split(text)
    msgs = []
    for i in range(0, len(parts) - 1, 2):
        head, date = parts[i], parts[i + 1]
        m = HEAD_RE.match(head)
        if m:
            msgs.append({
                "id": int(m.group(1)),
                "address": m.group(2),
                "body": m.group(3).strip(),
                "date": int(date),
            })
    return msgs


def main() -> None:
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        sys.exit(2)
    text = open(sys.argv[1]).read()
    json.dump(parse(text), sys.stdout, indent=2)


if __name__ == "__main__":
    main()
