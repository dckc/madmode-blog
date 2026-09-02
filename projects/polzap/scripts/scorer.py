#!/usr/bin/env python3
# SPDX-License-Identifier: CC0-1.0
"""Weighted political filter.

Scores a message body by summing the weights of every matching regex; a
message is political if the score meets a threshold. Mirrors
PoliticalScorer.kt in the app; keep the two in sync (see ScorerParityTest).

Rules are grouped by score, one row per theme. Case-insensitivity is inline
via (?i); the NOW rule is uppercase-only (spam urgency).

CLI: ``scorer.py BODY`` prints is_political, score, and a match vector.
"""
import re


# (pattern, weight). Compiled below.
_RULES = [
    # weight 3 — hard asks
    (r"(?i)\b(?:donate|donation)\b", 3),
    (r"(?i)\bcampaign\b", 3),
    # weight 2 — election mechanics, figures, institutions, links
    (r"(?i)\b(?:election|ballot|petition)\b", 2),
    (r"(?i)\b(?:Trump|Harris|Biden)\b", 2),
    (r"(?i)\b(?:PAC|MAGA|president|debate|senate|congress)\b", 2),
    # Pseudo-URLs like foo.org/blort or trumpmaga.vip/x (any TLD, requires "/").
    (r"(?i)\b[\w.-]+\.\w+/\S*\b", 2),
    # weight 1 — soft signals, urgency, structural markers
    (r"(?i)\b(?:vote|contribute|candidate|democrat|republican|government|deadline|signature)\b", 1),
    (r"\bNOW\b", 1),  # uppercase-only
    (r"(?i)(?:stop2end|end2end|text stop to quit|paid for by|reply stop to opt-out)", 1),
]

RULES = [(re.compile(p), w) for p, w in _RULES]

THRESHOLD = 3


def score(body: str) -> int:
    return sum(w for rx, w in RULES if rx.search(body))


def is_political(body: str) -> bool:
    return score(body) >= THRESHOLD


def score_with_matches(body: str) -> tuple[int, list[tuple[str, int]]]:
    matches = [(m.group(0), w) for rx, w in RULES if (m := rx.search(body))]
    return sum(w for _, w in matches), matches


def main(argv, stdout) -> int:
    if len(argv) != 2:
        print("Usage: scorer.py BODY", file=stdout)
        return 2
    body = argv[1]
    s, matches = score_with_matches(body)
    print(f"is_political: {is_political(body)}", file=stdout)
    print(f"score: {s}", file=stdout)
    print(f"vector: {', '.join(f'{t}={w}' for t, w in matches)}", file=stdout)
    return 0


if __name__ == "__main__":
    def _script_io() -> int:
        from sys import argv, stdout

        return main(list(argv), stdout)

    raise SystemExit(_script_io())
