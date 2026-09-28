// SPDX-FileCopyrightText: 2026 Dan Connolly
// SPDX-License-Identifier: Apache-2.0

/** Tests for D-Bus notification serialization.
 *
 * Uses Node's built-in test runner (`node:test`).  Run with:
 *   node --test test/notification.test.ts
 *
 * D-Bus Specification v0.43, 2024-10-29 — wire format reference.
 * https://dbus.freedesktop.org/doc/dbus-specification.html
 *
 * XDG Desktop Portal Notification interface v2 — payload semantics.
 * https://flatpak.github.io/xdg-desktop-portal/docs/doc-org.freedesktop.portal.Notification.html */

import assert from "node:assert/strict";
import test from "node:test";

import { serialise, MESSAGE_TYPE_METHOD_CALL, FIELD_SIGNATURE } from "../src/dbus_msg.ts";
import { buildAddNotificationPayload, notificationToDict } from "../src/notification.ts";

test("dbus_msg: serialise a minimal method call", () => {
  const headers = new Map<number, unknown>();
  headers.set(1, "/org/freedesktop/DBus");       // FIELD_PATH
  headers.set(6, "org.freedesktop.DBus");          // FIELD_DESTINATION
  headers.set(2, "org.freedesktop.DBus");          // FIELD_INTERFACE
  headers.set(3, "Hello");                         // FIELD_MEMBER

  const msg = serialise(MESSAGE_TYPE_METHOD_CALL, 1, headers, "", []);

  // Header: endian=l, type=1 (method call), flags=0, proto=1
  assert.equal(msg[0], 0x6c, "little-endian marker");
  assert.equal(msg[1], 1, "method call type");
  assert.equal(msg[2], 0, "flags");
  assert.equal(msg[3], 1, "protocol version");

  // Body length = 0
  const bodyLen = new DataView(msg.buffer, msg.byteOffset + 4, 4).getUint32(0, true);
  assert.equal(bodyLen, 0, "empty body");

  // Serial = 1
  const serial = new DataView(msg.buffer, msg.byteOffset + 8, 4).getUint32(0, true);
  assert.equal(serial, 1, "serial");

  // Object path should be present in header fields
  const asText = new TextDecoder().decode(msg);
  assert.ok(asText.includes("/org/freedesktop/DBus"), "object path in message");
  assert.ok(asText.includes("Hello"), "method name in message");
});

test("dbus_msg: serialise a method call with body", () => {
  const headers = new Map<number, unknown>();
  headers.set(1, "/org/freedesktop/Notifications");
  headers.set(6, "org.freedesktop.Notifications");
  headers.set(2, "org.freedesktop.Notifications");
  headers.set(3, "Notify");
  headers.set(FIELD_SIGNATURE, "susssasa{sv}i");

  const body: unknown[] = [
    "tiny-notify",        // app_name (s)
    0,                    // replaces_id (u)
    "",                   // app_icon (s)
    "CI Failed!",         // summary (s)
    "Your build broke.",  // body (s)
    [],                   // actions (as)
    {},                   // hints (a{sv})
    -1,                   // expire_timeout (i)
  ];

  const msg = serialise(MESSAGE_TYPE_METHOD_CALL, 2, headers, "susssasa{sv}i", body);

  assert.equal(msg[0], 0x6c, "little-endian marker");
  assert.equal(msg[1], 1, "method call type");
  assert.equal(msg[3], 1, "protocol version");

  const bodyLen = new DataView(msg.buffer, msg.byteOffset + 4, 4).getUint32(0, true);
  assert.ok(bodyLen > 0, "non-empty body");

  const asText = new TextDecoder().decode(msg);
  assert.ok(asText.includes("tiny-notify"), "app name in body");
  assert.ok(asText.includes("CI Failed!"), "summary in body");
  assert.ok(asText.includes("Your build broke."), "body text in body");
});

