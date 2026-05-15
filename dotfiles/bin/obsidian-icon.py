#!/usr/bin/env python3
"""Set _NET_WM_ICON on X11 windows by WM_CLASS.

Obsidian (Electron) does not set _NET_WM_ICON on its X11 window, so the MATE
panel window list shows a generic icon instead of the application icon.  This
script reads the icon from a PNG file and sets _NET_WM_ICON on all windows
whose WM_CLASS matches the given class.
"""

from __future__ import annotations

import logging
from pathlib import Path

from PIL import Image
from Xlib import display, X

_ICON_PATH = "/usr/share/icons/hicolor/48x48/apps/obsidian.png"
# TODO: consider bundling a copy of the icon in dotfiles so the script
# doesn't depend on the system hicolor theme.  If the icon lives at
# ~/projects/madmode-blog/dotfiles/icons/obsidian.png then `files / "obsidian.png"`
# would work and _ICON_PATH plus the files / "/absolute/..." trick both vanish.


def encode_icon(img, size):
    """Convert any image to _NET_WM_ICON CARDINAL array.

    Resizes to ``size``, converts to RGBA, then packs each pixel as one
    32-bit ARGB CARDINAL.  For a 2x2 image the result has 2 (header) + 4
    (pixels) = 6 elements.  The buggy encoding (raw bytes as CARDINALs)
    gives 18.

    >>> from PIL import Image
    >>> img = Image.new('RGBA', (2, 2), (255, 0, 0, 255))
    >>> data = encode_icon(img, 2)
    >>> len(data)
    6
    >>> data[:2]
    [2, 2]
    """
    if img.size != (size, size):
        img = img.resize((size, size), Image.LANCZOS)
    if img.mode != "RGBA":
        img = img.convert("RGBA")
    pixels = img.getdata()
    data = [size, size]
    for r, g, b, a in pixels:
        data.append((a << 24) | (r << 16) | (g << 8) | b)
    return data


class Client:
    """An X11 client window identified by WM_CLASS.

    ``find()`` is the factory: it searches the root window's client list,
    captures matching window IDs, and returns a ``Client`` (or ``None``).
    The ``wm_class`` string lives only in ``find()`` — once constructed,
    a ``Client`` carries no forgeable string, only an X11 display and
    pre-identified window IDs.
    """

    def __init__(self, xdpy, window_ids):
        self.__xdpy = xdpy
        self.__window_ids = window_ids

    @staticmethod
    def find(xdpy, wm_class):
        root = xdpy.screen().root
        client_list_prop = root.get_full_property(
            xdpy.intern_atom("_NET_CLIENT_LIST"), X.AnyPropertyType
        )
        if client_list_prop is None:
            msg = "no _NET_CLIENT_LIST on root window; is a window manager running?"
            raise RuntimeError(msg)
        found = []
        for wid in client_list_prop.value:
            window = xdpy.create_resource_object("window", wid)
            cls = window.get_wm_class()
            if cls is not None and (cls[0] == wm_class or cls[1] == wm_class):
                found.append(wid)
        if not found:
            return None
        return Client(xdpy, found)

    def set_icon(self, icon_data):
        atom = self.__xdpy.intern_atom("_NET_WM_ICON")
        cardinal = self.__xdpy.intern_atom("CARDINAL")
        for wid in self.__window_ids:
            window = self.__xdpy.create_resource_object("window", wid)
            window.change_property(atom, cardinal, 32, icon_data)
        self.__xdpy.sync()
        logging.info("set icon on %d window(s)", len(self.__window_ids))


def main(files, environ, x11):
    # TODO: consider opts for WM_CLASS, icon size

    display_name = environ.get("DISPLAY")
    if display_name is None:
        logging.error("DISPLAY not set; is X11 running?")
        return 1

    xdpy = x11(display_name)

    img = Image.open(files / _ICON_PATH)
    icon_data = encode_icon(img, 48)

    client = Client.find(xdpy, "obsidian")
    if client is None:
        logging.warning("no window found matching 'obsidian'")
        return 1
    client.set_icon(icon_data)


if __name__ == "__main__":
    def _script_io():
        from os import environ
        from pathlib import Path

        logging.basicConfig(level=logging.INFO, format="%(message)s")

        return main(
            files=Path.cwd(),
            environ=dict(environ),
            x11=display.Display,
        )

    raise SystemExit(_script_io())
