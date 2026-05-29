"""
Generate or verify D-Bus Notify payload fixtures.

Uses jeepney v0.9.0, 2025-02-27, by Thomas Kluyver.
https://jeepney.readthedocs.io/en/latest/

Notify method signature "susssasa{sv}i": Desktop Notifications Specification,
v1.3, 2024-08-18, §2 Basic Design.
https://specifications.freedesktop.org/notification/latest/

Patterns derived from libnotify test suite (LGPL-2.1-or-later),
https://gitlab.gnome.org/GNOME/libnotify/-/tree/master/tests/

Usage:
  python3 test/notify_fixtures.py          # generate .bin files
  python3 test/notify_fixtures.py check    # verify .bin files match
"""

import logging
import sys

from jeepney import new_method_call, DBusAddress, Message as ParsedMsg

NOTIFY_ADDR = DBusAddress(
    object_path="/org/freedesktop/Notifications",
    bus_name="org.freedesktop.Notifications",
    interface="org.freedesktop.Notifications",
)

# Each entry: name -> (body_tuple, serial)
BODIES = {

    "libnotify-basic-long-summary": (
        ("Basics", 0, "",
         "Summary that is very long 8374983278r32j4 rhjjfh dw8f 43jhf 8ds7 "
         "ur2389f jdbjkt h8924yf jkdbjkt 892hjfiHER98HEJIF BDSJHF hjdhF JKLH "
         "890YRHEJHFU 89HRJKSHdd dddd ddddd dddd ddddd dddd ddddd dddd dddd "
         "ddd ddd dddd Fdd d ddddd dddddddd ddddddddhjkewdkjsjfjk sdhkjf hdkj "
         "dadasdadsa adsd asd sd saasd fadskfkhsjf hsdkhfkshfjkhsd kjfhsjdkhfj "
         "ksdhfkjshkjfsd sadhfjkhaskd jfhsdajkfhkjs dhfkjsdhfkjs adhjkfhasdkj "
         "fhdsakjhfjk asdhkjkfhd akfjshjfsk afhjkasdhf jkhsdaj hf kjsdfahkfh "
         "sakjhfksdah kfdashkjf ksdahfj shdjdh",
         "Content", [], {}, 3000), 1),

    "libnotify-basic-long-body": (
        ("Basics", 0, "",
         "Summary",
         "Content that is very long 8374983278r32j4 rhjjfh dw8f 43jhf 8ds7 "
         "ur2389f jdbjkt h8924yf jkdbjkt 892hjfiHER98HEJIF BDSJHF hjdhF JKLH "
         "890YRHEJHFU 89HRJKSHdd dddd ddddd dddd ddddd dddd ddddd dddd dddd "
         "ddd ddd dddd Fdd d ddddd dddddddd ddddddddhjkewdkjsjfjk sdhkjf hdkj "
         "dadasdadsa adsd asd sd saasd fadskfkhsjf hsdkhfkshfjkhsd kjfhsjdkhfj "
         "ksdhfkjshkjfsd sadhfjkhaskd jfhsdajkfhkjs dhfkjsdhfkjs adhjkfhasdkj "
         "fhdsakjhfjk asdhkjkfhd akfjshjfsk afhjkasdhf jkhsdaj hf kjsdfahkfh "
         "sakjhfksdah kfdashkjf ksdahfj shdjdh",
         [], {}, 3000), 2),

    "libnotify-basic-summary-only": (
        ("Basics", 0, "",
         "Summary only there is no message content",
         "", [], {}, 0), 3),

    "libnotify-urgency-low": (
        ("Urgency", 0, "",
         "Low Urgency", "Joe signed online.",
         [], {"urgency": ("y", 0)}, -1), 4),

    "libnotify-urgency-normal": (
        ("Urgency", 0, "",
         "Normal Urgency", "You have a meeting in 10 minutes.",
         [], {"urgency": ("y", 1)}, -1), 5),

    "libnotify-urgency-critical": (
        ("Urgency", 0, "",
         "Critical Urgency",
         "This message will self-destruct in 10 seconds.",
         [], {"urgency": ("y", 2)}, 10000), 6),

    "libnotify-transient": (
        ("Transient Test", 0, "audio-volume-medium",
         "Some transient change", "Something happened",
         [], {"transient": ("b", True)}, -1), 7),

    "libnotify-default-action": (
        ("Default Action Test", 0, "",
         "Matt is online", "",
         ["default", "Do Default Action"],
         {"category": ("s", "presence.online")}, -1), 8),

    "libnotify-markup": (
        ("Markup", 0, "",
         "Summary",
         "Some <b>bold</b>, <u>underlined</u>, <i>italic</i>, "
         "<a href='http://www.google.com'>linked</a> text",
         [], {}, 3000), 9),

    "libnotify-multi-actions": (
        ("Multi Action Test", 0, "drive-harddisk-symbolic",
         "Low disk space",
         "You can free up some disk space by emptying the trash can.",
         ["help", "Help", "ignore", "Ignore", "empty", "Empty Trash"],
         {"transient": ("b", True), "urgency": ("y", 2),
          "category": ("s", "device")}, -1), 10),

    "libnotify-action-icons": (
        ("Action Icon Test", 0, "",
         "Music Player", "Some solid funk",
         ["media-skip-backward", "Previous",
          "media-playback-pause", "Pause",
          "media-skip-forward", "Next"],
         {"action-icons": ("b", True)}, -1), 11),

    "libnotify-resident": (
        ("Resident Test", 0, "audio-x-generic",
         "Music Player", "Playing some fine song",
         ["previous", "Previous", "pause", "Pause", "next", "Next"],
         {"resident": ("b", True)}, -1), 12),

    "libnotify-persistence": (
        ("Persistence Test", 0, "software-update-available-symbolic",
         "Software Updates Available",
         "Important updates for your apps are now available.",
         ["install", "Install now"],
         {}, 0), 13),

    "libnotify-xy": (
        ("XY", 0, "",
         "X, Y Test", "This notification should point to 150, 10",
         [], {"x": ("i", 150), "y": ("i", 10)}, -1), 14),

    "libnotify-replace-first": (
        ("Replace Test", 0, "",
         "Summary", "First message",
         [], {}, 0), 15),

    "libnotify-replace-second": (
        ("Replace Test", 0, "",
         "Second Summary", "First mesage was replaced",
         [], {}, -1), 16),

    "chat-message": (
        ("Slack", 0, "slack",
         "Alice", "What do you think about the proposal?",
         ["reply", "Reply", "mark_read", "Mark Read"],
         {"category": ("s", "im.received"),
          "sound-name": ("s", "message-new-instant")}, -1), 17),

    "email-arrival": (
        ("Thunderbird", 0, "thunderbird",
         "New mail from Bob",
         "Meeting tomorrow at 3pm in the conference room.",
         ["reply", "Reply", "archive", "Archive"],
         {"category": ("s", "email.arrived")}, 8000), 18),

    "battery-critical": (
        ("GNOME Shell", 0, "battery-caution-charging-symbolic",
         "Battery Critical", "10% remaining — plug in now.",
         [], {"urgency": ("y", 2), "resident": ("b", True)}, 0), 19),

    "download-complete": (
        ("Firefox", 0, "firefox",
         "Download complete",
         "notify-fun-0.1.0.tar.gz (2.4 MB) — 100%",
         [], {"category": ("s", "transfer.complete")}, 5000), 20),

    "network-disconnected": (
        ("NetworkManager", 0, "network-offline-symbolic",
         "Connection lost", "You are no longer connected to the internet.",
         [], {"category": ("s", "network.disconnected"),
              "urgency": ("y", 1)}, -1), 21),
}


