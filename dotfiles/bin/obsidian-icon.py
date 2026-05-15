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
    """Pack RGBA image into _NET_WM_ICON CARDINAL array.

    Each pixel becomes one 32-bit ARGB CARDINAL, not four byte-sized
    CARDINALs.  For a 2x2 image the result has 2 (header) + 4 (pixels)
    = 6 elements.  The buggy encoding (raw bytes as CARDINALs) gives 18.

    >>> from PIL import Image
    >>> img = Image.new('RGBA', (2, 2), (255, 0, 0, 255))
    >>> data = encode_icon(img, 2)
    >>> len(data)
    6
    >>> data[:2]
    [2, 2]
    """
    pixels = img.getdata()
    data = [size, size]
    for r, g, b, a in pixels:
        data.append((a << 24) | (r << 16) | (g << 8) | b)
    return data


def main(files, environ, x11):
    # TODO: consider opts for WM_CLASS, icon size

    display_name = environ.get("DISPLAY")
    if display_name is None:
        logging.error("DISPLAY not set; is X11 running?")
        return 1

    xdpy = x11(display_name)

    img = Image.open(files / _ICON_PATH)
    if img.size != (48, 48):
        img = img.resize((48, 48), Image.LANCZOS)
    if img.mode != "RGBA":
        img = img.convert("RGBA")

    icon_data = encode_icon(img, 48)

    count = set_window_icon(xdpy, "obsidian", icon_data)
    if count == 0:
        logging.warning("no window found matching 'obsidian'")
        return 1


def set_window_icon(xdpy, wm_class, icon_data):
    root = xdpy.screen().root

    atom = xdpy.intern_atom("_NET_WM_ICON")
    cardinal = xdpy.intern_atom("CARDINAL")

    client_list_prop = root.get_full_property(
        xdpy.intern_atom("_NET_CLIENT_LIST"), X.AnyPropertyType
    )
    if client_list_prop is None:
        msg = "no _NET_CLIENT_LIST on root window; is a window manager running?"
        raise RuntimeError(msg)

    found = 0
    for wid in client_list_prop.value:
        window = xdpy.create_resource_object("window", wid)
        cls = window.get_wm_class()
        if cls is not None and (cls[0] == wm_class or cls[1] == wm_class):
            window.change_property(atom, cardinal, 32, icon_data)
            found += 1

    xdpy.sync()
    logging.info("set icon on %d window(s) matching '%s'", found, wm_class)
    return found


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
