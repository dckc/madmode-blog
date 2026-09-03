#!/usr/bin/env python3
# SPDX-License-Identifier: CC0-1.0
"""Train a logistic-regression political filter with scikit-learn.

Features: TF-IDF word vectors over the message corpus. Labels: the current
scorer's predictions from the `scored` table in eval/msgs.db. Reports train
accuracy and prints the top political-signal words by learned weight.

Usage:
  linear.py msgs.json
"""
import json
import sqlite3
import sys

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


def main(argv, stdout, stderr, cwd) -> int:
    if len(argv) != 2:
        print(__doc__, file=stderr)
        return 2
    msgs = json.load((cwd / argv[1]).open(encoding="utf-8"))
    con = sqlite3.connect(cwd / "eval" / "msgs.db")
    scored = dict(con.execute("SELECT id, prediction FROM scored").fetchall())

    bodies = [m["body"] for m in msgs]
    y = [1.0 if scored.get(m["id"]) == "political" else 0.0 for m in msgs]

    vec = TfidfVectorizer(min_df=3, token_pattern=r"[a-z0-9']+")
    X = vec.fit_transform(bodies)

    clf = LogisticRegression(max_iter=1000)
    clf.fit(X, y)

    pred = clf.predict(X)
    acc = (pred == y).mean()

    print(f"trained on {len(msgs)} messages, {X.shape[1]} vocab terms", file=stdout)
    print(f"train accuracy: {acc:.3f}", file=stdout)
    print("\ntop political-signal words (highest weight):", file=stdout)
    names = vec.get_feature_names_out()
    order = clf.coef_[0].argsort()[::-1][:40]
    for i in order:
        if clf.coef_[0][i] != 0:
            print(f"  {names[i]:20s} w={clf.coef_[0][i]:+.3f}", file=stdout)
    return 0


if __name__ == "__main__":
    def _script_io() -> int:
        from pathlib import Path
        from sys import argv, stdout, stderr
        return main(list(argv), stdout, stderr, Path.cwd())
    raise SystemExit(_script_io())
