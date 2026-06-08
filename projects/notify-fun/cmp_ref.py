# SPDX-FileCopyrightText: 2026 Dan Connolly
# SPDX-License-Identifier: Apache-2.0

import struct, sys

"""Compare generated payload against reference, field by field."""

ref = open("notify_ref.bin", "rb").read()
gen = open("notify.bin", "rb").read()

def parse_dbus_msg(data, label):
    if len(data) < 16:
        return f"{label}: too short ({len(data)} bytes)"
    endian = '<' if data[0] == 0x6c else '>'
    msg_type = data[1]
    flags = data[2]
    proto = data[3]
    body_len = struct.unpack_from(f'{endian}I', data, 4)[0]
    serial = struct.unpack_from(f'{endian}I', data, 8)[0]
    fields_len = struct.unpack_from(f'{endian}I', data, 12)[0]

    info = f"{label}: type={msg_type} flags={flags} proto={proto}"
    info += f" serial={serial} body_len={body_len} fields_len={fields_len}"
    info += f" total={len(data)}"

    # Check body offset
    body_off = ((16 + fields_len + 7) // 8) * 8
    info += f" body_off={body_off}"
    if body_off + body_len > len(data):
        info += " (body extends beyond file!)"
    else:
        actual_body = data[body_off:body_off+body_len]
        info += f" actual_body_bytes={len(actual_body)}"
        # Show body
        info += f" body_hex={actual_body.hex()}"

    # Check all header fields  
    pos = 16
    field_num = 0
    info += "\n  Fields:"
    while pos < body_off:
        tag = data[pos]
        # VARIANT: type sig byte + \0 + pad + value
        variant_type_byte = data[pos+1]
        # Read the SIGNATURE following pos+1
        sig_len = data[pos+2]
        sig_str = data[pos+3:pos+3+sig_len].decode('ascii', errors='replace')
        # pos+3+sig_len is the NUL
        variant_sig = sig_str[0] if sig_str else '?'
        # Now the variant value starts after: pos + 1 + 1 + sig_len + 1 = pos + 3 + sig_len
        variant_pos = pos + 3 + sig_len  # +1 for sig_byte, +1 for sig_len, +sig_len for chars, +1 for NUL

        val_repr = ""
        if variant_sig == 's':
            vlen = struct.unpack_from(f'{endian}I', data, variant_pos)[0]
            vstr = data[variant_pos+4:variant_pos+4+vlen].decode('ascii', errors='replace')
            val_repr = f"\"{vstr}\""
            val_end = variant_pos + 4 + vlen + 1
        elif variant_sig == 'o':
            vlen = struct.unpack_from(f'{endian}I', data, variant_pos)[0]
            vstr = data[variant_pos+4:variant_pos+4+vlen].decode('ascii', errors='replace')
            val_repr = f"path:\"{vstr}\""
            val_end = variant_pos + 4 + vlen + 1
        elif variant_sig == 'g':
            vsig_len = data[variant_pos]
            vsig_str = data[variant_pos+1:variant_pos+1+vsig_len].decode('ascii', errors='replace')
            val_repr = f"sig:\"{vsig_str}\""
            val_end = variant_pos + 1 + vsig_len + 1
        else:
            val_repr = f"<unknown variant type {variant_sig}>"
            val_end = data.index(b'\x00', variant_pos) + 1

        field_len = val_end - pos
        info += f"\n    [{field_num}] tag={tag} type={variant_sig} {val_repr} (field_bytes={field_len})"
        pos = val_end
        field_num += 1

    return info

print(parse_dbus_msg(ref, "REF"))
print()
print(parse_dbus_msg(gen, "GEN"))

# Raw byte comparison
print()
if len(ref) == len(gen):
    print(f"SAME SIZE: {len(ref)} bytes")
else:
    print(f"DIFFERENT SIZE: ref={len(ref)} gen={len(gen)}")
    if len(ref) < len(gen):
        shorter, longer, sname, lname = ref, gen, "ref", "gen"
    else:
        shorter, longer, sname, lname = gen, ref, "gen", "ref"
    # Find first difference
    for i in range(len(shorter)):
        if shorter[i] != longer[i]:
            print(f"  First diff at offset {i} (0x{i:x}): {sname}={shorter[i]:02x} {lname}={longer[i]:02x}")
            # Show surrounding context
            start = max(0, i-8)
            end = min(len(shorter), i+8)
            print(f"  Context:")
            print(f"    {sname}: {shorter[start:end].hex()}")
            print(f"    {lname}: {longer[start:end].hex()}")
            break
    print(f"  Shorter ends at offset {len(shorter)} mismatching bytes start")
    for j in range(len(shorter), min(len(shorter)+16, len(longer))):
        print(f"    extra {lname} byte at {j} (0x{j:x}): {longer[j]:02x}")

# Check body section specifically
ref_body_off = ((16 + 155 + 7) // 8) * 8  # ref fields_len = 155
gen_fields_len = struct.unpack_from('<I', gen, 12)[0]
gen_body_off = ((16 + gen_fields_len + 7) // 8) * 8
ref_body_len = struct.unpack_from('<I', ref, 4)[0]
gen_body_len = struct.unpack_from('<I', gen, 4)[0]

print(f"\nBody comparison:")
print(f"  REF: body_off={ref_body_off} body_len={ref_body_len} body_hex={ref[ref_body_off:ref_body_off+ref_body_len].hex()}")
print(f"  GEN: body_off={gen_body_off} body_len={gen_body_len} body_hex={gen[gen_body_off:gen_body_off+gen_body_len].hex()}")

if ref_body_len == gen_body_len:
    if ref[ref_body_off:ref_body_off+ref_body_len] == gen[gen_body_off:gen_body_off+gen_body_len]:
        print(f"  Bodies MATCH")
    else:
        print(f"  Bodies DIFFER")
        for i in range(min(ref_body_len, gen_body_len)):
            if ref[ref_body_off+i] != gen[gen_body_off+i]:
                print(f"    First diff at body offset {i}: ref={ref[ref_body_off+i]:02x} gen={gen[gen_body_off+i]:02x}")
                break
