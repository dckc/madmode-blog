import struct

def pad_to(data, alignment):
    n = (alignment - (len(data) % alignment)) % alignment
    return data + b'\x00' * n

def make_field(tag, sig_byte, val_bytes):
    field = struct.pack('<BB', tag, 1)
    field += sig_byte + b'\x00'
    if sig_byte == b'g':
        field += struct.pack('<B', len(val_bytes) - 1) + val_bytes
    else:
        field += struct.pack('<I', len(val_bytes) - 1) + val_bytes
    return field

def build_dbus_packet(serial_num, dest_name, path_name, iface_name,
                      member_name, signature, body_bytes):
    fields_raw = b''
    def add(tag, sig, val):
        nonlocal fields_raw
        fields_raw = pad_to(fields_raw, 8)
        fields_raw += make_field(tag, sig, val)

    add(1, b'o', path_name.encode() + b'\x00')
    if dest_name:
        add(6, b's', dest_name.encode() + b'\x00')
    add(2, b's', iface_name.encode() + b'\x00')
    add(3, b's', member_name.encode() + b'\x00')
    if signature:
        add(8, b'g', signature.encode() + b'\x00')

    fields_len = len(fields_raw)
    header = b'l\x01\x00\x01'
    header += struct.pack('<I', len(body_bytes))
    header += struct.pack('<I', serial_num)
    header += struct.pack('<I', fields_len)
    packet = pad_to(header, 8) + fields_raw
    packet = pad_to(packet, 8) + body_bytes
    return pad_to(packet, 8)

def build_string(val):
    return struct.pack('<I', len(val) - 1) + val

# D-Bus alignment rules per type:
#   s -> 4, o -> 4, g -> 1, u -> 4, i -> 4, (s) -> 4, {sv} -> 8
TYPE_ALIGN = {
    's': 4, 'o': 4, 'g': 1, 'u': 4, 'i': 4,
}

def build_body():
    body = b''

    body = pad_to(body, TYPE_ALIGN['s']) + build_string(b"tiny-notify\x00")
    body = pad_to(body, TYPE_ALIGN['u']) + struct.pack('<I', 0)       # replaces_id
    body = pad_to(body, TYPE_ALIGN['s']) + build_string(b"\x00")       # app_icon
    body = pad_to(body, TYPE_ALIGN['s']) + build_string(b"CI Failed!\x00")
    body = pad_to(body, TYPE_ALIGN['s']) + build_string(b"Your build broke.\x00")

    # actions: a(s) -> array of STRING, alignment 4
    body = pad_to(body, 4) + struct.pack('<I', 0)  # empty array

    # hints: a{sv} -> array of DICT_ENTRY{STRING,VARIANT}, alignment 8
    body = pad_to(body, 8)                         # align to 8
    body += struct.pack('<I', 0)                    # empty dict length
    body = pad_to(body, 8)                         # libdbus pads even for empty dicts

    body = pad_to(body, TYPE_ALIGN['i']) + struct.pack('<i', -1)
    return body

notify_body = build_body()

hello_pkt = build_dbus_packet(1, "org.freedesktop.DBus",
    "/org/freedesktop/DBus", "org.freedesktop.DBus", "Hello", "", b"")
with open("hello.bin", "wb") as f:
    f.write(hello_pkt)

notify_pkt = build_dbus_packet(2, "org.freedesktop.Notifications",
    "/org/freedesktop/Notifications", "org.freedesktop.Notifications",
    "Notify", "susssasa{sv}i", notify_body)
with open("notify.bin", "wb") as f:
    f.write(notify_pkt)

print(f"Hello: {len(hello_pkt)} bytes")
print(f"Notify: {len(notify_pkt)} bytes, body_len={notify_body.__len__()}")

# ── Self-validation ────────────────────────────────────────────────

# Variant alignment table: each type signature -> alignment
ALIGN_OF = {
    ord('s'): 4, ord('o'): 4, ord('g'): 1,
    ord('u'): 4, ord('i'): 4, ord('b'): 1,
    ord('y'): 1, ord('n'): 4, ord('q'): 2,
    ord('d'): 8, ord('t'): 8,
    ord('a'): 8, ord('('): 8, ord('{'): 8,
    ord('v'): 1,
}

