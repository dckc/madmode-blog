"""Minimal D-Bus message implementation — replaces jeepney for generate_payload.py."""

import struct

MESSAGE_TYPE_METHOD_CALL = 1

FIELD_PATH = 1
FIELD_INTERFACE = 2
FIELD_MEMBER = 3
FIELD_DESTINATION = 6
FIELD_SIGNATURE = 8


class DBusAddress:
    def __init__(self, *, object_path, bus_name, interface):
        self.object_path = object_path
        self.bus_name = bus_name
        self.interface = interface


class Header:
    def __init__(self, fields):
        self.fields = fields


class Message:
    def __init__(self, header, body, message_type):
        self.header = header
        self.body = body
        self.message_type = message_type

    def serialise(self, serial=1):
        return _serialise(self, serial)

    @classmethod
    def from_buffer(cls, data):
        return _parse(data)


def new_method_call(address, method, signature=None, body=None):
    fields = {}
    fields[FIELD_PATH] = address.object_path
    fields[FIELD_DESTINATION] = address.bus_name
    if address.interface is not None:
        fields[FIELD_INTERFACE] = address.interface
    fields[FIELD_MEMBER] = method
    if signature:
        fields[FIELD_SIGNATURE] = signature
    if body is None:
        body = ()
    elif not isinstance(body, tuple):
        body = (body,)
    return Message(Header(fields), body, MESSAGE_TYPE_METHOD_CALL)


_TYPE_ALIGN = {
    'y': 1, 'b': 4, 'n': 2, 'q': 2, 'i': 4, 'u': 4,
    'x': 8, 't': 8, 'd': 8, 's': 4, 'o': 4, 'g': 1,
    'v': 1, 'h': 4,
}


def _align(offset, a):
    return (offset + a - 1) & ~(a - 1)


def _align_buf(buf, a):
    pos = len(buf)
    aligned = _align(pos, a)
    if aligned > pos:
        buf.extend(b'\x00' * (aligned - pos))


def _pack_string(buf, s):
    data = s.encode('utf-8')
    buf.extend(struct.pack('<I', len(data)))
    buf.extend(data)
    buf.append(0)


def _pack_sig(buf, sig):
    encoded = sig.encode('ascii')
    buf.append(len(encoded))
    buf.extend(encoded)
    buf.append(0)


def _sig_align(sig):
    if not sig:
        return 1
    c = sig[0]
    if c == 'a':
        if len(sig) > 1 and sig[1] == '{':
            return 8
        elem_align = _sig_align(sig[1:])
        return max(4, elem_align)
    elif c == '(':
        inner = sig[1:-1]
        if not inner:
            return 1
        types = _parse_sigs(inner)
        return max((_sig_align(t) for t in types), default=1)
    elif c in _TYPE_ALIGN:
        return _TYPE_ALIGN[c]
    return 1


def _parse_sigs(sig):
    types = []
    i = 0
    while i < len(sig):
        c = sig[i]
        if c == 'a':
            if i + 1 < len(sig) and sig[i + 1] == '{':
                end = sig.index('}', i + 2)
                types.append(sig[i:end + 1])
                i = end + 1
            else:
                types.append(c + sig[i + 1])
                i += 2
        elif c == '(':
            end = sig.index(')', i + 1)
            types.append(sig[i:end + 1])
            i = end + 1
        else:
            types.append(c)
            i += 1
    return types


def _pack_value(buf, sig, value):
    c = sig[0] if sig else ''
    if c == 'y':
        buf.append(value)
    elif c == 'b':
        buf.extend(struct.pack('<I', 1 if value else 0))
    elif c == 'n':
        buf.extend(struct.pack('<h', value))
    elif c == 'q':
        buf.extend(struct.pack('<H', value))
    elif c == 'i':
        buf.extend(struct.pack('<i', value))
    elif c == 'u':
        buf.extend(struct.pack('<I', value))
    elif c == 'x':
        buf.extend(struct.pack('<q', value))
    elif c == 't':
        buf.extend(struct.pack('<Q', value))
    elif c == 'd':
        buf.extend(struct.pack('<d', value))
    elif c in ('s', 'o'):
        _pack_string(buf, value)
    elif c == 'g':
        _pack_sig(buf, value)
    elif c == 'h':
        buf.extend(struct.pack('<I', value))
    elif c == 'v':
        inner_sig, inner_val = value
        _pack_sig(buf, inner_sig)
        _align_buf(buf, _sig_align(inner_sig))
        _pack_value(buf, inner_sig, inner_val)
    elif c == 'a':
        if len(sig) > 1 and sig[1] == '{':
            key_sig = sig[2]
            value_sig = sig[3:-1]
            _align_buf(buf, 4)
            items = list(value.items()) if isinstance(value, dict) else list(value)
            buf.extend(struct.pack('<I', len(items)))
            _align_buf(buf, 8)
            for k, v in items:
                _align_buf(buf, 8)
                _pack_value(buf, key_sig, k)
                _pack_value(buf, 'v', (value_sig, v))
        else:
            elem_sig = sig[1:]
            _align_buf(buf, 4)
            buf.extend(struct.pack('<I', len(value)))
            _align_buf(buf, _sig_align(elem_sig))
            for item in value:
                _pack_value(buf, elem_sig, item)
    elif c == '(':
        inner_sigs = _parse_sigs(sig[1:-1])
        for inner_sig, item in zip(inner_sigs, value):
            _align_buf(buf, _sig_align(inner_sig))
            _pack_value(buf, inner_sig, item)
    else:
        raise ValueError(f"Unknown type: {sig}")


