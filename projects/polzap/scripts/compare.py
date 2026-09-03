#!/usr/bin/env python3
# SPDX-License-Identifier: CC0-1.0
"""Compare the logistic model against the scorer: find disagreements.

Trains a logistic regression on the scorer's predictions, then reports
messages where the model and scorer disagree — the model's "new" calls.

Usage:
  compare.py msgs.json
"""
import json
import re
import sqlite3
import sys

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

TOK = re.compile(r"[a-zA-Z0-9']+")


def dual_tokens(body: str) -> list[str]:
    """Emit each word as both its original form and its lowercase form.

    Lets the model learn that uppercase (NOW, URGENT) is a stronger signal
    than lowercase (now, urgent).
    """
    out = []
    for w in TOK.findall(body or ""):
        out.append(w)
        lw = w.lower()
        if lw != w:
            out.append(lw)
    return out


def main(argv, stdout, stderr, cwd) -> int:
    if len(argv) != 2:
        print(__doc__, file=stderr)
        return 2
    msgs = json.load((cwd / argv[1]).open(encoding="utf-8"))
    con = sqlite3.connect(cwd / "eval" / "msgs.db")
    scored = dict(con.execute("SELECT id, prediction FROM scored").fetchall())

    bodies = [m["body"] for m in msgs]
    y = [1.0 if scored.get(m["id"]) == "political" else 0.0 for m in msgs]

    vec = TfidfVectorizer(min_df=3, tokenizer=dual_tokens, token_pattern=None)
    X = vec.fit_transform(bodies)
    clf = LogisticRegression(max_iter=1000)
    clf.fit(X, y)
    pred = clf.predict(X)

    new_political = 0
    new_clean = 0
    for m, p, yi in zip(msgs, pred, y):
        if p == 1 and yi == 0:
            new_political += 1
        elif p == 0 and yi == 1:
            new_clean += 1

    print(f"model flags {int(pred.sum())} total", file=stdout)
    print(f"  new political (scorer said clean): {new_political}", file=stdout)
    print(f"  new clean (scorer said political): {new_clean}", file=stdout)
    print("\nsample of model-flagged-but-scorer-clean messages:", file=stdout)
    shown = 0
    for m, p, yi in zip(msgs, pred, y):
        if p == 1 and yi == 0:
            print(f"  [{m['id']}] {m['body'][:120]}", file=stdout)
            shown += 1
            if shown >= 15:
                break
    return 0


if __name__ == "__main__":
    def _script_io() -> int:
        from pathlib import Path
        from sys import argv, stdout, stderr
        return main(list(argv), stdout, stderr, Path.cwd())
    raise SystemExit(_script_io())
