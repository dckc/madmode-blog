#!/usr/bin/env python3
# SPDX-License-Identifier: CC0-1.0
"""Evaluate the political filter against a labeled message set.

Usage:
  evaluate.py msgs.json labels.json

Reads parsed messages (from parse_sms.py) and a labels file mapping message id
to a label, then reports precision/recall and writes the raw + borderline sheets.

Labels: "political" (spam to suppress) or "clean" (keep). Borderline cases get
label "borderline".
"""
import json

from scorer import is_political


def evaluate(msgs: dict[int, dict], labels: dict[int, str]) -> dict:
    tp = fp = tn = fn = 0
    borderline = []
    for mid, label in labels.items():
        pred = is_political(msgs[mid]["body"])
        if label == "borderline":
            borderline.append(msgs[mid])
            continue
        if label == "political":
            if pred:
                tp += 1
            else:
                fn += 1
        else:  # clean
            if pred:
                fp += 1
            else:
                tn += 1

    precision = tp / (tp + fp) if (tp + fp) else float("nan")
    recall = tp / (tp + fn) if (tp + fn) else float("nan")
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else float("nan")

    return {
        "labeled": len(labels),
        "borderline": len(borderline),
        "tp": tp,
        "fp": fp,
        "tn": tn,
        "fn": fn,
        "precision": precision,
        "recall": recall,
        "f1": f1,
    }


def report(result: dict, stdout) -> None:
    print(f"labeled: {result['labeled']}  (borderline: {result['borderline']})", file=stdout)
    print(f"TP={result['tp']} FP={result['fp']} TN={result['tn']} FN={result['fn']}", file=stdout)
    print(f"precision={result['precision']:.3f} recall={result['recall']:.3f} f1={result['f1']:.3f}", file=stdout)


def main(argv, stdout, stderr, cwd) -> int:
    if len(argv) != 3:
        print(__doc__, file=stderr)
        return 2
    msgs = {int(m["id"]): m for m in json.load((cwd / argv[1]).open(encoding="utf-8"))}
    labels = {int(k): v for k, v in json.load((cwd / argv[2]).open(encoding="utf-8")).items()}

    result = evaluate(msgs, labels)
    report(result, stdout)
    return 0


if __name__ == "__main__":
    def _script_io() -> int:
        from pathlib import Path
        from sys import argv, stdout, stderr

        return main(list(argv), stdout, stderr, Path.cwd())

    raise SystemExit(_script_io())
