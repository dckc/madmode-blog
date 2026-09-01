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
import sys

from scorer import is_political


def main() -> None:
    if len(sys.argv) != 3:
        print(__doc__, file=sys.stderr)
        sys.exit(2)
    msgs = {int(m["id"]): m for m in json.load(open(sys.argv[1]))}
    labels = {int(k): v for k, v in json.load(open(sys.argv[2])).items()}

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

    print(f"labeled: {len(labels)}  (borderline: {len(borderline)})")
    print(f"TP={tp} FP={fp} TN={tn} FN={fn}")
    print(f"precision={precision:.3f} recall={recall:.3f} f1={f1:.3f}")


if __name__ == "__main__":
    main()
