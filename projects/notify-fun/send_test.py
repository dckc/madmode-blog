# SPDX-FileCopyrightText: 2026 Dan Connolly
# SPDX-License-Identifier: Apache-2.0

"""Send a test D-Bus notification over a raw Unix socket, verify reply.

SASL AUTH EXTERNAL handshake: D-Bus Specification v0.43, 2024-10-29,
§2.4 Authentication (SASL profile).
https://dbus.freedesktop.org/doc/dbus-specification.html

Reply ID parsing (§2 Message Protocol — method return body layout).
"""

import struct
import logging
from socket import AF_UNIX, SOCK_STREAM, timeout as SocketTimeout


def parse_reply_id(data):
    bl = struct.unpack_from('<I', data, 4)[0]
    fl = struct.unpack_from('<I', data, 12)[0]
    bo = ((16 + fl + 7) // 8) * 8
    return struct.unpack_from('<I', data, bo)[0]


class DBusSock:
    def __init__(self, sock, sleep):
        self._sock = sock
        self._sleep = sleep

    def authenticate(self):
        self._sock.sendall(b"\x00AUTH EXTERNAL 31303030\r\nNEGOTIATE_UNIX_FD\r\nBEGIN\r\n")
        self._sleep(0.3)
        self._sock.settimeout(2)
        try:
            while self._sock.recv(4096):
                pass
        except SocketTimeout:
            pass

    def send_message(self, payload):
        self._sock.sendall(payload)
        self._sleep(0.5)
        self._sock.settimeout(3)
        try:
            return self._sock.recv(4096)
        except SocketTimeout:
            return None


def main(files, sleep, socket):
    hello_pkt = (files / "hello.bin").read_bytes()
    notify_pkt = (files / "notify.bin").read_bytes()

    sock = socket(AF_UNIX, SOCK_STREAM)
    try:
        sock.settimeout(5)
        sock.connect("/run/user/1000/bus")

        dbus = DBusSock(sock, sleep)
        dbus.authenticate()

        hr = dbus.send_message(hello_pkt)
        if hr is None or len(hr) < 16 or hr[1] != 2:
            logging.error("Hello: FAILED")
            return 1
        logging.info("Hello: OK")

        nr = dbus.send_message(notify_pkt)
        if nr is None:
            logging.error("Notify: TIMEOUT")
            return 1
        if nr[1] != 2:
            logging.error("Notify: FAILED")
            return 1
        nid = parse_reply_id(nr)
        logging.info("Notify: OK (id=%s)", nid)
        return 0
    finally:
        sock.close()


if __name__ == "__main__":
    def _script_io():
        from pathlib import Path
        import time
        import sys
        import socket

        logging.basicConfig(level=logging.INFO, format="%(message)s")

        return main(
            files=Path.cwd(),
            sleep=time.sleep,
            socket=socket.socket,
        )

    raise SystemExit(_script_io())