test("dbus_msg: serialise addNotification with a{sv} dict", () => {
  const headers = new Map<number, unknown>();
  headers.set(1, "/org/freedesktop/portal/notification");
  headers.set(6, "org.freedesktop.portal.Desktop");
  headers.set(2, "org.freedesktop.portal.Notification");
  headers.set(3, "AddNotification");
  headers.set(FIELD_SIGNATURE, "sa{sv}");

  const dict: Record<string, [string, unknown]> = {
    title: ["s", "Hello"],
    body: ["s", "World"],
    priority: ["s", "low"],
  };

  const body: unknown[] = ["test-id", dict];
  const msg = serialise(MESSAGE_TYPE_METHOD_CALL, 1, headers, "sa{sv}", body);

  assert.equal(msg[0], 0x6c, "little-endian marker");

  const bodyLen = new DataView(msg.buffer, msg.byteOffset + 4, 4).getUint32(0, true);
  assert.ok(bodyLen > 0, "non-empty body");

  const asText = new TextDecoder().decode(msg);
  assert.ok(asText.includes("test-id"), "notification id in body");
  assert.ok(asText.includes("Hello"), "title in body");
  assert.ok(asText.includes("World"), "body text in body");
  assert.ok(asText.includes("priority"), "priority key in body");
  assert.ok(asText.includes("low"), "priority value in body");
});

test("notification: buildAddNotificationPayload basic", () => {
  const payload = buildAddNotificationPayload("test-1", {
    title: "Hello from TypeScript",
    body: "This is a test notification.",
    priority: "normal",
  });

  // Validate header bytes
  assert.equal(payload[0], 0x6c, "little-endian");
  assert.equal(payload[1], 1, "method call");

  // Scan for expected strings
  const text = new TextDecoder().decode(payload);
  assert.ok(text.includes("AddNotification"), "method name");
  assert.ok(text.includes("test-1"), "notification id");
  assert.ok(text.includes("Hello from TypeScript"), "title");
  assert.ok(text.includes("This is a test notification."), "body");
  assert.ok(text.includes("normal"), "priority");
  assert.ok(text.includes("sa{sv}"), "body signature");
});

test("notification: buildAddNotificationPayload with all fields", () => {
  const payload = buildAddNotificationPayload("full-test", {
    title: "Full Test",
    body: "All fields populated.",
    "markup-body": "<b>Full</b> <i>Test</i>",
    priority: "high",
    "default-action": "app.view",
    category: "im.received",
    "display-hint": ["transient", "hide-content-on-lockscreen"],
    buttons: [
      { label: "View", action: "app.view" },
      { label: "Dismiss", action: "app.dismiss", purpose: "call.decline" },
    ],
  });

  const text = new TextDecoder().decode(payload);
  assert.ok(text.includes("Full Test"), "title");
  assert.ok(text.includes("All fields populated."), "body");
  assert.ok(text.includes("<b>Full</b> <i>Test</i>"), "markup body");
  assert.ok(text.includes("high"), "priority");
  assert.ok(text.includes("app.view"), "default action");
  assert.ok(text.includes("im.received"), "category");
  assert.ok(text.includes("transient"), "display hint");
  assert.ok(text.includes("hide-content-on-lockscreen"), "display hint 2");
  assert.ok(text.includes("View"), "button label");
  assert.ok(text.includes("Dismiss"), "button label 2");
  assert.ok(text.includes("app.dismiss"), "button action");
  assert.ok(text.includes("call.decline"), "button purpose");
});

test("notification: notificationToDict round-trip", () => {
  const n = {
    title: "Test",
    body: "Body",
    priority: "urgent" as const,
  };

  const dict = notificationToDict(n);

  assert.deepEqual(dict.title, ["s", "Test"]);
  assert.deepEqual(dict.body, ["s", "Body"]);
  assert.deepEqual(dict.priority, ["s", "urgent"]);
});

test("notification: icon serialization", () => {
  const payload = buildAddNotificationPayload("icon-test", {
    title: "Icon Test",
    icon: { themed: ["dialog-warning"] },
  });

  const text = new TextDecoder().decode(payload);
  assert.ok(text.includes("icon"), "icon key in dict");
  assert.ok(text.includes("dialog-warning"), "themed icon name");
  assert.ok(text.includes("themed"), "themed key in struct");

  // String icon (backward compat)
  const payload2 = buildAddNotificationPayload("icon-string", {
    title: "String Icon",
    icon: "dialog-info",
  });

  const text2 = new TextDecoder().decode(payload2);
  assert.ok(text2.includes("dialog-info"), "string icon name");

  // File descriptor icon
  const payload3 = buildAddNotificationPayload("icon-fd", {
    title: "FD Icon",
    icon: { "file-descriptor": 42 },
  });

  const text3 = new TextDecoder().decode(payload3);
  assert.ok(text3.includes("file-descriptor"), "file-descriptor key");
});

