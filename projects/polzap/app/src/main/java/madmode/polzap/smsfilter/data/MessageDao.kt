// Room DAO for the indexed political message table.
// SPDX-License-Identifier: CC0-1.0
package madmode.polzap.smsfilter.data

import androidx.room.Dao
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query

@Dao
interface MessageDao {
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertMessage(message: PoliticalMessageEntity): Long

    @Query("SELECT * FROM indexed_political_messages ORDER BY intercept_timestamp DESC")
    suspend fun getAllIndexedMessages(): List<PoliticalMessageEntity>

    @Query("DELETE FROM indexed_political_messages WHERE id = :messageId")
    suspend fun deleteMessageById(messageId: Long)
}
