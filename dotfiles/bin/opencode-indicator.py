#!/usr/bin/python3
"""
Ayatana indicator for `opencode web` as a systemd user service.

Registers a StatusNotifierItem on the session D-Bus — the MATE indicator
applet (or any StatusNotifierHost) picks it up.  Polls systemd every 2 s.
Right-click menu: Start, Stop, Copy URL, Open in Browser, Quit.

Prereq:  apt install gir1.2-ayatanaappindicator3-0.1 python3-gi
Service: dotfiles/systemd/user/opencode-web.service
Install: make -C dotfiles -f opencode-indicator.mk
"""

from __future__ import annotations

import logging
import os
import subprocess
from pathlib import Path

import gi

gi.require_version("Gtk", "3.0")

try:
    gi.require_version("AyatanaAppIndicator3", "0.1")
    from gi.repository import AyatanaAppIndicator3 as AppIndicator
except (ValueError, ImportError):
    gi.require_version("AppIndicator3", "0.1")
    from gi.repository import AppIndicator3 as AppIndicator

from gi.repository import GLib, Gtk

LABEL = "ai"
UNIT = "opencode-web"
_SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
ICON = os.path.join(_SCRIPT_DIR, "..", "icons", "opencode.svg")
URL = os.environ.get("OPENCODE_URL", "http://127.0.0.1:3000")

CLIP_CMDS = ["xclip", "-selection", "clipboard"], ["wl-copy"]


class Monitor:
    def __init__(self):
        self._active = False
        self._indicator = AppIndicator.Indicator.new(
            LABEL,
            ICON,
            AppIndicator.IndicatorCategory.APPLICATION_STATUS,
        )
        self._indicator.set_status(AppIndicator.IndicatorStatus.ACTIVE)
        self._build_menu()
        GLib.timeout_add(2000, self._poll)

    def _build_menu(self):
        menu = Gtk.Menu()

        self._item_start = Gtk.MenuItem(label="Start")
        self._item_start.connect("activate", lambda _: self._systemctl("start"))
        menu.append(self._item_start)

        self._item_stop = Gtk.MenuItem(label="Stop")
        self._item_stop.connect("activate", lambda _: self._systemctl("stop"))
        menu.append(self._item_stop)

        menu.append(Gtk.SeparatorMenuItem())

        item_open = Gtk.MenuItem(label="Open in Browser")
        item_open.connect("activate", lambda _: self._open_url())
        menu.append(item_open)

        item_copy = Gtk.MenuItem(label="Copy URL")
        item_copy.connect("activate", lambda _: self._copy_url())
        menu.append(item_copy)

        menu.append(Gtk.SeparatorMenuItem())

        item_quit = Gtk.MenuItem(label="Quit")
        item_quit.connect("activate", lambda _: Gtk.main_quit())
        menu.append(item_quit)

        menu.show_all()
        self._indicator.set_menu(menu)

    def _systemctl(self, action):
        subprocess.run(["systemctl", "--user", action, f"{UNIT}.service"])

    def _systemctl_is_active(self) -> bool:
        r = subprocess.run(
            ["systemctl", "--user", "is-active", f"{UNIT}.service"],
            capture_output=True,
            text=True,
        )
        return r.stdout.strip() == "active"

    def _open_url(self):
        subprocess.run(["xdg-open", URL])

    def _copy_url(self):
        for cmd in CLIP_CMDS:
            try:
                subprocess.run([*cmd], input=URL, text=True, check=True)
                return
            except FileNotFoundError:
                continue
        logging.error("no clipboard tool found (tried xclip, wl-copy)")

    def _set_ui(self, active: bool):
        self._active = active
        self._item_start.set_sensitive(not active)
        self._item_stop.set_sensitive(active)
        label = f"{LABEL}\u2713" if active else f"{LABEL}\u2717"
        self._indicator.set_label(label, "")
        self._indicator.set_title(label)

    def _poll(self):
        self._set_ui(self._systemctl_is_active())
        return True

    def run(self):
        self._poll()
        Gtk.main()


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(message)s",
        datefmt="%H:%M:%S",
    )
    Monitor().run()


if __name__ == "__main__":
    raise SystemExit(main())
