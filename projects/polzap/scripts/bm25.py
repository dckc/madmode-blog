#!/usr/bin/env python3
# SPDX-License-Identifier: CC0-1.0
"""BM25 political filter.

Builds two pseudo-documents from the LLM-judged labels — one from the
political messages, one from the clean — and classifies each message by
which pseudo-document it scores higher against under BM25.

BM25 is a bag-of-words ranking function: term frequency saturates (k1) and
scores are length-normalized (b), which suits short, repetitive SMS.

Usage:
  bm25.py msgs.json [--k1 1.5] [--b 0.75]
"""
import argparse
import json
import math
import re
from collections import Counter

TOK = re.compile(r"[a-zA-Z0-9']+")


def build_index(docs: list[str]) -> tuple[dict[str, int], dict[str, float], float]:
    """Return (df, idf, avgdl) over the given documents."""
    n = len(docs)
    df: Counter = Counter()
    lengths = []
    for d in docs:
        terms = set(TOK.findall(d))
        df.update(terms)
        lengths.append(len(TOK.findall(d)))
    avgdl = sum(lengths) / n if n else 0.0
    idf = {t: math.log(1 + (n - c + 0.5) / (c + 0.5)) for t, c in df.items()}
    return df, idf, avgdl


def bm25_score(query: str, df: dict[str, int], idf: dict[str, float], avgdl: float, k1: float, b: float) -> float:
    """Score a query string against the index's pseudo-document."""
    tf = Counter(TOK.findall(query))
    dl = sum(tf.values())
    score = 0.0
    for t, c in tf.items():
        if t not in idf:
            continue
        denom = c + k1 * (1 - b + b * dl / avgdl)
        score += idf[t] * c * (k1 + 1) / denom
    return score


def classify(msgs: list[dict], judged: dict[str, str], pol_idx, clean_idx, k1: float, b: float) -> dict:
    """Classify each labeled message by which pseudo-document scores higher."""
    tp = fp = tn = fn = 0
    for m in msgs:
        lab = judged.get(m["id"])
        if lab is None or lab == "borderline":
            continue
        s_pol = bm25_score(m["body"], *pol_idx, k1, b)
        s_clean = bm25_score(m["body"], *clean_idx, k1, b)
        pred = "political" if s_pol > s_clean else "clean"
        if lab == "political":
            if pred == "political":
                tp += 1
            else:
                fn += 1
        else:
            if pred == "political":
                fp += 1
            else:
                tn += 1
    return dict(tp=tp, fp=fp, tn=tn, fn=fn)


def report(result: dict, k1: float, b: float):
    tp, fp, tn, fn = result["tp"], result["fp"], result["tn"], result["fn"]
    prec = tp / (tp + fp) if tp + fp else float("nan")
    rec = tp / (tp + fn) if tp + fn else float("nan")
    f1 = 2 * prec * rec / (prec + rec) if prec + rec else float("nan")
    yield f"BM25 (k1={k1}, b={b})"
    yield f"TP={tp} FP={fp} TN={tn} FN={fn}"
    yield f"precision={prec:.3f} recall={rec:.3f} f1={f1:.3f}"


def main(argv, stdout, cwd) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("msgs", type=cwd.joinpath)
    ap.add_argument("--k1", type=float, default=1.5)
    ap.add_argument("--b", type=float, default=0.75)
    args = ap.parse_args(argv[1:])

    msgs = json.load(args.msgs.open(encoding="utf-8"))
    judged = json.load((cwd / "eval" / "msgs-judged.json").open(encoding="utf-8"))

    pol_docs = [m["body"] for m in msgs if judged.get(m["id"]) == "political"]
    clean_docs = [m["body"] for m in msgs if judged.get(m["id"]) == "clean"]
    pol_idx = build_index(pol_docs)
    clean_idx = build_index(clean_docs)

    result = classify(msgs, judged, pol_idx, clean_idx, args.k1, args.b)
    for line in report(result, args.k1, args.b):
        print(line, file=stdout)
    return 0


if __name__ == "__main__":
    def _script_io() -> int:
        from pathlib import Path
        from sys import argv, stdout
        return main(list(argv), stdout, Path.cwd())
    raise SystemExit(_script_io())