test("notification: sound serialization", () => {
  // Default sound
  const payload = buildAddNotificationPayload("sound-test", {
    title: "Sound Test",
    sound: "default",
  });

  const text = new TextDecoder().decode(payload);
  assert.ok(text.includes("default"), "default sound");

  // Silent
  const payload2 = buildAddNotificationPayload("sound-silent", {
    title: "Silent",
    sound: "silent",
  });

  const text2 = new TextDecoder().decode(payload2);
  assert.ok(text2.includes("silent"), "silent sound");
});

test("notification: display-hint serialization", () => {
  const payload = buildAddNotificationPayload("hint-test", {
    title: "Hints",
    "display-hint": ["transient", "persistent"],
  });

  const text = new TextDecoder().decode(payload);
  assert.ok(text.includes("transient"), "transient hint");
  assert.ok(text.includes("persistent"), "persistent hint");
});

test("notification: empty notification (only id)", () => {
  const payload = buildAddNotificationPayload("empty-test", {});

  const text = new TextDecoder().decode(payload);
  assert.ok(text.includes("empty-test"), "id present");
  assert.equal(payload[0], 0x6c, "valid message");
});

// ── Fixture comparison ──────────────────────────────────────────────
// Fixtures generated by test/notify_fixtures.py using jeepney v0.9.0.
// Each fixture builds a Notify(susssasa{sv}i) method call and
// serialises it.  We rebuild the same payload in TypeScript and
// compare byte-for-byte.

import { readFileSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const FIXTURES_DIR = join(__dirname, "fixtures");

/** Build a Notify(susssasa{sv}i) method-call body for the given fields. */
function buildNotifyBody(
  appName: string,
  replacesId: number,
  appIcon: string,
  summary: string,
  body: string,
  actions: readonly string[],
  hints: Record<string, [string, unknown]>,
  expireTimeout: number,
  serial: number,
): Uint8Array {
  const headers = new Map<number, unknown>();
  headers.set(1, "/org/freedesktop/Notifications");
  headers.set(6, "org.freedesktop.Notifications");
  headers.set(2, "org.freedesktop.Notifications");
  headers.set(3, "Notify");
  headers.set(FIELD_SIGNATURE, "susssasa{sv}i");

  return serialise(
    MESSAGE_TYPE_METHOD_CALL,
    serial,
    headers,
    "susssasa{sv}i",
    [appName, replacesId, appIcon, summary, body, actions, hints, expireTimeout],
  );
}

interface FixtureCase {
  readonly name: string;
  readonly appName: string;
  readonly replacesId: number;
  readonly appIcon: string;
  readonly summary: string;
  readonly body: string;
  readonly actions: readonly string[];
  readonly hints: Record<string, [string, unknown]>;
  readonly expireTimeout: number;
  readonly serial: number;
}

/** All fixture cases derived from test/notify_fixtures.py. */
const FIXTURES: FixtureCase[] = [
  {
    name: "libnotify-basic-long-summary", serial: 1,
    appName: "Basics", replacesId: 0, appIcon: "",
    summary: "Summary that is very long 8374983278r32j4 rhjjfh dw8f 43jhf 8ds7 "
      + "ur2389f jdbjkt h8924yf jkdbjkt 892hjfiHER98HEJIF BDSJHF hjdhF JKLH "
      + "890YRHEJHFU 89HRJKSHdd dddd ddddd dddd ddddd dddd ddddd dddd dddd "
      + "ddd ddd dddd Fdd d ddddd dddddddd ddddddddhjkewdkjsjfjk sdhkjf hdkj "
      + "dadasdadsa adsd asd sd saasd fadskfkhsjf hsdkhfkshfjkhsd kjfhsjdkhfj "
      + "ksdhfkjshkjfsd sadhfjkhaskd jfhsdajkfhkjs dhfkjsdhfkjs adhjkfhasdkj "
      + "fhdsakjhfjk asdhkjkfhd akfjshjfsk afhjkasdhf jkhsdaj hf kjsdfahkfh "
      + "sakjhfksdah kfdashkjf ksdahfj shdjdh",
    body: "Content",
    actions: [], hints: {}, expireTimeout: 3000,
  },
  {
    name: "libnotify-basic-long-body", serial: 2,
    appName: "Basics", replacesId: 0, appIcon: "",
    summary: "Summary",
    body: "Content that is very long 8374983278r32j4 rhjjfh dw8f 43jhf 8ds7 "
      + "ur2389f jdbjkt h8924yf jkdbjkt 892hjfiHER98HEJIF BDSJHF hjdhF JKLH "
      + "890YRHEJHFU 89HRJKSHdd dddd ddddd dddd ddddd dddd ddddd dddd dddd "
      + "ddd ddd dddd Fdd d ddddd dddddddd ddddddddhjkewdkjsjfjk sdhkjf hdkj "
      + "dadasdadsa adsd asd sd saasd fadskfkhsjf hsdkhfkshfjkhsd kjfhsjdkhfj "
      + "ksdhfkjshkjfsd sadhfjkhaskd jfhsdajkfhkjs dhfkjsdhfkjs adhjkfhasdkj "
      + "fhdsakjhfjk asdhkjkfhd akfjshjfsk afhjkasdhf jkhsdaj hf kjsdfahkfh "
      + "sakjhfksdah kfdashkjf ksdahfj shdjdh",
    actions: [], hints: {}, expireTimeout: 3000,
  },
  {
    name: "libnotify-basic-summary-only", serial: 3,
    appName: "Basics", replacesId: 0, appIcon: "",
    summary: "Summary only there is no message content",
    body: "", actions: [], hints: {}, expireTimeout: 0,
  },
  {
    name: "libnotify-urgency-low", serial: 4,
    appName: "Urgency", replacesId: 0, appIcon: "",
    summary: "Low Urgency", body: "Joe signed online.",
    actions: [], hints: { urgency: ["y", 0] }, expireTimeout: -1,
  },
  {
    name: "libnotify-urgency-normal", serial: 5,
    appName: "Urgency", replacesId: 0, appIcon: "",
    summary: "Normal Urgency", body: "You have a meeting in 10 minutes.",
    actions: [], hints: { urgency: ["y", 1] }, expireTimeout: -1,
  },
  {
    name: "libnotify-urgency-critical", serial: 6,
    appName: "Urgency", replacesId: 0, appIcon: "",
    summary: "Critical Urgency",
    body: "This message will self-destruct in 10 seconds.",
    actions: [], hints: { urgency: ["y", 2] }, expireTimeout: 10000,
  },
  {
    name: "libnotify-transient", serial: 7,
    appName: "Transient Test", replacesId: 0, appIcon: "audio-volume-medium",
    summary: "Some transient change", body: "Something happened",
    actions: [], hints: { transient: ["b", true] }, expireTimeout: -1,
  },
  {
    name: "libnotify-default-action", serial: 8,
    appName: "Default Action Test", replacesId: 0, appIcon: "",
    summary: "Matt is online", body: "",
    actions: ["default", "Do Default Action"],
    hints: { category: ["s", "presence.online"] }, expireTimeout: -1,
  },
  {
    name: "libnotify-markup", serial: 9,
    appName: "Markup", replacesId: 0, appIcon: "",
    summary: "Summary",
    body: "Some <b>bold</b>, <u>underlined</u>, <i>italic</i>, "
      + "<a href='http://www.google.com'>linked</a> text",
    actions: [], hints: {}, expireTimeout: 3000,
  },
  {
    name: "libnotify-multi-actions", serial: 10,
    appName: "Multi Action Test", replacesId: 0, appIcon: "drive-harddisk-symbolic",
    summary: "Low disk space",
    body: "You can free up some disk space by emptying the trash can.",
    actions: ["help", "Help", "ignore", "Ignore", "empty", "Empty Trash"],
    hints: { transient: ["b", true], urgency: ["y", 2], category: ["s", "device"] },
    expireTimeout: -1,
  },
  {
    name: "libnotify-action-icons", serial: 11,
    appName: "Action Icon Test", replacesId: 0, appIcon: "",
    summary: "Music Player", body: "Some solid funk",
    actions: ["media-skip-backward", "Previous", "media-playback-pause", "Pause",
      "media-skip-forward", "Next"],
    hints: { "action-icons": ["b", true] }, expireTimeout: -1,
  },
  {
    name: "libnotify-resident", serial: 12,
    appName: "Resident Test", replacesId: 0, appIcon: "audio-x-generic",
    summary: "Music Player", body: "Playing some fine song",
    actions: ["previous", "Previous", "pause", "Pause", "next", "Next"],
    hints: { resident: ["b", true] }, expireTimeout: -1,
  },
  {
    name: "libnotify-persistence", serial: 13,
    appName: "Persistence Test", replacesId: 0,
    appIcon: "software-update-available-symbolic",
    summary: "Software Updates Available",
    body: "Important updates for your apps are now available.",
    actions: ["install", "Install now"], hints: {}, expireTimeout: 0,
  },
  {
    name: "libnotify-xy", serial: 14,
    appName: "XY", replacesId: 0, appIcon: "",
    summary: "X, Y Test", body: "This notification should point to 150, 10",
    actions: [], hints: { x: ["i", 150], y: ["i", 10] }, expireTimeout: -1,
  },
  {
    name: "libnotify-replace-first", serial: 15,
    appName: "Replace Test", replacesId: 0, appIcon: "",
    summary: "Summary", body: "First message",
    actions: [], hints: {}, expireTimeout: 0,
  },
  {
    name: "libnotify-replace-second", serial: 16,
    appName: "Replace Test", replacesId: 0, appIcon: "",
    summary: "Second Summary", body: "First mesage was replaced",
    actions: [], hints: {}, expireTimeout: -1,
  },
  {
    name: "chat-message", serial: 17,
    appName: "Slack", replacesId: 0, appIcon: "slack",
    summary: "Alice", body: "What do you think about the proposal?",
    actions: ["reply", "Reply", "mark_read", "Mark Read"],
    hints: { category: ["s", "im.received"], "sound-name": ["s", "message-new-instant"] },
    expireTimeout: -1,
  },
  {
    name: "email-arrival", serial: 18,
    appName: "Thunderbird", replacesId: 0, appIcon: "thunderbird",
    summary: "New mail from Bob",
    body: "Meeting tomorrow at 3pm in the conference room.",
    actions: ["reply", "Reply", "archive", "Archive"],
    hints: { category: ["s", "email.arrived"] }, expireTimeout: 8000,
  },
  {
    name: "battery-critical", serial: 19,
    appName: "GNOME Shell", replacesId: 0, appIcon: "battery-caution-charging-symbolic",
    summary: "Battery Critical", body: "10% remaining — plug in now.",
    actions: [], hints: { urgency: ["y", 2], resident: ["b", true] }, expireTimeout: 0,
  },
  {
    name: "download-complete", serial: 20,
    appName: "Firefox", replacesId: 0, appIcon: "firefox",
    summary: "Download complete",
    body: "notify-fun-0.1.0.tar.gz (2.4 MB) — 100%",
    actions: [], hints: { category: ["s", "transfer.complete"] }, expireTimeout: 5000,
  },
  {
    name: "network-disconnected", serial: 21,
    appName: "NetworkManager", replacesId: 0, appIcon: "network-offline-symbolic",
    summary: "Connection lost", body: "You are no longer connected to the internet.",
    actions: [],
    hints: { category: ["s", "network.disconnected"], urgency: ["y", 1] },
    expireTimeout: -1,
  },
];

test("fixtures: match jeepney-generated .bin files", () => {
  for (const tc of FIXTURES) {
    const fixturePath = join(FIXTURES_DIR, `${tc.name}.bin`);
    const fixtureBytes = readFileSync(fixturePath);

    const tsBytes = buildNotifyBody(
      tc.appName, tc.replacesId, tc.appIcon,
      tc.summary, tc.body, tc.actions, tc.hints,
      tc.expireTimeout, tc.serial,
    );

    assert.equal(
      tsBytes.length, fixtureBytes.length,
      `${tc.name}: size mismatch (ts=${tsBytes.length} fixture=${fixtureBytes.length})`,
    );

    for (let i = 0; i < tsBytes.length; i++) {
      if (tsBytes[i] !== fixtureBytes[i]) {
        const start = Math.max(0, i - 4);
        const end = Math.min(tsBytes.length, i + 8);
        const tsHex = Array.from(tsBytes.slice(start, end))
          .map((b) => b.toString(16).padStart(2, "0")).join(" ");
        const fxHex = Array.from(fixtureBytes.slice(start, end))
          .map((b) => b.toString(16).padStart(2, "0")).join(" ");
        assert.fail(
          `${tc.name}: byte mismatch at offset ${i} `
          + `(ts=0x${tsBytes[i].toString(16)} fix=0x${fixtureBytes[i].toString(16)})`
          + `\n  TS: ${tsHex}\n  FX: ${fxHex}`,
        );
      }
    }
  }
});
