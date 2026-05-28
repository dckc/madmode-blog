const std = @import("std");
const dbus = @import("dbus_msg.zig");

const hello_payload_inner = blk: {
    @setEvalBranchQuota(10000);
    var b = dbus.Buf{};
    b.serialise(
        dbus.MESSAGE_TYPE_METHOD_CALL,
        1,
        .{
            .{ .code = dbus.FIELD_PATH, .sig = "o", .val = "/org/freedesktop/DBus" },
            .{ .code = dbus.FIELD_INTERFACE, .sig = "s", .val = "org.freedesktop.DBus" },
            .{ .code = dbus.FIELD_MEMBER, .sig = "s", .val = "Hello" },
            .{ .code = dbus.FIELD_DESTINATION, .sig = "s", .val = "org.freedesktop.DBus" },
        },
        "",
        .{},
    );
    const len = b.off;
    var result: [len]u8 = undefined;
    @memcpy(&result, b.get());
    break :blk result;
};

const notify_payload_inner = blk: {
    @setEvalBranchQuota(10000);
    var b = dbus.Buf{};
    b.serialise(
        dbus.MESSAGE_TYPE_METHOD_CALL,
        2,
        .{
            .{ .code = dbus.FIELD_PATH, .sig = "o", .val = "/org/freedesktop/Notifications" },
            .{ .code = dbus.FIELD_INTERFACE, .sig = "s", .val = "org.freedesktop.Notifications" },
            .{ .code = dbus.FIELD_MEMBER, .sig = "s", .val = "Notify" },
            .{ .code = dbus.FIELD_DESTINATION, .sig = "s", .val = "org.freedesktop.Notifications" },
            .{ .code = dbus.FIELD_SIGNATURE, .sig = "g", .val = "susssasa{sv}i" },
        },
        "susssasa{sv}i",
        .{
            "tiny-notify",
            @as(u32, 0),
            "",
            "CI Failed!",
            "Your build broke.",
            [_][]const u8{},
            [_]struct {
                key: []const u8,
                value: struct { []const u8, u32 },
            }{},
            @as(i32, -1),
        },
    );
    const len = b.off;
    var result: [len]u8 = undefined;
    @memcpy(&result, b.get());
    break :blk result;
};

pub fn buildHello() []const u8 {
    return &hello_payload_inner;
}

pub fn buildNotify() []const u8 {
    return &notify_payload_inner;
}
