const std = @import("std");
const linux = std.os.linux;
const gen = @import("./generate_payload.zig");

fn parseReplyId(data: []const u8) u32 {
    const field_len = std.mem.readInt(u32, data[12..16], .little);
    const body_off = ((16 + field_len + 7) / 8) * 8;
    return std.mem.readInt(u32, data[body_off..][0..4], .little);
}

const DBusSock = struct {
    fd: i32,
    buf: [4096]u8,

    fn authenticate(self: *DBusSock) void {
        const sasl = "\x00AUTH EXTERNAL 31303030\r\nNEGOTIATE_UNIX_FD\r\nBEGIN\r\n";
        _ = linux.write(self.fd, sasl.ptr, sasl.len);
        const tv = linux.timeval{ .sec = 2, .usec = 0 };
        _ = linux.setsockopt(self.fd, linux.SOL.SOCKET, linux.SO.RCVTIMEO, @ptrCast(&tv), @sizeOf(linux.timeval));
        while (true) {
            const n = linux.read(self.fd, &self.buf, self.buf.len);
            if (n == 0 or n > self.buf.len) break;
        }
    }

    fn sendMessage(self: *DBusSock, payload: []const u8) ?[]u8 {
        _ = linux.write(self.fd, payload.ptr, payload.len);
        const n = linux.read(self.fd, &self.buf, self.buf.len);
        if (n == 0 or n > self.buf.len) return null;
        return self.buf[0..n];
    }
};

pub fn main() void {
    const fd_signed = linux.socket(linux.AF.UNIX, linux.SOCK.STREAM, 0);
    if (fd_signed < 0) return;
    const fd = @as(i32, @intCast(fd_signed));
    defer _ = linux.close(fd);

    var addr: linux.sockaddr.un = .{
        .family = linux.AF.UNIX,
        .path = [1]u8{0} ** 108,
    };
    const bus_path = "/run/user/1000/bus";
    @memcpy(addr.path[0..bus_path.len], bus_path);

    const addr_ptr = @as(*const linux.sockaddr, @ptrCast(&addr));
    const addr_len = @as(linux.socklen_t, @intCast(@sizeOf(linux.sa_family_t) + bus_path.len));
    if (linux.connect(fd, addr_ptr, addr_len) < 0) return;

    var dbus = DBusSock{ .fd = fd, .buf = undefined };
    dbus.authenticate();

    const hello_payload = comptime gen.buildHello();
    const hr = dbus.sendMessage(hello_payload);
    if (hr == null or hr.?.len < 16 or hr.?[1] != 2) return;

    const notify_payload = comptime gen.buildNotify();
    const nr = dbus.sendMessage(notify_payload);
    if (nr == null or nr.?.len < 16 or nr.?[1] != 2) return;
    const nid = parseReplyId(nr.?);
    _ = nid;
}
