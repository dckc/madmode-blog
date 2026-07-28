I want `systemd` user services paired with MATE desktop panel status icons / menus.

Perhaps I want to start the service using a menu item or button. Then I want a status bar icon to show me what's up. And a right click way to stop it?

Are there Mac OS Human Interface Guidelines for this?

Are there Gnome norms that I'm missing by using MATE? How about Plasma?

In particular, I want `opencode web` as such a service. I want a guesture to copy the url and to open the url in a browser.

## Where "Add to Panel..." comes from

MATE panel applets are registered via `.mate-panel-applet` files in `/usr/share/mate-panel/applets/`, each backed by a D-Bus service file in `/usr/share/dbus-1/services/`. The "Add to Panel..." dialog scans those system-wide directories — there's no per-user extension point. Adding a custom applet means dropping files into system directories (via package install or root).

But D-Bus *itself* is a per-user extension point. A user session D-Bus daemon runs for each login, and any process can register names on it. The `StatusNotifierItem` protocol used by [Ayatana Indicators](https://www.linux.com/news/ayatana/) works over session D-Bus — no system-wide registration needed. That's the key insight: the MATE "Add to Panel" directory scan is a system-wide mechanism, but the indicator tray is a per-user D-Bus rendezvous.

("Ayatana" is a Buddhist term for "sense base" or "sense sphere" — Canonical chose it circa 2009 for their UX improvement initiative, of which the indicator framework was a part. When upstream maintenance lapsed, Debian/X2Go folks [forked the indicator libraries under the same name](https://sunweavers.net/blog/node/58) to keep them desktop-agnostic.)

(Ayatana Indicators offer a simpler path: a Python script using `AppIndicator3` / `AyatanaAppIndicator3` that registers a `StatusNotifierItem` via D-Bus. The MATE indicator applet picks it up automatically — no applet registration needed, no root. See [`opencode-indicator.py`](../dotfiles/bin/opencode-indicator.py). For context, [PR #251](https://github.com/dckc/madmode-blog/pull/251) bundles this with the ~2800:1-smaller notification binary from [a tiny XDG notifier using zig](/2026/notify-fun/).)

## Approaches

| Approach | Registration | Root? | Complexity |
|---|---|---|---|
| MATE panel applet | `/usr/share/mate-panel/applets/*.mate-panel-applet` | yes (or package) | high (C/Python + D-Bus service) |
| Ayatana indicator | None (auto via D-Bus `StatusNotifierItem`) | no | low (~50 LOC Python) |
| Raw XEmbed tray | `_NET_SYSTEM_TRAY` | no | medium (legacy, not well-supported) |
| Nyx (existing tool) | systemd user service | no | pre-built, full service manager |