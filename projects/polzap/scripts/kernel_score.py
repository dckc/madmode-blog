#!/usr/bin/env python3
# SPDX-License-Identifier: CC0-1.0
"""Score a message with the kernel classifier.

Usage:
  kernel_score.py BODY
"""
import json
import re
import sys

TOK = re.compile(r"[a-zA-Z0-9']+")


def score(body: str, kernel: dict) -> tuple[float, list[tuple[str, float]]]:
    terms = kernel["terms"]
    total = kernel["intercept"]
    hits = []
    for w in TOK.findall(body):
        for tok in (w, w.lower()):
            if tok in terms:
                total += terms[tok]
                hits.append((tok, terms[tok]))
    return total, hits


def main(argv, stdout, stderr, cwd) -> int:
    if len(argv) != 2:
        print("Usage: kernel_score.py BODY", file=stderr)
        return 2
    body = argv[1]
    kernel = json.load((cwd / "eval" / "kernel.json").open(encoding="utf-8"))
    total, hits = score(body, kernel)
    print(f"score: {total:.3f}  political: {total > 0}", file=stdout)
    for tok, w in hits:
        print(f"  {tok:20s} {w:+.3f}", file=stdout)
    return 0


if __name__ == "__main__":
    def _script_io() -> int:
        from pathlib import Path
        from sys import argv, stdout, stderr
        return main(list(argv), stdout, stderr, Path.cwd())
    raise SystemExit(_script_io())
