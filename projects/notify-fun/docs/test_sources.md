# XDG Notification Test Sources

Sources of realistic `org.freedesktop.Notifications.Notify` message examples,
for building a test corpus.

## 1. libnotify test suite (primary source)

**Repository**: https://gitlab.gnome.org/GNOME/libnotify (mirror: https://github.com/GNOME/libnotify)  
**License**: LGPL-2.1-or-later  
**Files**: `tests/test-*.c`  
**Coverage**: 20 standalone C programs, each exercising one notification feature.

| Test name | What it exercises |
|-----------|-------------------|
| `basic` | long summary, long body, summary-only with NOTIFY_EXPIRES_NEVER |
| `urgency` | low / normal / critical urgency hints |
| `transient` | `transient` boolean hint |
| `persistence` | action with timeout=0 (never expire) |
| `resident` | `resident` boolean hint, 3 actions (prev/pause/next) |
| `default-action` | single "default" action, `category` hint |
| `multi-actions` | 3 actions, urgency=critical, transient hint, category hint |
| `action-icons` | `action-icons` boolean hint, themed icon action IDs |
| `markup` | body text with HTML `<b>` `<u>` `<i>` `<a>` tags |
| `image` | themed icon, file URI icon, raw pixbuf via `image-data` hint |
| `replace` | `replaces_id` via `notify_notification_update()` |
| `removal` | `CloseNotification` via `notify_notification_close()` |
| `error` | (placeholder — no real error condition) |
| `server-info` | `GetServerInformation` |
| `rtl` | right-to-left layout |
| `xy` | `x`/`y` int32 position hints |
| `xy-actions` | `x`/`y` position hints + actions |
| `xy-stress` | many rapid `x`/`y` updates |
| `size-changes` | icon size edge cases |
| `replace-widget` | (removed — widget anchoring deprecated) |

All tests call `notify_notification_new(summary, body, icon)` then set
properties and call `notify_notification_show()`.

## 2. XDG Desktop Notification Specification

**URL**: https://specifications.freedesktop.org/notification/latest/  
**License**: Public domain / open specification (freedesktop.org)  
**Relevant sections**: Hints table (§Hints), Categories table (§Categories)

The spec documents standard hints and categories. Each is a potential
test case:

- **Urgency**: `urgency` byte hint (0=low, 1=normal, 2=critical)
- **Categories**: `device`, `device.added`, `device.error`, `device.removed`,
  `email`, `email.arrived`, `email.bounced`, `im`, `im.error`, `im.received`,
  `network`, `network.connected`, `network.disconnected`, `network.error`,
  `presence`, `presence.offline`, `presence.online`, `transfer`,
  `transfer.complete`, `transfer.error`
- **Hints**: `action-icons`, `category`, `desktop-entry`, `image-data`,
  `image-path`, `resident`, `sound-file`, `sound-name`, `suppress-sound`,
  `transient`, `x`, `y`, `urgency`, `sender-pid`

## 3. Jeepney library

**Repository**: https://gitlab.com/takluyver/jeepney  
**License**: BSD-2-Clause  
**Relevance**: Low-level D-Bus message builder used by this project.
Its own test suite exercises D-Bus marshalling for all standard types.
Not a source of *notification* examples, but useful for verifying
wire-format correctness.

## 4. Notification daemon implementations

These implement the *server* side. Their documentation and test suites
describe what hints they support:

| Daemon | URL | License |
|--------|-----|---------|
| **mako** | https://github.com/emersion/mako | MIT |
| **dunst** | https://github.com/dunst-project/dunst | BSD-3-Clause |
| **GNOME Shell** | https://gitlab.gnome.org/GNOME/gnome-shell | GPL-2.0-or-later |
| **KDE Plasma** | https://invent.kde.org/plasma/plasma-workspace | LGPL-2.0-or-later |
| **lxqt-notificationd** | https://github.com/lxqt/lxqt-notificationd | LGPL-2.1-or-later |

`man mako` and `man dunst` document the hints each daemon respects,
which can reveal what real-world usage looks like.

## 5. Real-world desktop applications

Capturing actual D-Bus traffic (e.g. via `busctl monitor`) from common
applications provides the most realistic corpus. Tools like
`dbus-monitor --session` or `busctl monitor` can dump raw messages.

Applications worth capturing:
- **Firefox/Chromium** — web notifications with icon, summary, body, actions
- **Slack/Discord/Telegram** — IM notifications with `im.received` category,
  actions (Reply, Mark as Read), sound hints
- **Thunderbird/Geary** — email notifications with `email.arrived` category,
  archive/reply actions
- **GNOME Software** — critical urgency, `transfer.complete` category
- **Transmission** — download complete with `transfer.complete` category
- **VS Code** — build task notifications with actions

## 6. notify-send man page / help output

`notify-send` (from libnotify) has CLI options that map 1:1 to the
Notify method parameters. Running `notify-send --help` documents all
supported flags (`-u` urgency, `-c` category, `-t` timeout,
`-A` actions, `-h` hints, `-e` transient, `-i` icon).

## License compatibility note

The libnotify test files are **LGPL-2.1-or-later** — compatible with this
project's use since we extract *ideas/patterns* not verbatim C code.
The generated binary payloads are derived from the XDG Notification
specification (open standard) and do not incorporate libnotify code.

Jeepney is **BSD-2-Clause** — compatible with any use.
