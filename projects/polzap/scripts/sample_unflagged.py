#!/usr/bin/env python3
# SPDX-License-Identifier: CC0-1.0
"""Sample messages for manual labeling (recall estimation).

Usage:
  sample_unflagged.py msgs.json N [seed] [--months M] > sample.txt

Prints N random messages NOT flagged by the filter, for human judgment.
Only messages from the last M months (default 6) are eligible.
"""
import argparse
import json
import random

from scorer import is_political


def sample_unflagged(msgs: list[dict], n: int, rng: random.Random, cutoff_ms: int) -> list[dict]:
    recent = [m for m in msgs if m["date"] >= cutoff_ms]
    unflagged = [m for m in recent if not is_political(m["body"])]
    return rng.sample(unflagged, min(n, len(unflagged)))


def render_sample(m: dict) -> str:
    return f"[{m['id']}] {m['address']} | {m['body'].replace(chr(10), ' / ')}"


def main(argv, stdout, stderr, cwd, now_ms) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("msgs", type=cwd.joinpath)
    ap.add_argument("n", type=int)
    ap.add_argument("seed", type=int, nargs="?", default=1)
    ap.add_argument("--months", type=int, default=6)
    args = ap.parse_args(argv[1:])

    msgs = json.load(args.msgs.open(encoding="utf-8"))
    cutoff_ms = now_ms - args.months * 30 * 86400_000
    rng = random.Random(args.seed)
    sample = sample_unflagged(msgs, args.n, rng, cutoff_ms)
    for m in sample:
        print(render_sample(m), file=stdout)
    return 0


if __name__ == "__main__":
    def _script_io() -> int:
        import time
        from pathlib import Path
        from sys import argv, stdout, stderr

        return main(list(argv), stdout, stderr, Path.cwd(), int(time.time() * 1000))

    raise SystemExit(_script_io())
