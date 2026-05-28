"""Generate D-Bus message payloads for Hello and Notify method calls.

Hello method: D-Bus Specification v0.43, 2024-10-29, §3.3.1 org.freedesktop.DBus.
https://dbus.freedesktop.org/doc/dbus-specification.html

Notify method signature "susssasa{sv}i": Desktop Notifications Specification,
v1.3, 2024-08-18, §2 Basic Design.
https://specifications.freedesktop.org/notification/latest/
"""

from dbus_msg import new_method_call, DBusAddress, Message
import logging


def build_hello_payload():
    addr = DBusAddress(
        object_path="/org/freedesktop/DBus",
        bus_name="org.freedesktop.DBus",
        interface="org.freedesktop.DBus",
    )
    msg = new_method_call(addr, "Hello")
    return msg.serialise(serial=1)


def build_notify_payload():
    addr = DBusAddress(
        object_path="/org/freedesktop/Notifications",
        bus_name="org.freedesktop.Notifications",
        interface="org.freedesktop.Notifications",
    )
    body = ("tiny-notify", 0, "", "CI Failed!", "Your build broke.", [], {}, -1)
    msg = new_method_call(addr, "Notify", "susssasa{sv}i", body)
    return msg.serialise(serial=2)


def validate_hello(data):
    h = Message.from_buffer(data)
    return (
        h.header.fields[1] == "/org/freedesktop/DBus"
        and h.header.fields[6] == "org.freedesktop.DBus"
    )


def validate_notify(data):
    n = Message.from_buffer(data)
    return (
        n.header.fields[1] == "/org/freedesktop/Notifications"
        and n.body == ("tiny-notify", 0, "", "CI Failed!", "Your build broke.", [], {}, -1)
    )


def main(out_dir):
    hello_pkt = build_hello_payload()
    notify_pkt = build_notify_payload()

    (out_dir / "hello.bin").write_bytes(hello_pkt)
    (out_dir / "notify.bin").write_bytes(notify_pkt)

    logging.info("Hello: %s bytes", len(hello_pkt))
    logging.info("Notify: %s bytes", len(notify_pkt))

    assert validate_hello(hello_pkt)
    assert validate_notify(notify_pkt)
    logging.info("Validation OK")


if __name__ == "__main__":
    def _script_io():
        from pathlib import Path

        logging.basicConfig(level=logging.INFO, format="%(message)s")
        main(out_dir=Path.cwd())
        return 0

    raise SystemExit(_script_io())
