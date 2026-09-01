// SPDX-License-Identifier: CC0-1.0
package madmode.polzap.smsfilter.services

/**
 * Weighted political filter, ported from scripts/scorer.py.
 *
 * Scores a message body by summing the weights of every matching regex; a
 * message is political if the score meets a threshold. Keep in sync with
 * scripts/scorer.py (see ScorerParityTest).
 *
 * Rules are grouped by score, one row per theme. Case-insensitivity is inline
 * via (?i); the NOW rule is uppercase-only (spam urgency).
 */
object PoliticalScorer {

    private val RULES = listOf(
        // weight 3 — hard asks
        Regex("""(?i)\b(?:donate|donation)\b""") to 3,
        Regex("""(?i)\bcampaign\b""") to 3,
        // weight 2 — election mechanics, figures, institutions, links
        Regex("""(?i)\b(?:election|ballot|petition)\b""") to 2,
        Regex("""(?i)\b(?:Trump|Harris|Biden)\b""") to 2,
        Regex("""(?i)\b(?:PAC|MAGA|president|debate|senate|congress)\b""") to 2,
        // Pseudo-URLs like foo.org/blort or trumpmaga.vip/x (any TLD, requires "/").
        Regex("""(?i)\b[\w.-]+\.\w+/\S*\b""") to 2,
        // weight 1 — soft signals, urgency, structural markers
        Regex("""(?i)\b(?:vote|contribute|candidate|democrat|republican|government|deadline|signature)\b""") to 1,
        Regex("""\bNOW\b""") to 1,  // uppercase-only
        Regex("""(?i)(?:stop2end|end2end|text stop to quit|paid for by|reply stop to opt-out)""") to 1,
    )

    private const val THRESHOLD = 3

    fun score(body: String): Int =
        RULES.sumOf { (rx, w) -> if (rx.containsMatchIn(body)) w else 0 }

    fun isPolitical(body: String): Boolean = score(body) >= THRESHOLD
}
