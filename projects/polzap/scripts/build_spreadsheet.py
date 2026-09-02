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
import json
from datetime import datetime

from openpyxl import Workbook
from openpyxl.styles import Font


def evaluate(msgs: dict[int, dict], labels: dict[int, str], is_political):
    tp = fp = tn = fn = 0
    borderline = []
    review = []
    for mid, label in labels.items():
        pred = is_political(msgs[mid]["body"])
        if label == "borderline":
            borderline.append(msgs[mid])
            review.append((msgs[mid], "borderline"))
            continue
        if label == "political":
            if pred:
                tp += 1
            else:
                fn += 1
                review.append((msgs[mid], "false negative"))
        else:
            if pred:
                fp += 1
                review.append((msgs[mid], "false positive"))
            else:
                tn += 1

    precision = tp / (tp + fp) if (tp + fp) else float("nan")
    recall = tp / (tp + fn) if (tp + fn) else float("nan")
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else float("nan")

    return dict(
        tp=tp,
        fp=fp,
        tn=tn,
        fn=fn,
        precision=precision,
        recall=recall,
        f1=f1,
        borderline=borderline,
        review=review,
    )


def build_spreadsheet(
    msgs: dict[int, dict],
    labels: dict[int, str],
    is_political,
) -> tuple[Workbook, dict]:
    result = evaluate(msgs, labels, is_political)
    tp, fp, tn, fn = result["tp"], result["fp"], result["tn"], result["fn"]
    precision, recall, f1 = result["precision"], result["recall"], result["f1"]
    borderline = result["borderline"]
    review = result["review"]

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

    return wb, result


def main(argv, stdout, stderr, cwd, import_module) -> int:
    if len(argv) not in (4, 5):
        print(__doc__, file=stderr)
        return 2
    out = cwd / argv[3]
    filter_mod = argv[4] if len(argv) == 5 else "scorer"

    def load(path_name: str):
        return json.load((cwd / path_name).open(encoding="utf-8"))

    msgs = {int(m["id"]): m for m in load(argv[1])}
    labels = {int(k): v for k, v in load(argv[2]).items()}

    is_political = import_module(filter_mod).is_political

    wb, result = build_spreadsheet(msgs, labels, is_political)
    wb.save(out)

    print(
        f"wrote {out}: precision={result['precision']:.3f} "
        f"recall={result['recall']:.3f} f1={result['f1']:.3f}",
        file=stdout,
    )
    return 0


if __name__ == "__main__":
    def _script_io() -> int:
        import importlib
        from pathlib import Path
        from sys import argv, stdout, stderr

        return main(list(argv), stdout, stderr, Path.cwd(), importlib.import_module)

    raise SystemExit(_script_io())
