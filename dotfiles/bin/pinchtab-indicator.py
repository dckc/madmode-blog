#!/usr/bin/python3
"""
Ayatana indicator for `pinchtab`.

Registers a StatusNotifierItem on the session D-Bus — the MATE indicator
applet (or any StatusNotifierHost) picks it up.
Right-click menu: Quit.

Prereq:  apt install gir1.2-ayatanaappindicator3-0.1 python3-gi
Install: make -C dotfiles -f pinchtab-indicator.mk
"""

from __future__ import annotations

import logging
import os

import gi

gi.require_version("Gtk", "3.0")

try:
    gi.require_version("AyatanaAppIndicator3", "0.1")
    from gi.repository import AyatanaAppIndicator3 as AppIndicator
except (ValueError, ImportError):
    gi.require_version("AppIndicator3", "0.1")
    from gi.repository import AppIndicator3 as AppIndicator
from gi.repository import Gtk

LABEL = "pt"
_SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
ICON = os.path.join(_SCRIPT_DIR, "..", "icons", "pinchtab.png")


class Monitor:
    def __init__(self):
        self._indicator = AppIndicator.Indicator.new(
            LABEL,
            ICON,
            AppIndicator.IndicatorCategory.APPLICATION_STATUS,
        )
        self._indicator.set_status(AppIndicator.IndicatorStatus.ACTIVE)
        self._build_menu()

    def _build_menu(self):
        menu = Gtk.Menu()

        item_quit = Gtk.MenuItem(label="Quit")
        item_quit.connect("activate", lambda _: Gtk.main_quit())
        menu.append(item_quit)

        menu.show_all()
        self._indicator.set_menu(menu)

    def run(self):
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