_FIELD_ORDER = [FIELD_PATH, FIELD_INTERFACE, FIELD_MEMBER, FIELD_DESTINATION, FIELD_SIGNATURE]
_FIELD_TYPE = {
    FIELD_PATH: 'o',
    FIELD_INTERFACE: 's',
    FIELD_MEMBER: 's',
    FIELD_DESTINATION: 's',
    FIELD_SIGNATURE: 'g',
}


def _serialise(msg, serial):
    body_buf = bytearray()
    body_sig = msg.header.fields.get(FIELD_SIGNATURE, '')
    if body_sig:
        _pack_value(body_buf, '(' + body_sig + ')', msg.body)

    hdr_buf = bytearray()
    first = True
    for code in _FIELD_ORDER:
        if code in msg.header.fields:
            if not first:
                _align_buf(hdr_buf, 8)
            first = False
            _pack_header_field(hdr_buf, code, _FIELD_TYPE[code], msg.header.fields[code])

    buf = bytearray()
    buf.append(ord('l'))
    buf.append(msg.message_type)
    buf.append(0)
    buf.append(1)
    buf.extend(struct.pack('<I', len(body_buf)))
    buf.extend(struct.pack('<I', serial))
    buf.extend(struct.pack('<I', len(hdr_buf)))
    buf.extend(hdr_buf)
    _align_buf(buf, 8)
    buf.extend(body_buf)
    return bytes(buf)


def _pack_header_field(buf, code, sig, value):
    buf.append(code)
    _pack_sig(buf, sig)
    _align_buf(buf, _sig_align(sig))
    _pack_value(buf, sig, value)


def _parse_single_value(data, offset, sig):
    c = sig[0] if sig else ''
    a = _sig_align(sig)
    offset = _align(offset, a)

    if c == 'y':
        return data[offset], offset + 1
    elif c == 'b':
        return bool(struct.unpack_from('<I', data, offset)[0]), offset + 4
    elif c == 'n':
        return struct.unpack_from('<h', data, offset)[0], offset + 2
    elif c == 'q':
        return struct.unpack_from('<H', data, offset)[0], offset + 2
    elif c == 'i':
        return struct.unpack_from('<i', data, offset)[0], offset + 4
    elif c == 'u':
        return struct.unpack_from('<I', data, offset)[0], offset + 4
    elif c == 'x':
        return struct.unpack_from('<q', data, offset)[0], offset + 8
    elif c == 't':
        return struct.unpack_from('<Q', data, offset)[0], offset + 8
    elif c == 'd':
        return struct.unpack_from('<d', data, offset)[0], offset + 8
    elif c in ('s', 'o'):
        length = struct.unpack_from('<I', data, offset)[0]
        start = offset + 4
        val = data[start:start + length].decode('utf-8')
        return val, start + length + 1
    elif c == 'g':
        length = data[offset]
        start = offset + 1
        val = data[start:start + length].decode('ascii')
        return val, start + length + 1
    elif c == 'h':
        return struct.unpack_from('<I', data, offset)[0], offset + 4
    elif c == 'v':
        sig_len = data[offset]
        inner_sig = data[offset + 1:offset + 1 + sig_len].decode('ascii')
        offset2 = offset + 1 + sig_len + 1
        value, offset2 = _parse_single_value(data, offset2, inner_sig)
        return (inner_sig, value), offset2
    elif c == 'a':
        length = struct.unpack_from('<I', data, offset)[0]
        offset += 4
        if len(sig) > 1 and sig[1] == '{':
            key_sig = sig[2]
            value_sig = sig[3:-1]
            result = []
            offset = _align(offset, 8)
            for _ in range(length):
                offset = _align(offset, 8)
                k, offset = _parse_single_value(data, offset, key_sig)
                v, offset = _parse_single_value(data, offset, 'v')
                result.append((k, v))
            return dict(result), offset
        else:
            elem_sig = sig[1:]
            elem_align = _sig_align(elem_sig)
            offset = _align(offset, elem_align)
            result = []
            for _ in range(length):
                v, offset = _parse_single_value(data, offset, elem_sig)
                result.append(v)
            return result, offset
    elif c == '(':
        inner_sigs = _parse_sigs(sig[1:-1])
        result = []
        for inner_sig in inner_sigs:
            offset = _align(offset, _sig_align(inner_sig))
            v, offset = _parse_single_value(data, offset, inner_sig)
            result.append(v)
        return tuple(result), offset
    else:
        raise ValueError(f"Unknown type: {sig}")


def _parse(data):
    endian = chr(data[0])
    if endian != 'l':
        raise ValueError(f"Unsupported endianness: {endian}")
    message_type = data[1]
    body_len = struct.unpack_from('<I', data, 4)[0]
    hdr_len = struct.unpack_from('<I', data, 12)[0]
    hdr_start = 16
    hdr_end = hdr_start + hdr_len
    hdr_data = data[hdr_start:hdr_end]

    fields = {}
    offset = 0
    while offset < len(hdr_data):
        code = hdr_data[offset]
        offset += 1
        value, offset = _parse_single_value(hdr_data, offset, 'v')
        fields[code] = value[1]
        offset = _align(offset, 8)

    body_start = _align(hdr_end, 8)
    body_end = body_start + body_len
    body_data = data[body_start:body_end]

    body_sig = fields.get(FIELD_SIGNATURE, '')
    body = ()
    if body_sig:
        sig = '(' + body_sig + ')'
        body, _ = _parse_single_value(data, body_start, sig)

    return Message(Header(fields), body, message_type)
