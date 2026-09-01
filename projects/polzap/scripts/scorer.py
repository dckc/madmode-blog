#!/usr/bin/env python3
# SPDX-License-Identifier: CC0-1.0
"""Weighted political filter (prototype).

Scores a message body by summing the weights of every matching regex; a
message is political if the score meets a threshold. Mirrors
PoliticalScorer.kt in the app; keep the two in sync (see ScorerParityTest).

Rules are grouped by score, one row per theme. Case-insensitivity is inline
via (?i); the NOW rule is uppercase-only (spam urgency).
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
