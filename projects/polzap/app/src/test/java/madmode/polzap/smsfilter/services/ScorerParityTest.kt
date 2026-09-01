// SPDX-License-Identifier: CC0-1.0
package madmode.polzap.smsfilter.services

import org.junit.Assert.assertEquals
import org.junit.Assume.assumeTrue
import org.junit.Test
import java.io.File

/**
 * Runs the Kotlin scorer over the real sms-dump and checks it agrees with the
 * Python reference (scripts/scorer.py) predictions.
 *
 * Only runs when the SMS_DUMP env var is set to the dump path; the reference
 * predictions are expected next to it as <dump>.predictions.json. Both are
 * gitignored, so this is an explicit local/integration check, not part of the
 * default unit-test run.
 */
class ScorerParityTest {

    @Test
    fun `kotlin scorer matches python reference over the dump`() {
        val dumpPath = System.getenv("SMS_DUMP")
        assumeTrue("SMS_DUMP not set; skipping", dumpPath != null)
        val dump = File(dumpPath!!)
        assumeTrue("$dumpPath not found; skipping", dump.exists())
        val ref = File("$dumpPath.predictions.json")
        assumeTrue("$ref not found; skipping", ref.exists())

        val predictions = parseRef(ref.readText())
        val msgs = parseMessages(dump.readText())

        var mismatches = 0
        for (m in msgs) {
            val expected = predictions[m.id] ?: continue
            val actual = PoliticalScorer.isPolitical(m.body)
            if (expected != actual) {
                mismatches++
                if (mismatches <= 10) {
                    println("MISMATCH id=${m.id} expected=$expected actual=$actual body=${m.body.take(60)}")
                }
            }
        }
        assertEquals("scorer parity mismatches", 0, mismatches)
    }

    private data class Msg(val id: Int, val body: String)

    private fun parseMessages(text: String): List<Msg> {
        val parts = text.split(Regex(", date=\\d+\n"))
        val msgs = mutableListOf<Msg>()
        for (head in parts) {
            val m = Regex("Row: \\d+ _id=(\\d+), address=.*?, body=(.*)$", RegexOption.DOT_MATCHES_ALL)
                .find(head)
            if (m != null) {
                msgs.add(Msg(m.groupValues[1].toInt(), m.groupValues[2].trim()))
            }
        }
        return msgs
    }

    // Reference file is {"<id>": true|false, ...}; parse without a JSON lib.
    private fun parseRef(text: String): Map<Int, Boolean> {
        val out = mutableMapOf<Int, Boolean>()
        Regex("\"(\\d+)\"\\s*:\\s*(true|false)").findAll(text).forEach { m ->
            out[m.groupValues[1].toInt()] = m.groupValues[2] == "true"
        }
        return out
    }
}
