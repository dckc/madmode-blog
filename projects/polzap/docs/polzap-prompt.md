# Product Requirements Document (PRD) & Technical Specification
## Project Name: Project Agora (Automated Political SMS Indexer & Filter)

> Historical artifact: the original spec that spawned this code, kept for
> reference. The implementation has since diverged (package is now
> `madmode.polzap`, not `com.example.agora`).

---

## 1. Executive Summary
Project Agora is an internal, non-published Android utility designed to intercept, analyze, and index political SMS/RCS messages in real-time without replacing the default system SMS application ([Google Messages](https://play.google.com/store/apps/details?id=com.google.android.apps.messaging "Google Messages on Play Store")). By leveraging Android's `NotificationListenerService`, the application silently captures message payloads directly from status bar alerts, programmatically dismisses matching political notifications via `cancelNotification()`, and logs structured data into a local relational database for indexing.

---

## 2. Architecture & System Topology
The application utilizes an event-driven, decoupled background architecture optimized for minimal battery drain and immediate execution context.

### 2.1 Component Interaction Diagram
1. **Telephony/RCS Layer:** Carrier routes incoming texts to the default handler (`com.google.android.apps.messaging`).
2. **System Status Bar:** The default handler fires a standard UI notification alert.
3. **Notification Interceptor Core:** The custom `SMSNotificationListener` catches the alert immediately via a system-level binder transaction.
4. **Heuristics Engine:** A regex and NLP rule layer evaluates the string contents.
5. **Action Handlers:**
   * **If Political:** Fires a database pipeline worker to persist data, then invokes the IPC `cancelNotification()` method to vaporize the UI element.
   * **If Clean:** No-op. The event loop terminates, letting the user interact with the text naturally.

---

## 3. Technical Specifications & Concrete Manifests

### 3.1 Android Manifest Declaration (`AndroidManifest.xml`)
The application requires explicit registration of the sensitive service binder alongside standard background persistence features.

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.agora.smsfilter">

    <!-- Permissions required for background lifecycle execution -->
    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
    <uses-permission android:name="android.permission.FOREGROUND_SERVICE" />

    <application
        android:allowBackup="false"
        android:icon="@mipmap/ic_launcher"
        android:label="Agora SMS Filter"
        android:theme="@style/Theme.AppCompat.NoActionBar">

        <!-- Interceptor Core Engine -->
        <service
            android:name=".services.SMSNotificationListener"
            android:label="Agora Interceptor Core"
            android:permission="android.permission.BIND_NOTIFICATION_LISTENER_SERVICE"
            android:exported="true">
            <intent-filter>
                <action android:name="android.service.notification.NotificationListenerService" />
            </intent-filter>
        </service>

        <!-- Local DB Bootstrapping Receiver -->
        <receiver android:name=".receivers.BootReceiver" android:exported="false">
            <intent-filter>
                <action android:name="android.intent.action.BOOT_COMPLETED" />
            </intent-filter>
        </receiver>

    </application>
</manifest>
```

---

## 4. Kotlin Source Implementation Details

### 4.1 Interceptor Core (`SMSNotificationListener.kt`)
This component executes on the system main binder thread loop. Heavy processing must be immediately offloaded to a coroutine background worker context.

```kotlin
package com.example.agora.smsfilter.services

import android.service.notification.NotificationListenerService
import android.service.notification.StatusBarNotification
import android.app.Notification
import android.os.Bundle
import android.util.Log
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import com.example.agora.smsfilter.data.MessageDatabase
import com.example.agora.smsfilter.data.PoliticalMessageEntity

class SMSNotificationListener : NotificationListenerService() {

    private val serviceScope = CoroutineScope(Dispatchers.IO)
    private val targetPackage = "com.google.android.apps.messaging"

    override fun onNotificationPosted(sbn: StatusBarNotification) {
        if (sbn.packageName != targetPackage) return

        val extras: Bundle = sbn.notification.extras
        val title: String = extras.getString(Notification.EXTRA_TITLE) ?: ""
        val body: String = extras.getCharSequence(Notification.EXTRA_TEXT)?.toString() ?: ""

        if (body.isEmpty()) return

        serviceScope.launch {
            if (evaluateHeuristics(body)) {
                // Instantly command system server to tear down notification UI
                cancelNotification(sbn.key)
                
                // Commit to local indexed persistence
                persistToStorage(title, body)
            }
        }
    }

    private fun evaluateHeuristics(messageText: String): Boolean {
        // Compile static matching constraints to prevent object reallocation loops
        val politicalRegex = Regex(
            "\\b(vote|campaign|donate|election|candidate|pac|democrat|republican|ballot|contribute|trump|harris)\\b", 
            RegexOption.IGNORE_CASE
        )
        return politicalRegex.containsMatchIn(messageText)
    }

    private suspend fun persistToStorage(sender: String, message: String) {
        try {
            val db = MessageDatabase.getInstance(applicationContext)
            val entity = PoliticalMessageEntity(
                sender = sender,
                messageBody = message,
                timestamp = System.currentTimeMillis()
            )
            db.messageDao().insertMessage(entity)
            Log.d("AgoraCore", "Successfully indexed political context from $sender")
        } catch (e: Exception) {
            Log.e("AgoraCore", "Storage write exception encountered", e)
        }
    }
}
```

---

## 5. Storage Layer Schema Configuration (Room/SQLite)

The local data persistence architecture utilizes standard Android Room schema mappings compiling into a lightweight, local transactional SQLite binary on-device.

### 5.1 Entity Contract Schema (`PoliticalMessageEntity.kt`)
```kotlin
package com.example.agora.smsfilter.data

import androidx.room.Entity
import androidx.room.PrimaryKey
import androidx.room.ColumnInfo

@Entity(tableName = "indexed_political_messages")
data class PoliticalMessageEntity(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    @ColumnInfo(name = "sender_identity") val sender: String,
    @ColumnInfo(name = "message_payload") val messageBody: String,
    @ColumnInfo(name = "intercept_timestamp") val timestamp: Long
)
```

### 5.2 Data Access Object Template (`MessageDao.kt`)
```kotlin
package com.example.agora.smsfilter.data

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
```

---

## 6. Execution Lifecycle & Toolchain Checklist

Because this tool runs exclusively as an internal, side-loaded project utility, use the following engineering sequence to bypass Google Play testing parameters:

* **Compilation Architecture:** Target SDK 34 / 35 using Kotlin 1.9+ toolchain bindings.
* **Deployment Vector:** Build unsigned local debug targets using Gradle directly onto testbed hardware.
* **Bypassing the Android OS Permission Settings Barrier:**
  Android considers `NotificationListenerService` access a severe privacy risk. Standard application runtime popups cannot activate this. Execute the following sequence on the terminal host machine once side-loading finishes to inject authorization headers immediately:
  ```bash
  adb shell cmd notification allow_listener com.example.agora.smsfilter/com.example.agora.smsfilter.services.SMSNotificationListener
  ```
* **Production Validation Sequence:** Send a test payload containing structural matching triggers (e.g., `"Click here to donate to the campaign campaign"`) to verify the background loop triggers an absolute UI dismissal within milliseconds.
