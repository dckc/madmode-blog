# polzap

*Get me off this crazy thing!* — dozens of political texts a day, mostly from
ActBlue. polzap makes the notifications stop.

But it must keep alerting me: people I know *and* solicited-but-unknown senders
(pharmacy, repair person). Never suppress at the app level. So polzap only
silences the notifications that look like political spam; everything you
actually want stays loud. Google Messages stays your default handler, and the
texts are still delivered and stored — polzap just indexes them and kills the
ping.

This is a quick hack. If it breaks, you get to keep both pieces.

## Use

1. Build the app from this `projects/polzap` directory:

   ```sh
   nix build
   ```

   The APK is at `result/polzap.apk`.
2. Install the bundle on the phone ("sideloading"): put the APK on the device
   and tap it, or, with the phone plugged in via USB, run this from your
   computer:

   ```sh
   adb install result/polzap.apk
   ```

   Note: the app has **no launcher icon** on purpose — it's a background
   utility, so nothing new appears in your app drawer after install. That's
   normal, not a failed install. To confirm it's there:

   ```sh
   adb shell pm list packages | grep polzap
   ```

   You should see `package:madmode.polzap.smsfilter`.
3. Android forbids normal apps from activating a notification listener, so
   grant it from the host after install:

   ```sh
   adb shell cmd notification allow_listener \
     madmode.polzap.smsfilter/madmode.polzap.smsfilter.services.SMSNotificationListener
   ```

4. Test it: send a text containing a match trigger, e.g.

   ```
   donate to the campaign
   ```

   Its notification should be dismissed, and the message indexed in
   `polzap_index.db` (see below). Non-political texts are left untouched.

## Query the database

The index is a SQLite database in the app's private storage. Pull it to your
computer and query it there. Room keeps recent writes in a write-ahead log, so
grab the `.db` **and** its `-wal`/`-shm` sidecars together, or you'll see an
empty database:

```sh
cd /tmp
for f in polzap_index.db polzap_index.db-wal polzap_index.db-shm; do
  adb shell run-as madmode.polzap.smsfilter cat databases/$f > /tmp/$f
done
sqlite3 /tmp/polzap_index.db "SELECT * FROM indexed_political_messages;"
```

Columns: `id`, `sender_identity`, `message_payload`, `intercept_timestamp`
(epoch millis).

## Troubleshooting

### `adb: no devices/emulators found`

`adb` can't see your phone. This means either the phone isn't connected, or
adb doesn't have permission / USB debugging isn't on.

1. Plug the phone into the computer with a USB cable.
2. On the phone, enable **Developer options** (Settings » About phone » tap
   "Build number" seven times), then turn on **USB debugging** under
   Developer options.
3. Confirm adb sees it:

   ```sh
   adb devices
   ```

   You should see the device listed. If it shows as "unauthorized", tap
   **Allow USB debugging** on the phone's screen.
4. Re-run the install command.
