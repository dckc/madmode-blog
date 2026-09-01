#!/usr/bin/env python3
# SPDX-License-Identifier: CC0-1.0
"""Sample messages for manual labeling (recall estimation).

Usage:
  sample_unflagged.py msgs.json flagged_ids.json N [seed] > sample.txt

Prints N random messages NOT flagged by the filter, for human judgment.
"""
import json
import random
import sys

from scorer import is_political


def main() -> None:
    if len(sys.argv) not in (4, 5):
        print(__doc__, file=sys.stderr)
        sys.exit(2)
    msgs = json.load(open(sys.argv[1]))
    n = int(sys.argv[2])
    seed = int(sys.argv[3]) if len(sys.argv) == 5 else 1
    rng = random.Random(seed)
    unflagged = [m for m in msgs if not is_political(m["body"])]
    sample = rng.sample(unflagged, min(n, len(unflagged)))
    for m in sample:
        print(f"[{m['id']}] {m['address']} | {m['body'].replace(chr(10),' / ')}")


if __name__ == "__main__":
    main()
