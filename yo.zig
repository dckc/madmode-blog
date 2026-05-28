const std = @import("std");
const linux = std.os.linux;

pub fn main() void {
    // 1. Create the raw Unix socket
    const fd_signed = linux.socket(linux.AF.UNIX, linux.SOCK.STREAM, 0);
    if (fd_signed < 0) return;
    const fd = @as(i32, @intCast(fd_signed));
    defer _ = linux.close(fd);

    // 2. Manually construct the Linux sockaddr_un struct
    // Linux defines sockaddr_un as: { sa_family_t sun_family; char sun_path[108]; }
    var addr: linux.sockaddr.un = .{
        .family = linux.AF.UNIX,
        .path = [1]u8{0} ** 108, // Initialize path buffer with null bytes
    };

    // Copy our socket path into the struct
    const path = "/run/user/1000/bus";
    @memcpy(addr.path[0..path.len], path);

    // 3. Connect via raw Linux syscall
    const addr_ptr = @as(*const linux.sockaddr, @ptrCast(&addr));
    const addr_len = @as(linux.socklen_t, @intCast(@sizeOf(linux.sa_family_t) + path.len));
    const connect_rc = linux.connect(fd, addr_ptr, addr_len);
    if (connect_rc < 0) return;

    // 4. Write raw bytes via raw Linux syscall
    const dbus_payload = "YOUR_RAW_DBUS_WIRE_BYTES_HERE";
    _ = linux.write(fd, dbus_payload.ptr, dbus_payload.len);
}
