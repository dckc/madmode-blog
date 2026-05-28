const std = @import("std");
const linux = std.os.linux;

pub fn main() void {
    const fd_signed = linux.socket(linux.AF.UNIX, linux.SOCK.STREAM, 0);
    if (fd_signed < 0) return;
    const fd = @as(i32, @intCast(fd_signed));
    defer _ = linux.close(fd);

    var addr: linux.sockaddr.un = .{
        .family = linux.AF.UNIX,
        .path = [1]u8{0} ** 108,
    };
    const path = "/run/user/1000/bus";
    @memcpy(addr.path[0..path.len], path);

    const addr_ptr = @as(*const linux.sockaddr, @ptrCast(&addr));
    const addr_len = @as(linux.socklen_t, @intCast(@sizeOf(linux.sa_family_t) + path.len));
    if (linux.connect(fd, addr_ptr, addr_len) < 0) return;

    var buf: [4096]u8 = undefined;

    // Phase 1: SASL authentication
    const sasl = "\x00AUTH EXTERNAL 31303030\r\nNEGOTIATE_UNIX_FD\r\nBEGIN\r\n";
    _ = linux.write(fd, sasl.ptr, sasl.len);
    _ = linux.read(fd, &buf, buf.len);

    // Phase 2: Hello (register with D-Bus daemon)
    const hello_payload = @embedFile("hello.bin");
    _ = linux.write(fd, hello_payload.ptr, hello_payload.len);
    const hello_n = linux.read(fd, &buf, buf.len);
    _ = hello_n;

    // Phase 3: Send notification
    const notify_payload = @embedFile("notify.bin");
    _ = linux.write(fd, notify_payload.ptr, notify_payload.len);

    // Wait for reply before closing
    const ts = linux.timespec{ .sec = 0, .nsec = 500 * 1000 * 1000 };
    _ = linux.nanosleep(&ts, null);
    _ = linux.read(fd, &buf, buf.len);
}
