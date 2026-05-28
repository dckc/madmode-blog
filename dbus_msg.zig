const std = @import("std");

pub const MESSAGE_TYPE_METHOD_CALL = 1;

pub const FIELD_PATH = 1;
pub const FIELD_INTERFACE = 2;
pub const FIELD_MEMBER = 3;
pub const FIELD_DESTINATION = 6;
pub const FIELD_SIGNATURE = 8;

const MAX_SIZE = 512;

pub const Buf = struct {
    data: [MAX_SIZE]u8 = undefined,
    off: usize = 0,

    pub fn get(self: *const Buf) []const u8 {
        return self.data[0..self.off];
    }

    pub fn putU8(self: *Buf, v: u8) void {
        self.data[self.off] = v;
        self.off += 1;
    }

    pub fn padTo(self: *Buf, a: usize) void {
        const new_off = alignUp(self.off, a);
        while (self.off < new_off) : (self.off += 1) {
            self.data[self.off] = 0;
        }
    }

    pub fn putU32(self: *Buf, v: u32) void {
        self.padTo(4);
        std.mem.writeInt(u32, self.data[self.off..][0..4], v, .little);
        self.off += 4;
    }

    pub fn putI32(self: *Buf, v: i32) void {
        self.padTo(4);
        std.mem.writeInt(i32, self.data[self.off..][0..4], v, .little);
        self.off += 4;
    }

    pub fn putString(self: *Buf, s: []const u8) void {
        self.padTo(4);
        self.putU32(@intCast(s.len));
        @memcpy(self.data[self.off..][0..s.len], s);
        self.off += s.len;
        self.data[self.off] = 0;
        self.off += 1;
    }

    pub fn putSignature(self: *Buf, s: []const u8) void {
        self.data[self.off] = @intCast(s.len);
        self.off += 1;
        @memcpy(self.data[self.off..][0..s.len], s);
        self.off += s.len;
        self.data[self.off] = 0;
        self.off += 1;
    }

    fn putVariantValue(self: *Buf, comptime sig: []const u8, val: anytype) void {
        self.putSignature(sig);
        self.padTo(sigAlign(sig));
        self.putValue(sig, val);
    }

    fn putArray(self: *Buf, comptime elem_sig: []const u8, items: anytype) void {
        self.padTo(4);
        self.putU32(@intCast(items.len));
        self.padTo(sigAlign(elem_sig));
        inline for (items) |item| {
            self.putValue(elem_sig, item);
        }
    }

    fn putDict(self: *Buf, comptime key_sig: u8, comptime val_sig: []const u8, items: anytype) void {
        self.padTo(4);
        self.putU32(@intCast(items.len));
        self.padTo(8);
        inline for (items) |item| {
            self.padTo(8);
            self.putValue(&.{key_sig}, item.key);
            self.putVariantValue(val_sig, item.value);
        }
    }

    fn putBody(self: *Buf, comptime sig: []const u8, values: anytype) void {
        const types = comptime sigTypes(sig);
        inline for (types, 0..) |t, i| {
            self.padTo(sigAlign(t));
            self.putValue(t, values[i]);
        }
    }

    pub fn serialise(self: *Buf, comptime msg_type: u8, comptime serial: u32, comptime headers: anytype, comptime body_sig: []const u8, body: anytype) void {
        self.putU8('l');
        self.putU8(msg_type);
        self.putU8(0);
        self.putU8(1);

        const body_len_off = self.off;
        self.off += 4;

        self.putU32(serial);

        const hdr_len_off = self.off;
        self.off += 4;

        const hdr_start = self.off;

        inline for (headers) |hdr| {
            self.padTo(8);
            self.putU8(hdr.code);
            self.putSignature(hdr.sig);
            self.padTo(sigAlign(hdr.sig));
            self.putValue(hdr.sig, hdr.val);
        }

        const hdr_len = self.off - hdr_start;
        std.mem.writeInt(u32, self.data[hdr_len_off..][0..4], @intCast(hdr_len), .little);

        self.padTo(8);
        const body_start = self.off;

        if (body_sig.len > 0) {
            putBody(self, body_sig, body);
        }

        const body_len = self.off - body_start;
        std.mem.writeInt(u32, self.data[body_len_off..][0..4], @intCast(body_len), .little);
    }

    fn putValue(self: *Buf, comptime sig: []const u8, val: anytype) void {
        const c = sig[0];
        if (c == 's' or c == 'o') {
            self.putString(val);
        } else if (c == 'u') {
            self.putU32(val);
        } else if (c == 'i') {
            self.putI32(val);
        } else if (c == 'g') {
            self.putSignature(val);
        } else if (c == 'v') {
            self.putVariantValue(val[0], val[1]);
        } else if (c == 'a') {
            if (sig[1] == '{') {
                self.putDict(sig[2], sig[3..sig.len - 1], val);
            } else {
                self.putArray(sig[1..], val);
            }
        } else if (c == '(') {
            const inner = comptime sigTypes(sig[1..sig.len - 1]);
            inline for (inner, 0..) |t, i| {
                self.padTo(sigAlign(t));
                self.putValue(t, val[i]);
            }
        }
    }

    fn sigAlign(comptime sig: []const u8) usize {
        const c = sig[0];
        if (c == 'y' or c == 'g') return 1;
        if (c == 'b' or c == 'i' or c == 'u' or c == 'h') return 4;
        if (c == 'n' or c == 'q') return 2;
        if (c == 'x' or c == 't' or c == 'd') return 8;
        if (c == 's' or c == 'o') return 4;
        if (c == 'v') return 1;
        if (c == 'a') {
            if (sig.len > 1 and sig[1] == '{') return 8;
            return @max(@as(usize, 4), sigAlign(sig[1..]));
        }
        if (c == '(') {
            const inner = comptime sigTypes(sig[1..sig.len - 1]);
            var max_align: usize = 1;
            inline for (inner) |t| {
                max_align = @max(max_align, sigAlign(t));
            }
            return max_align;
        }
        return 1;
    }

    fn sigTypes(comptime sig: []const u8) []const []const u8 {
        comptime {
            var result: [16][]const u8 = undefined;
            var count: usize = 0;
            var i: usize = 0;
            while (i < sig.len) {
                if (sig[i] == 'a') {
                    if (i + 1 < sig.len and sig[i + 1] == '{') {
                        const end = std.mem.indexOfScalarPos(u8, sig, i + 2, '}') orelse break;
                        result[count] = sig[i .. end + 1];
                        i = end + 1;
                    } else {
                        result[count] = sig[i .. i + 2];
                        i += 2;
                    }
                } else if (sig[i] == '(') {
                    const end = std.mem.indexOfScalarPos(u8, sig, i + 1, ')') orelse break;
                    result[count] = sig[i .. end + 1];
                    i = end + 1;
                } else {
                    result[count] = sig[i .. i + 1];
                    i += 1;
                }
                count += 1;
            }
            return result[0..count];
        }
    }
};

fn alignUp(off: usize, a: usize) usize {
    return (off + a - 1) & ~(a - 1);
}
