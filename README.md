---
title: a tiny XDG notifier using zig comptime and syscalls
tags:
  - zig
  - linux
  - protocols
  - performance
  - capabilities
date: 2026-05-28
published: true
summary: what's the least authority needed to send a desktop notification?
---

[notify-send](https://man.archlinux.org/man/notify-send.1) needs 9.1 MB of shared libraries and 416 syscalls to pop up a notification. Can we do better? Could we write one with the *least authority* needed — nothing but the D-Bus protocol over a Unix socket? a few assembly instructions? does rust or zig let me build a binary that has nothing else? any other languages? nim?

[zig](https://en.wikipedia.org/wiki/Zig_(programming_language)) fits like a glove for a couple reasons:
1. "On Linux libc can be side-stepped by using `std.os.linux` directly." -- [os.zig](https://github.com/ziglang/zig/blob/master/lib/std/os.zig) [^1]
2. [comptime](https://zig.guide/language-basics/comptime/) lets us omit message building code at runtime.

## syscalls: 17 vs 416

It makes 17 syscalls, 5 of which are zig runtime setup:

```
$ make trace
strace ./yo
execve("./yo", ["./yo"], 0x7ffd48138640 /* 160 vars */) = 0
mmap(NULL, 262176, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x75624f3d8000
arch_prctl(ARCH_SET_FS, 0x75624f418000) = 0
prlimit64(0, RLIMIT_STACK, NULL, {rlim_cur=8192*1024, rlim_max=RLIM64_INFINITY}) = 0
prlimit64(0, RLIMIT_STACK, {rlim_cur=16384*1024, rlim_max=RLIM64_INFINITY}, NULL) = 0
sigaltstack({ss_sp=0x75624f3d8000, ss_flags=0, ss_size=262144}, NULL) = 0
socket(AF_UNIX, SOCK_STREAM, 0)         = 3
connect(3, {sa_family=AF_UNIX, sun_path="/run/user/1000/bus"}, 20) = 0
write(3, "\0AUTH EXTERNAL 31303030\r\nNEGOTIA"..., 51) = 51
setsockopt(3, SOL_SOCKET, SO_RCVTIMEO_OLD, "\2\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0", 16) = 0
read(3, "OK b4f1cb3ecbcde86fd0f50bf16a162"..., 4096) = 52
read(3, 0x7ffe232c87f8, 4096)           = -1 EAGAIN (Resource temporarily unavailable)
write(3, "l\1\0\1\0\0\0\0\1\0\0\0m\0\0\0\1\1o\0\25\0\0\0/org/fre"..., 128) = 128
read(3, "l\2\1\1\v\0\0\0\1\0\0\0=\0\0\0\6\1s\0\6\0\0\0:1.419\0\0"..., 4096) = 262
write(3, "l\1\0\1T\0\0\0\2\0\0\0\233\0\0\0\1\1o\0\36\0\0\0/org/fre"..., 260) = 260
read(3, "l\2\1\1\4\0\0\0\35\0\0\0/\0\0\0\6\1s\0\6\0\0\0:1.419\0\0"..., 4096) = 68
close(3)                                = 0
exit_group(0)                           = ?
+++ exited with 0 +++
```

compare with `notify-send` trace:

```
$ wc *.trace
  418  2459 29020 notify-send.trace
   19   112  1284 yo.trace
```

Why so many syscalls? Because `notify-send` isn't one binary — it's a gateway to a shared library dependency tree:

```
$ ldd $(type -p notify-send)
    linux-vdso.so.1
    libnotify.so.4       → libgobject-2.0 → libglib-2.0
    libgdk_pixbuf-2.0    → libpng, libjpeg
    libgio-2.0           → libmount, libblkid, libselinux
    libpcre2-8, libffi, libz, libm, libc
```

**9.1 MB** of shared libraries loaded to pop up "Your build broke." Every one of those `.so` files carries ambient authority — filesystem access via libmount, image decoding via libpng/libjpeg, SELinux policy enforcement. You'd need to audit all 9.1 MB before handing this binary to untrusted code.

`yo-strip` is **3.3 KB**. Static. No libraries. 17 syscalls, all documented above. It's a single-purpose capability: "you may send a D-Bus notification, nothing else." Small enough to ship inside a [bubblewrap](https://github.com/containers/bubblewrap) sandbox as a confined [Endo](https://endojs.org) capability for AI agents.

## message building

yay for [jeepney](https://jeepney.readthedocs.io/) and sans-io! `generate_payload.py` is <50 LOC[^2].

Then I replaced the jeepney 

`dbus_msg.py` - just enough jeepny

Translation to zig is straightforward. The magic is **comptime**:

```zig
    const hello_payload = comptime gen.buildHello();
...
    const notify_payload = comptime gen.buildNotify();
```

## dbus protocol: Hello, ...

For debugging the dbus protocol, I soon realized zig was not the right tool. But `send_test.py` does the `Hello` handshake and such in under 100 LOC[^3].

After that, again, translation to `zig` is straightforward. All told:

| Module                    | Python | Zig |
| ------------------------- | ------ | --- |
| `dbus_msg`                | 352    | 228 |
| `generate_payload`        | 75     | 74  |
| `yo.zig` / `send_test.py` | 94     | 71  |
## bloaty - not!

`yo-strip` is 3304 B. What are they all for?

- **ELF headers + PHDR**: 568 B (17%) — OS loader
- **.text (code)**: 1103 B (33%) — actual machine code, broken into:
  - Zig runtime init: **595 B** (54% of .text) — aux-vector parsing, stack setup, mmap, init_array dispatch, TLS, exit
  - `main()`: **315 B** (29%) — socket, connect, authenticate, sendMessage ×2, reply parsing
  - `sendMessage()`: **72 B** (7%) — write+read wrapper
  - TLS init: **50 B** (5%)
  - `memset`: **28 B** (3%)
  - `memcpy`: **29 B** (3%)
  - `_start` entry: **14 B** (1%)
- **.rodata (payloads)**: 480 B (15%) — compiled D-Bus messages (hello 128 B, notify 260 B), SASL auth string, bus path
- **.eh_frame/.eh_frame_hdr**: 332 B (10%) — exception handling metadata (could be stripped)
- **Section headers**: 704 B (21%) — could be removed

The **Zig runtime init** dominates code size at 595 bytes — it's the freestanding crt0 equivalent. The actual application logic (`main` + `sendMessage`) is only 387 B.
[^1]: zig v0.16.0 2026-04 `24fdd5b7a4c1` nixpkgs `64c08a7ca051`

[^2]: excl comments, blank lines

[^3]: incl comments and all
