#!/usr/bin/env python3
# SPDX-License-Identifier: CC0-1.0
"""Train a compact logistic-regression "kernel" classifier.

Trains on the LLM-judged labels (eval/msgs-judged.json), using dual
tokenization (each word as itself + its lowercase form, so case is a signal).
Prunes to the top-K terms by |weight| and emits a compact (term, weight) table
suitable for hard-coding.

Usage:
  kernel.py msgs.json [--k 50] [--out kernel.json]
"""
import argparse
import json
import re
import sqlite3

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

TOK = re.compile(r"[a-zA-Z0-9']+")


def dual_tokens(body: str) -> list[str]:
    out = []
    for w in TOK.findall(body or ""):
        out.append(w)
        lw = w.lower()
        if lw != w:
            out.append(lw)
    return out


def load_training_data(msgs: list[dict], judged: dict[str, str]) -> tuple[list[str], list[float]]:
    bodies, y = [], []
    for m in msgs:
        lab = judged.get(m["id"])
        if lab is None or lab == "borderline":
            continue
        bodies.append(m["body"])
        y.append(1.0 if lab == "political" else 0.0)
    return bodies, y


def train(bodies: list[str], y: list[float]) -> tuple[TfidfVectorizer, LogisticRegression]:
    vec = TfidfVectorizer(min_df=2, tokenizer=dual_tokens, token_pattern=None)
    X = vec.fit_transform(bodies)
    clf = LogisticRegression(max_iter=1000)
    clf.fit(X, y)
    return vec, clf


def prune(vec: TfidfVectorizer, clf: LogisticRegression, k: int) -> dict:
    names = vec.get_feature_names_out()
    w = clf.coef_[0]
    order = abs(w).argsort()[::-1][:k]
    return {
        "intercept": float(clf.intercept_[0]),
        "terms": {names[i]: float(w[i]) for i in order},
    }


def main(argv, stdout, stderr, cwd) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("msgs", type=cwd.joinpath)
    ap.add_argument("--k", type=int, default=50)
    ap.add_argument("--out", type=cwd.joinpath, default=cwd / "eval" / "kernel.json")
    args = ap.parse_args(argv[1:])

    msgs = json.load(args.msgs.open(encoding="utf-8"))
    judged = json.load((cwd / "eval" / "msgs-judged.json").open(encoding="utf-8"))

    bodies, y = load_training_data(msgs, judged)
    vec, clf = train(bodies, y)
    kernel = prune(vec, clf, args.k)

    args.out.write_text(json.dumps(kernel, indent=2) + "\n", encoding="utf-8")

    print(f"trained on {len(bodies)} labeled messages, {len(vec.get_feature_names_out())} vocab", file=stdout)
    print(f"kernel: {len(kernel['terms'])} terms, {len(json.dumps(kernel))} bytes", file=stdout)
    print(f"wrote {args.out}", file=stdout)
    return 0


if __name__ == "__main__":
    def _script_io() -> int:
        from pathlib import Path
        from sys import argv, stdout, stderr
        return main(list(argv), stdout, stderr, Path.cwd())
    raise SystemExit(_script_io())
