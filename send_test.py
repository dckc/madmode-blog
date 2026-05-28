#!/usr/bin/env python3
"""Send a test D-Bus notification over a raw Unix socket, verify reply."""

import socket, struct, sys, time

def main():
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.settimeout(5)
    sock.connect("/run/user/1000/bus")

    # SASL with FD negotiation (matching libdbus)
    sock.sendall(b"\x00AUTH EXTERNAL 31303030\r\nNEGOTIATE_UNIX_FD\r\nBEGIN\r\n")
    time.sleep(0.3)
    try:
        sock.settimeout(2)
        while True:
            d = sock.recv(4096)
            if not d:
                break
    except socket.timeout:
        pass

    # Hello
    hello = open("hello.bin", "rb").read()
    sock.sendall(hello)
    time.sleep(0.2)
    hr = sock.recv(4096)
    if len(hr) < 16 or hr[1] != 2:
        print(f"Hello failed: type={hr[1]}, len={len(hr)}", file=sys.stderr)
        return 1
    print(f"Hello: OK (got unique name)", file=sys.stderr)

    # Notify
    notify = open("notify.bin", "rb").read()
    sock.sendall(notify)
    time.sleep(0.5)
    try:
        sock.settimeout(3)
        nr = sock.recv(4096)
        if nr and nr[1] == 2:
            bl = struct.unpack_from('<I', nr, 4)[0]
            fl = struct.unpack_from('<I', nr, 12)[0]
            bo = ((16 + fl + 7) // 8) * 8
            nid = struct.unpack_from('<I', nr, bo)[0]
            print(f"Notify: OK (id={nid})", file=sys.stderr)
            return 0
        else:
            print(f"Notify: FAILED (type={nr[1] if nr else 'N/A'})", file=sys.stderr)
            return 1
    except socket.timeout:
        print("Notify: TIMEOUT", file=sys.stderr)
        return 1
    finally:
        sock.close()

if __name__ == "__main__":
    sys.exit(main())
