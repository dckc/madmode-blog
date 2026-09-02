#!/usr/bin/env python3
# SPDX-License-Identifier: CC0-1.0
"""Sample messages for manual labeling (recall estimation).

Usage:
  sample_unflagged.py msgs.json flagged_ids.json N [seed] > sample.txt

Prints N random messages NOT flagged by the filter, for human judgment.
"""
import json
import random

from scorer import is_political


def sample_unflagged(msgs: list[dict], n: int, rng: random.Random) -> list[dict]:
    unflagged = [m for m in msgs if not is_political(m["body"])]
    return rng.sample(unflagged, min(n, len(unflagged)))


def render_sample(m: dict) -> str:
    return f"[{m['id']}] {m['address']} | {m['body'].replace(chr(10), ' / ')}"


def main(argv, stdout, stderr, cwd) -> int:
    if len(argv) not in (4, 5):
        print(__doc__, file=stderr)
        return 2
    msgs = json.load((cwd / argv[1]).open(encoding="utf-8"))
    n = int(argv[2])
    seed = int(argv[3]) if len(argv) == 5 else 1
    rng = random.Random(seed)
    sample = sample_unflagged(msgs, n, rng)
    for m in sample:
        print(render_sample(m), file=stdout)
    return 0


if __name__ == "__main__":
    def _script_io() -> int:
        from pathlib import Path
        from sys import argv, stdout, stderr

        return main(list(argv), stdout, stderr, Path.cwd())

    raise SystemExit(_script_io())