def _build_notify(body, serial=1):
    msg = new_method_call(NOTIFY_ADDR, "Notify", "susssasa{sv}i", body)
    return msg.serialise(serial=serial)


def _gen(fixtures_dir):
    fixtures_dir.mkdir(parents=True, exist_ok=True)
    for name, (body, serial) in BODIES.items():
        data = _build_notify(body, serial=serial)
        (fixtures_dir / f"{name}.bin").write_bytes(data)
        parsed = ParsedMsg.from_buffer(data)
        assert parsed.body == body, f"{name}: body mismatch"
        logging.info("%-40s %4d bytes  OK", name, len(data))


def _check(fixtures_dir):
    bin_files = sorted(fixtures_dir.glob("*.bin"))
    if not bin_files:
        logging.error("No .bin fixtures found in %s", fixtures_dir)
        return False

    all_ok = True
    for bf in bin_files:
        name = bf.stem
        if name not in BODIES:
            logging.warning("%s: not in BODIES, skipping", name)
            continue
        body, serial = BODIES[name]
        disk_bytes = bf.read_bytes()
        built_bytes = _build_notify(body, serial=serial)
        if disk_bytes == built_bytes:
            logging.info("%-40s %4d bytes  OK", name, len(disk_bytes))
        else:
            min_len = min(len(disk_bytes), len(built_bytes))
            for i in range(min_len):
                if disk_bytes[i] != built_bytes[i]:
                    logging.error("%s: byte mismatch at offset %d "
                                  "(0x%02x vs 0x%02x)", name, i,
                                  disk_bytes[i], built_bytes[i])
                    break
            if len(disk_bytes) != len(built_bytes):
                logging.error("%s: size mismatch (disk=%d built=%d)",
                              name, len(disk_bytes), len(built_bytes))
            all_ok = False

    return all_ok


def main(out_dir, mode):
    out_dir = out_dir / "test" / "fixtures"

    if mode == "gen":
        _gen(out_dir)
    elif mode == "check":
        ok = _check(out_dir)
        if ok:
            logging.info("All fixtures OK")
            return 0
        else:
            logging.error("Some fixtures FAILED")
            return 1
    else:
        logging.error("Unknown mode: %s (use 'gen' or 'check')", mode)
        return 1


if __name__ == "__main__":
    def _script_io():
        from pathlib import Path

        logging.basicConfig(level=logging.INFO, format="%(message)s")
        mode = sys.argv[1] if len(sys.argv) > 1 else "gen"
        return main(out_dir=Path.cwd(), mode=mode)

    raise SystemExit(_script_io())
