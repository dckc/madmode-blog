# ocaml-notify

A minimal XDG desktop notifier written in pure OCaml. It speaks just enough
D-Bus over a Unix socket to call `org.freedesktop.Notifications.Notify` —
no external libraries beyond the standard `Unix` module.

## Usage

```sh
# build a native binary
ocamlopt unix.cmxa -o notify-bin notify.ml

# run the binary
./notify-bin "your message here"

# or run with the OCaml interpreter
ocaml unix.cma notify.ml -- "your message here"
```

## Dev environment

A Nix flake provides the OCaml toolchain:

```sh
nix develop
```

This drops you into a shell with `ocaml`, `ocamlopt`, `dune`, and `utop`.

## How it works

1. Connects to the session bus at `/run/user/<uid>/bus`.
2. Performs the SASL `AUTH EXTERNAL` handshake.
3. Sends a `Hello` method call to `org.freedesktop.DBus`.
4. Sends a `Notify` method call to `org.freedesktop.Notifications` with the
   message as the body.

The D-Bus wire format is built by hand (little-endian, header fields aligned
to 8 bytes, body aligned to 8). See the `notify-project` branch for the
reference implementation in Python/Zig and the D-Bus spec pointers.
