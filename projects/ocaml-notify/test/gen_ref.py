#!/usr/bin/env python3
"""Generate reference D-Bus payloads matching notify.ml's exact strings.

Uses the jeepney-free dbus_msg.py from the notify-project branch as an
independent oracle, so the OCaml hand-rolled serializer is checked against
a second implementation.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from dbus_msg import new_method_call, DBusAddress

def hello():
    addr = DBusAddress(
        object_path="/org/freedesktop/DBus",
        bus_name="org.freedesktop.DBus",
        interface="org.freedesktop.DBus",
    )
    return new_method_call(addr, "Hello").serialise(serial=1)

def notify(body_text):
    addr = DBusAddress(
        object_path="/org/freedesktop/Notifications",
        bus_name="org.freedesktop.Notifications",
        interface="org.freedesktop.Notifications",
    )
    body = ("ocaml-notify", 0, "", "ocaml-notify", body_text, [], {}, -1)
    return new_method_call(addr, "Notify", "susssasa{sv}i", body).serialise(serial=2)

def main(out):
    (out / "hello.bin").write_bytes(hello())
    (out / "notify.bin").write_bytes(notify("test"))
    print("wrote", out / "hello.bin", out / "notify.bin")

if __name__ == "__main__":
    main(pathlib.Path(__file__).parent)
