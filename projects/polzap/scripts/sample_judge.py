#!/usr/bin/env python3
# SPDX-License-Identifier: CC0-1.0
"""Sample messages for LLM judging, stratified by the scorer's prediction.

Draws a balanced sample from the last N months: half from messages the scorer
flagged as political, half from messages it called clean. Writes one message
per line as JSON to stdout.

Usage:
  sample_judge.py msgs.json [--months 9] [--n 250] [--seed 1]
"""
import argparse
import json
import random
import sqlite3
import time


def main(argv, stdout, stderr, cwd, now_ms) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("msgs", type=cwd.joinpath)
    ap.add_argument("--months", type=int, default=9)
    ap.add_argument("--n", type=int, default=250)
    ap.add_argument("--seed", type=int, default=1)
    args = ap.parse_args(argv[1:])

    msgs = json.load(args.msgs.open(encoding="utf-8"))
    con = sqlite3.connect(cwd / "eval" / "msgs.db")
    scored = dict(con.execute("SELECT id, prediction FROM scored").fetchall())

    cutoff = now_ms - args.months * 30 * 86400_000
    recent = [m for m in msgs if m["date"] >= cutoff]

    political = [m for m in recent if scored.get(m["id"]) == "political"]
    clean = [m for m in recent if scored.get(m["id"]) == "clean"]

    rng = random.Random(args.seed)
    half = args.n // 2
    sample = rng.sample(political, min(half, len(political)))
    sample += rng.sample(clean, min(args.n - len(sample), len(clean)))

    for m in sample:
        stdout.write(json.dumps(m) + "\n")
    return 0


if __name__ == "__main__":
    def _script_io() -> int:
        import time
        from pathlib import Path
        from sys import argv, stdout, stderr
        return main(list(argv), stdout, stderr, Path.cwd(), int(time.time() * 1000))
    raise SystemExit(_script_io())
