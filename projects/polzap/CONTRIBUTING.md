# Development and Design notes

polzap is an internal Android utility that intercepts political SMS/RCS
messages, indexes them into a local Room database, and auto-dismisses the
matching notification. See `README.md` for what it does and how to use it;
this file is the briefing for working on the code.

## Building

```sh
nix develop                          # enter dev shell (JDK 17, Gradle, Android SDK, adb)
./gradlew assembleDebug          # -> app/build/outputs/apk/debug/app-debug.apk
```

The APK is unsigned debug, built for side-loading, not Play.

## Enable the notification listener

Android refuses to let a normal app activate a `NotificationListenerService`.
Once the app is installed, grant it via adb from the host:

```sh
adb shell cmd notification allow_listener \
  madmode.polzap.smsfilter/madmode.polzap.smsfilter.services.SMSNotificationListener
```

## Layout

- **flake.nix** — dev shell (JDK 17, Gradle, Android SDK, adb, python3).
- **android app** — `app/build.gradle.kts`, `app/src/main/AndroidManifest.xml`, `app/src/main/java/`.
- **python eval** — `scripts/*.py` (parse, scorer, evaluate, sample, build_spreadsheet).

## File headers

Every source file carries a one-line statement of purpose and an
`SPDX-License-Identifier: CC0-1.0` header at the top; `head` on any file tells
you what it's for. Keep new files to the same pattern.

## Design Notes

1. The carrier routes incoming texts to the default handler
   (`com.google.android.apps.messaging`).
2. That handler posts a status-bar notification, which the
   `SMSNotificationListener` catches.
3. The body text is run against a heuristic regex
   (`vote|campaign|donate|election|...`).
4. If it matches: `cancelNotification()` tears down the alert and the message is
   persisted to the local Room DB. Otherwise the event loop does nothing, so
   the text is left to be read normally.
