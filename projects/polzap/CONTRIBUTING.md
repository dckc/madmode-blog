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

## Testing

```sh
nix develop -c ./gradlew test
```

Runs the JVM unit tests (`app/src/test/`). This is the conventional command and
the one to run before committing — a broken scorer or filter fails it.

The parity test (`ScorerParityTest`) only runs when `SMS_DUMP` is set to the
dump path; see "The scorer and anti-drift" below.

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

## The scorer and anti-drift

The political filter lives in two places that must stay in sync:

- **`PoliticalScorer.kt`** (app) — what actually runs on the phone.
- **`scripts/scorer.py`** (eval) — the Python port used to measure precision/recall.

`ScorerParityTest` is the guard: with `SMS_DUMP` set, it runs the Kotlin scorer
over the real dump and asserts it matches the Python reference predictions. If
you change the scoring rules, update **both** files and re-run the parity test
(`SMS_DUMP=... ./gradlew :app:testDebugUnitTest --tests "*ScorerParityTest*"`).

## Design Notes

1. The carrier routes incoming texts to the default handler
   (`com.google.android.apps.messaging`).
2. That handler posts a status-bar notification, which the
   `SMSNotificationListener` catches.
3. The body text is scored by `PoliticalScorer` (weighted keywords + URL bonus
   + structural markers, threshold 3).
4. If it scores at or above threshold: `cancelNotification()` tears down the
   alert and the message is persisted to the local Room DB. Otherwise the event
   loop does nothing, so the text is left to be read normally.