def align_offset(offset, alignment):
    return ((offset + alignment - 1) // alignment) * alignment

def parse_dbus_msg(data, label):
    """Structural parse of a D-Bus message. Returns errors list."""
    errs = []
    if len(data) < 16:
        errs.append(f"{label}: too short ({len(data)} bytes)")
        return errs
    endian = '<' if data[0] == 0x6c else '>'
    body_len = struct.unpack_from(f'{endian}I', data, 4)[0]
    fields_len = struct.unpack_from(f'{endian}I', data, 12)[0]
    msg_type = data[1]

    body_off = align_offset(16 + fields_len, 8)
    message_end = body_off + body_len
    message_end_padded = align_offset(message_end, 8)

    if body_off + body_len > len(data):
        errs.append(f"{label}: body extends beyond data")
        return errs

    # Walk each field using the known D-Bus header field struct:
    #   struct { byte tag; variant value; }
    # The variant is: type-signature (SIGNATURE), pad, value
    # Fields align implicitly per struct alignment rules.
    pos = 16
    field_count = 0
    tags_seen = []

    # Helper: advance past a VARIANT value given its single-basic-type char
    def skip_variant_value(p, vt):
        if vt in ('s', 'o'):
            if p + 4 > len(data): return p
            sl = struct.unpack_from(f'{endian}I', data, p)[0]
            return p + 4 + sl + 1
        elif vt == 'g':
            if p >= len(data): return p
            return p + 1 + data[p] + 1
        elif vt in ('u', 'i', 'b'):
            return p + 4
        elif vt == 'n':
            return p + 4
        elif vt == 'q':
            return p + 2
        elif vt in ('y',):
            return p + 1
        elif vt == '(':
            return p  # can't parse struct; caller must advance
        elif vt == 'a':
            return p  # can't parse array; caller must advance
        elif vt == '{':
            return p  # can't parse dict; caller must advance
        elif vt == 'v':
            return p
        return p

    while pos < body_off:
        # Stop if remaining bytes are body-alignment padding
        remaining = data[pos:body_off]
        if all(b == 0 for b in remaining):
            break

        # Each field struct starts at alignment = max(1, align_of(variant_value_type))
        # The struct alignment equals the max of its members.
        # tag (byte, align 1) is always fine.  The variant's alignment
        # equals the alignment of its value.  We just peek ahead.
        if pos + 3 > body_off:
            break

        # Compute the struct alignment from the variant type signature
        peek_sig_len = data[pos+1]
        if pos + 2 + peek_sig_len > body_off:
            break
        vt = chr(data[pos+2]) if peek_sig_len > 0 else '?'
        struct_align = ALIGN_OF.get(ord(vt), 4)

        # Pad start position to struct alignment (this is how alignment works
        # for nested structs, despite "Fields are NOT padded")
        field_start = align_offset(pos, struct_align)
        if field_start > pos:
            pos = field_start

        if pos + 2 > body_off:
            break

        tag = data[pos]
        tags_seen.append(tag)
        pos += 1  # tag

        sig_len = data[pos]; pos += 1
        sig_chars = data[pos:pos+sig_len].decode('ascii', errors='replace')
        pos += sig_len + 1  # chars + NUL

        value_type = sig_chars[0] if sig_chars else '?'

        # Pad variant value to its own alignment
        val_align = ALIGN_OF.get(ord(value_type), 4)
        pos = align_offset(pos, val_align)

        # Simple value types: advance
        if value_type in ('s', 'o'):
            vslen = struct.unpack_from(f'{endian}I', data, pos)[0]
            pos += 4 + vslen + 1
        elif value_type == 'g':
            pos += 1 + data[pos] + 1
        elif value_type in ('u', 'i', 'b'):
            pos += 4
        else:
            # Complex (array, struct, dict, variant) — skip rest of fields
            pos = body_off
        field_count += 1

    if message_end_padded != len(data):
        errs.append(f"{label}: total length {len(data)} != padded msg end {message_end_padded}")

    known_tags = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    for t in tags_seen:
        if t not in known_tags:
            errs.append(f"{label}: invalid tag {t}")

    return errs

def validate_body(body_bytes, signature="susssasa{sv}i"):
    """Parse body according to signature and check all alignment rules."""
    errs = []
    pos = 0
    expected = [
        ('s', 'app_name'),
        ('u', 'replaces_id'),
        ('s', 'app_icon'),
        ('s', 'summary'),
        ('s', 'body'),
        ('a(s)', 'actions'),
        ('a{sv}', 'hints'),
        ('i', 'expire_timeout'),
    ]
    for typ, name in expected:
        start_pos = pos
        if typ == 's':
            pos = ((pos + 3) // 4) * 4
            if pos != start_pos:
                errs.append(f"  {name}: aligned {start_pos} -> {pos}")
            if pos + 4 > len(body_bytes):
                errs.append(f"  {name}: body too short at {pos}")
                break
            slen = struct.unpack_from('<I', body_bytes, pos)[0]
            val = body_bytes[pos+4:pos+4+slen]
            try:
                errs.append(f"  {name}: '{val.decode()}' ({pos}+{4+slen+1})")
            except:
                errs.append(f"  {name}: <binary> ({pos}+{4+slen+1})")
            pos += 4 + slen + 1
        elif typ == 'u':
            pos = ((pos + 3) // 4) * 4
            if pos != start_pos:
                errs.append(f"  {name}: aligned {start_pos} -> {pos}")
            val = struct.unpack_from('<I', body_bytes, pos)[0]
            errs.append(f"  {name}: {val} ({pos}+4)")
            pos += 4
        elif typ == 'i':
            pos = ((pos + 3) // 4) * 4
            if pos != start_pos:
                errs.append(f"  {name}: aligned {start_pos} -> {pos}")
            val = struct.unpack_from('<i', body_bytes, pos)[0]
            errs.append(f"  {name}: {val} ({pos}+4)")
            pos += 4
        elif typ == 'a(s)':
            pos = ((pos + 3) // 4) * 4
            if pos != start_pos:
                errs.append(f"  {name}: aligned {start_pos} -> {pos}")
            alen = struct.unpack_from('<I', body_bytes, pos)[0]
            errs.append(f"  {name}: array_len={alen} ({pos}+4)")
            pos += 4
        elif typ == 'a{sv}':
            pos = ((pos + 7) // 8) * 8  # DICT_ENTRY alignment = 8
            if pos != start_pos:
                errs.append(f"  {name}: aligned {start_pos} -> {pos}")
            hlen = struct.unpack_from('<I', body_bytes, pos)[0]
            errs.append(f"  {name}: array_len={hlen} ({pos}+4)")
            pos += 4
            # libdbus pads even empty dicts to element alignment (8)
            padded = ((pos + 7) // 8) * 8
            if padded != pos:
                errs.append(f"  {name}: libdbus pad {pos} -> {padded}")
                pos = padded
    if pos != len(body_bytes):
        errs.append(f"  BODY MISMATCH: consumed {pos} of {len(body_bytes)} bytes")
    return errs


# Validate
print("\n── Validation ──")
for pkt, label in [(hello_pkt, "hello.bin"), (notify_pkt, "notify.bin")]:
    errs = parse_dbus_msg(pkt, label)
    if errs:
        for e in errs:
            print(f"  ERR: {e}")
    else:
        print(f"  {label}: packet OK")

print(f"\n── Notify body validation ──")
for line in validate_body(notify_body):
    print(line)

# Compare with ref
ref = open("notify_ref.bin", "rb").read()
ref_body_len = struct.unpack_from('<I', ref, 4)[0]
ref_fields_len = struct.unpack_from('<I', ref, 12)[0]
ref_body_off = ((16 + ref_fields_len + 7) // 8) * 8
ref_body = ref[ref_body_off:ref_body_off+ref_body_len]

if len(notify_body) != len(ref_body):
    print(f"\n── Body length differs: gen={len(notify_body)} ref={len(ref_body)} ──")
    # Find first diff
    for i in range(min(len(notify_body), len(ref_body))):
        if notify_body[i] != ref_body[i]:
            print(f"  First diff at offset {i}: gen={notify_body[i]:02x} ref={ref_body[i]:02x}")
            start = max(0, i-8)
            end = min(len(ref_body), i+16)
            print(f"  gen context: {notify_body[start:end].hex()}")
            print(f"  ref context: {ref_body[start:end].hex()}")
            break

print(f"\n── Done ──")
