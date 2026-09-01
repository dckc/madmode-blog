// Interceptor core: catches Google Messages notifications, runs the body
// against political heuristics, dismisses matches, and persists them.
// SPDX-License-Identifier: CC0-1.0
package madmode.polzap.smsfilter.services

import android.app.Notification
import android.os.Bundle
import android.service.notification.NotificationListenerService
import android.service.notification.StatusBarNotification
import android.util.Log
import madmode.polzap.smsfilter.data.MessageDatabase
import madmode.polzap.smsfilter.data.PoliticalMessageEntity
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.cancel
import kotlinx.coroutines.launch

class SMSNotificationListener : NotificationListenerService() {

    private val serviceScope = CoroutineScope(Dispatchers.IO)
    private val targetPackage = "com.google.android.apps.messaging"

    override fun onDestroy() {
        serviceScope.cancel()
        super.onDestroy()
    }

    override fun onNotificationPosted(sbn: StatusBarNotification) {
        if (sbn.packageName != targetPackage) return

        val extras: Bundle = sbn.notification.extras
        val title: String = extras.getString(Notification.EXTRA_TITLE) ?: ""
        val body: String = extras.getCharSequence(Notification.EXTRA_TEXT)?.toString() ?: ""

        if (body.isEmpty()) return

        serviceScope.launch {
            if (evaluateHeuristics(body)) {
                cancelNotification(sbn.key)
                persistToStorage(title, body)
            }
        }
    }

    private fun evaluateHeuristics(messageText: String): Boolean {
        return PoliticalScorer.isPolitical(messageText)
    }

    private suspend fun persistToStorage(title: String, message: String) {
        try {
            val db = MessageDatabase.getInstance(applicationContext)
            val entity = PoliticalMessageEntity(
                sender = title,
                messageBody = message,
                timestamp = System.currentTimeMillis()
            )
            db.messageDao().insertMessage(entity)
            Log.d("PolzapCore", "Successfully indexed political context from $title")
        } catch (e: Exception) {
            Log.e("PolzapCore", "Storage write exception encountered", e)
        }
    }
}
