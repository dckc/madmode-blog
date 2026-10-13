# Kernel Notes

Summary of the text-classification techniques explored for the polzap
political-SMS filter, in rough order of sophistication.

## 1. Hand-written weighted regex scorer

The baseline. `PoliticalScorer.kt` (app) and `scripts/scorer.py` (eval) hold a
list of `(regex, weight)` rules; a message is political if the summed weight of
matching rules meets a threshold (3). Transparent, debuggable, runs on-device in
milliseconds, zero training data.

Weaknesses discovered:
- **Plural/tense bugs** — the rule `\bsignature\b` missed "signatures", which
  let a real spam text through ("I'm sad you didn't sign...").
- **Thin vocabulary** — only knew Trump/Harris/Biden; missed Warnock, Walker,
  McConnell, Obama, Warren, Walz, GOP, Dems, etc.
- **Hand-picked weights** — no data behind them.

## 2. TF-IDF table

Pure corpus statistics, no labels. `tfidf` table in `eval/msgs.db`: for each
term, its document frequency and `idf = log((N+1)/(df+1)) + 1`. Rare terms get
high idf. Useful for spotting discriminative vocabulary (e.g. `signatures`
appears 33× vs `signature` 12× — the plural is the *more* common form).

## 3. TF-IDF + logistic regression

`scripts/linear.py`. Represent each message as a TF-IDF word vector, train a
logistic regression. The model learns weights from data instead of hand-picking
them. Trained on the scorer's own predictions it's circular, but it still
generalizes beyond the exact rules via correlated terms.

## 4. Dual tokenization (case as a signal)

Emit each word as both its original form and its lowercase form, so the model
can learn that SHOUTING (NOW, URGENT) is a stronger signal than lowercase.
Improved the model's ability to catch spam.

## 5. Model-vs-scorer disagreement analysis

`scripts/compare.py`. Trains a logistic model on the scorer's output, then
reports where they disagree. The model surfaced real false negatives the
hand-written rules missed (candidate names, party terms, issue advocacy) — the
error-analysis signal that drives rule fixes.

## 6. LLM-as-judge

Best practice for building ground truth on a corpus like this:
- **Stratified sampling**, not random — sample separately from predicted-
  political and predicted-clean so both precision and recall are measurable.
- **Fixed seed + frozen sample** for reproducibility.
- **Clear rubric** with political/clean/borderline and examples.
- **Judge each message independently** to avoid context bleed.

`scripts/sample_judge.py` draws a balanced 250-message sample from the last 9
months; the LLM judged all 250 into `eval/msgs-judged.json`. The scorer scored
precision 0.967 / recall 1.000 / F1 0.983 against it. Notably, the LLM's 4
"false positives" were actually issue/charity advocacy the scorer correctly
flagged — the LLM's rubric was too candidate-focused.

## 7. Compact kernel

`scripts/kernel.py` + `scripts/kernel_score.py`. Train a logistic regression on
the LLM-judged labels with dual tokenization, prune to the top-K terms by
|weight|, and emit a ~1.5KB `(term, weight)` table + intercept. This is the
"statistically derived kernel" — small enough to hard-code in Kotlin, and it
catches the message the hand-written scorer missed (the `sign` term handles the
plural bug).

## Takeaway

The progression is: hand-written rules → TF-IDF features → learned linear model →
compact pruned kernel. The kernel gives most of the benefit of the learned model
in a form small enough to ship on-device, and it's grounded in real (LLM-judged)
labels rather than hand-picked rules.
