#!/usr/bin/env python3
# SPDX-License-Identifier: CC0-1.0
"""Build the evaluation spreadsheet (3 sheets) from labels.

Usage:
  build_spreadsheet.py msgs.json labels.json out.xlsx [filter_module]

filter_module names a module in scripts/ exposing is_political(body) -> bool;
defaults to "scorer" (the weighted design, ported to the app).

Sheets:
  - "summary": precision/recall + descriptive stats
  - "borderline": messages flagged as borderline
  - "raw": every labeled message with id, address, date, body, label, prediction
"""
import importlib
import json
import sys
from datetime import datetime

from openpyxl import Workbook
from openpyxl.styles import Font


def main() -> None:
    if len(sys.argv) not in (4, 5):
        print(__doc__, file=sys.stderr)
        sys.exit(2)
    msgs = {int(m["id"]): m for m in json.load(open(sys.argv[1]))}
    labels = {int(k): v for k, v in json.load(open(sys.argv[2])).items()}
    out = sys.argv[3]
    filter_mod = importlib.import_module(sys.argv[4] if len(sys.argv) == 5 else "scorer")
    is_political = filter_mod.is_political

    # Confusion counts over labeled messages (borderline excluded from metrics).
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
        else:
            if pred:
                fp += 1
            else:
                tn += 1

    # The interesting cases for a human to review: false positives, false
    # negatives, and anything explicitly flagged borderline.
    review = []
    for mid, label in labels.items():
        pred = is_political(msgs[mid]["body"])
        if label == "borderline":
            review.append((msgs[mid], "borderline"))
        elif label == "political" and not pred:
            review.append((msgs[mid], "false negative"))
        elif label == "clean" and pred:
            review.append((msgs[mid], "false positive"))

    precision = tp / (tp + fp) if (tp + fp) else float("nan")
    recall = tp / (tp + fn) if (tp + fn) else float("nan")
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else float("nan")

    wb = Workbook()

    # --- summary sheet ---
    ws = wb.active
    ws.title = "summary"
    ws.append(["polzap filter evaluation"])
    ws.append([])
    ws.append(["metric", "value"])
    ws.append(["labeled messages", len(labels)])
    ws.append(["true positives (TP)", tp])
    ws.append(["false positives (FP)", fp])
    ws.append(["true negatives (TN)", tn])
    ws.append(["false negatives (FN)", fn])
    ws.append(["precision (TP/(TP+FP))", round(precision, 4)])
    ws.append(["recall (TP/(TP+FN))", round(recall, 4)])
    ws.append(["F1", round(f1, 4)])
    ws.append([])
    ws.append(["descriptive stats"])
    ws.append(["total messages in dump", len(msgs)])
    ws.append(["flagged by filter", tp + fp])
    ws.append(["borderline (excluded)", len(borderline)])
    dates = sorted(m["date"] for m in msgs.values())
    ws.append(["earliest message", datetime.fromtimestamp(dates[0] / 1000).isoformat()])
    ws.append(["latest message", datetime.fromtimestamp(dates[-1] / 1000).isoformat()])
    ws.append(["date span (days)", round((dates[-1] - dates[0]) / 86400000, 1)])
    ws.append(["distinct senders", len({m["address"] for m in msgs.values()})])
    for c in ws[1]:
        c.font = Font(bold=True)

    # --- borderline sheet ---
    ws2 = wb.create_sheet("borderline")
    ws2.append(["id", "address", "date", "kind", "body"])
    for m, kind in sorted(review, key=lambda x: x[0]["id"]):
        ws2.append([
            m["id"], m["address"],
            datetime.fromtimestamp(m["date"] / 1000).isoformat(),
            kind,
            m["body"],
        ])

    # --- raw sheet ---
    ws3 = wb.create_sheet("raw")
    ws3.append(["id", "kind", "address", "date", "label", "prediction", "body"])
    for m in sorted(msgs.values(), key=lambda m: m["date"], reverse=True):
        label = labels.get(m["id"], "")
        ws3.append([
            m["id"], m.get("kind", "sms"), m.get("address", ""),
            datetime.fromtimestamp(m["date"] / 1000).isoformat(),
            label,
            "political" if is_political(m["body"]) else "clean",
            m["body"],
        ])

    wb.save(out)
    print(f"wrote {out}: precision={precision:.3f} recall={recall:.3f} f1={f1:.3f}")


if __name__ == "__main__":
    main()
