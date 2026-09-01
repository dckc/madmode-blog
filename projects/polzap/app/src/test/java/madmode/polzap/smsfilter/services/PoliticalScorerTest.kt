// SPDX-License-Identifier: CC0-1.0
package madmode.polzap.smsfilter.services

import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

class PoliticalScorerTest {

    @Test
    fun `donation plus debate plus url plus stop marker is political`() {
        val body = "URGENT: Before Tim steps off the stage at the Vice-Presidential Debate...\n" +
            "900% MATCH your Dem House donation! hmpac.org/142?t=jDQDK9\n" +
            "-HMP\n" +
            "Text STOP to quit"
        assertTrue(PoliticalScorer.isPolitical(body))
    }
}
