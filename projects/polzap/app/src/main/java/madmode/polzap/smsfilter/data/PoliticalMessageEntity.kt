// Room entity: one row per intercepted political message.
// SPDX-License-Identifier: CC0-1.0
package madmode.polzap.smsfilter.data

import androidx.room.ColumnInfo
import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "indexed_political_messages")
data class PoliticalMessageEntity(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    @ColumnInfo(name = "sender_identity") val sender: String,
    @ColumnInfo(name = "message_payload") val messageBody: String,
    @ColumnInfo(name = "intercept_timestamp") val timestamp: Long
)
