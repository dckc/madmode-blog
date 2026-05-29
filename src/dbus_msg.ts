/** Minimal D-Bus message serialization — replaces jeepney for notification payloads.
 *
 * D-Bus wire format follows the D-Bus Specification v0.43, 2024-10-29.
 * https://dbus.freedesktop.org/doc/dbus-specification.html
 *   §2 Message Protocol — wire format, endianness, header layout
 *   §2.2 Type System — type codes, alignment rules, marshalling
 *   §2.3.1 Header Fields — field codes (PATH, INTERFACE, MEMBER, etc.)
 *
 * API (DBusAddress, newMethodCall, Message) modeled after Jeepney v0.9.0,
 * 2025-02-27, by Thomas Kluyver.  https://jeepney.readthedocs.io/en/latest/ */

/** D-Bus method call message type. */
export const MESSAGE_TYPE_METHOD_CALL = 1;

/** D-Bus method return message type. */
export const MESSAGE_TYPE_METHOD_RETURN = 2;

/** D-Bus signal message type. */
export const MESSAGE_TYPE_SIGNAL = 3;

/** Header field codes. */
export const FIELD_PATH = 1;
export const FIELD_INTERFACE = 2;
export const FIELD_MEMBER = 3;
export const FIELD_DESTINATION = 6;
export const FIELD_SIGNATURE = 8;

/** A D-Bus address (bus name, object path, interface). */
export interface DBusAddress {
  readonly objectPath: string;
  readonly busName: string;
  readonly interface: string;
}

/** A serialized D-Bus message header. */
export interface Header {
  readonly fields: ReadonlyMap<number, unknown>;
}

/** A serialized D-Bus message. */
export interface Message {
  readonly header: Header;
  readonly body: readonly unknown[];
  readonly messageType: number;
}

/** Type alignment in bytes. */
const TYPE_ALIGN: Record<string, number> = {
  y: 1, b: 4, n: 2, q: 2, i: 4, u: 4,
  x: 8, t: 8, d: 8, s: 4, o: 4, g: 1,
  v: 1, h: 4,
};

function align(offset: number, a: number): number {
  return (offset + a - 1) & ~(a - 1);
}

function sigAlignment(sig: string): number {
  if (sig.length === 0) return 1;
  const c = sig[0]!;
  if (c === "a") {
    if (sig.length > 1 && sig[1] === "{") {
      // Dict entry alignment = max(key_align, value_align)
      const entryAlign = Math.max(sigAlignment(sig[2]!), sigAlignment(sig.slice(3, -1)));
      return Math.max(4, entryAlign);
    }
    return Math.max(4, sigAlignment(sig.slice(1)));
  }
  if (c === "(") {
    const inner = sig.slice(1, -1);
    if (inner.length === 0) return 1;
    return Math.max(...parseSignatures(inner).map(sigAlignment));
  }
  return TYPE_ALIGN[c] ?? 1;
}

function parseSignatures(sig: string): string[] {
  const types: string[] = [];
  let i = 0;
  while (i < sig.length) {
    const c = sig[i]!;
    if (c === "a") {
      if (i + 1 < sig.length && sig[i + 1] === "{") {
        const end = sig.indexOf("}", i + 2);
        types.push(sig.slice(i, end + 1));
        i = end + 1;
      } else {
        types.push(c + sig[i + 1]!);
        i += 2;
      }
    } else if (c === "(") {
      const end = sig.indexOf(")", i + 1);
      types.push(sig.slice(i, end + 1));
      i = end + 1;
    } else {
      types.push(c);
      i += 1;
    }
  }
  return types;
}

/** Mutable byte buffer for building D-Bus messages. */
export class Buf {
  readonly data: number[] = [];

  get bytes(): Uint8Array {
    return new Uint8Array(this.data);
  }

  u8(v: number): void {
    this.data.push(v & 0xff);
  }

  padTo(a: number): void {
    const off = this.data.length;
    const aligned = align(off, a);
    for (let i = off; i < aligned; i++) this.data.push(0);
  }

  u32(v: number): void {
    this.padTo(4);
    this.data.push(v & 0xff, (v >>> 8) & 0xff, (v >>> 16) & 0xff, (v >>> 24) & 0xff);
  }

  i32(v: number): void {
    this.u32(v >>> 0);
  }

  /** Patch a u32 at a previously written position (used for array byte lengths). */
  _patchU32(off: number, v: number): void {
    this.data[off] = v & 0xff;
    this.data[off + 1] = (v >>> 8) & 0xff;
    this.data[off + 2] = (v >>> 16) & 0xff;
    this.data[off + 3] = (v >>> 24) & 0xff;
  }

  string(s: string): void {
    this.padTo(4);
    const encoded = new TextEncoder().encode(s);
    this.u32(encoded.length);
    for (const b of encoded) this.data.push(b);
    this.u8(0);
  }

  signature(sig: string): void {
    const encoded = new TextEncoder().encode(sig);
    this.u8(encoded.length);
    for (const b of encoded) this.data.push(b);
    this.u8(0);
  }

  /** Pack a typed value. `sig` is a single complete D-Bus type string. */
  packValue(sig: string, value: unknown): void {
    const c = sig[0]!;
    if (c === "y") {
      this.u8(value as number);
    } else if (c === "b") {
      this.u32(value ? 1 : 0);
    } else if (c === "n") {
      this.padTo(2);
      const v = value as number;
      this.data.push(v & 0xff, (v >>> 8) & 0xff);
    } else if (c === "q") {
      this.padTo(2);
      const v = value as number;
      this.data.push(v & 0xff, (v >>> 8) & 0xff);
    } else if (c === "i") {
      this.i32(value as number);
    } else if (c === "u") {
      this.u32(value as number);
    } else if (c === "x") {
      this.padTo(8);
      const v = BigInt(value as number);
      for (let i = 0; i < 8; i++) this.data.push(Number((v >> BigInt(i * 8)) & 0xffn));
    } else if (c === "t") {
      this.padTo(8);
      const v = BigInt(value as number);
      for (let i = 0; i < 8; i++) this.data.push(Number((v >> BigInt(i * 8)) & 0xffn));
    } else if (c === "d") {
      this.padTo(8);
      const buf = new ArrayBuffer(8);
      new DataView(buf).setFloat64(0, value as number, true);
      for (const b of new Uint8Array(buf)) this.data.push(b);
    } else if (c === "s" || c === "o") {
      this.string(value as string);
    } else if (c === "g") {
      this.signature(value as string);
    } else if (c === "h") {
      this.u32(value as number);
    } else if (c === "v") {
      const [innerSig, innerVal] = value as [string, unknown];
      this.signature(innerSig);
      this.padTo(sigAlignment(innerSig));
      this.packValue(innerSig, innerVal);
    } else if (c === "a") {
      // D-Bus array length is byte count of marshalled elements, not element count.
      // Write placeholder, serialize elements, then patch.
      const elemSig = sig.length > 1 && sig[1] === "{"
        ? sig.slice(2)   // dict: key+val, e.g. "sv"
        : sig.slice(1);  // plain array, e.g. "s"
      const items = value as readonly unknown[] | Record<string, unknown>;
      this.padTo(4);
      const lenOff = this.data.length;
      this.u32(0); // placeholder — patched below

      if (sig.length > 1 && sig[1] === "{") {
        // Dict: a{key val}
        const keySig = sig[2]!;
        const valSig = sig.slice(3, -1);
        const entries = (typeof items === "object" && !Array.isArray(items))
          ? Object.entries(items as Record<string, unknown>)
          : [];
        this.padTo(8);
        const dataStart = this.data.length;
        for (const [k, v] of entries) {
          this.padTo(8);
          this.packValue(keySig, k);
          this.packValue("v", valSig === "v" ? (v as [string, unknown]) : [valSig, v]);
        }
        // Patch byte length
        this._patchU32(lenOff, this.data.length - dataStart);
      } else {
        // Plain array
        const arrayItems = items as readonly unknown[];
        this.padTo(sigAlignment(elemSig));
        const dataStart = this.data.length;
        for (const item of arrayItems) {
          this.packValue(elemSig, item);
        }
        // Patch byte length
        this._patchU32(lenOff, this.data.length - dataStart);
      }
    } else if (c === "(") {
      const innerSigs = parseSignatures(sig.slice(1, -1));
      const vals = value as readonly unknown[];
      for (let i = 0; i < innerSigs.length; i++) {
        this.padTo(sigAlignment(innerSigs[i]!));
        this.packValue(innerSigs[i]!, vals[i]);
      }
    } else {
      throw new Error(`Unknown D-Bus type: ${sig}`);
    }
  }
}

const FIELD_ORDER = [FIELD_PATH, FIELD_INTERFACE, FIELD_MEMBER, FIELD_DESTINATION, FIELD_SIGNATURE];
const FIELD_TYPE: Record<number, string> = {
  [FIELD_PATH]: "o",
  [FIELD_INTERFACE]: "s",
  [FIELD_MEMBER]: "s",
  [FIELD_DESTINATION]: "s",
  [FIELD_SIGNATURE]: "g",
};

/** Serialize a D-Bus message to wire format bytes. */
export function serialise(
  messageType: number,
  serial: number,
  headers: ReadonlyMap<number, unknown>,
  bodySig: string,
  body: readonly unknown[],
): Uint8Array {
  const bodyBuf = new Buf();
  if (bodySig.length > 0) {
    bodyBuf.packValue(`(${bodySig})`, body);
  }

  const hdrBuf = new Buf();
  let first = true;
  for (const code of FIELD_ORDER) {
    if (headers.has(code)) {
      if (!first) hdrBuf.padTo(8);
      first = false;
      const sig = FIELD_TYPE[code]!;
      hdrBuf.u8(code);
      hdrBuf.signature(sig);
      hdrBuf.padTo(sigAlignment(sig));
      hdrBuf.packValue(sig, headers.get(code));
    }
  }

  const buf = new Buf();
  buf.u8(0x6c); // 'l' little-endian
  buf.u8(messageType);
  buf.u8(0); // flags
  buf.u8(1); // protocol version
  buf.u32(bodyBuf.data.length);
  buf.u32(serial);
  buf.u32(hdrBuf.data.length);
  for (const b of hdrBuf.data) buf.data.push(b);
  buf.padTo(8);
  for (const b of bodyBuf.data) buf.data.push(b);

  return buf.bytes;
}

/** Create a method call message. */
export function newMethodCall(
  address: DBusAddress,
  method: string,
  signature?: string,
  body?: readonly unknown[],
): Uint8Array {
  const headers = new Map<number, unknown>();
  headers.set(FIELD_PATH, address.objectPath);
  headers.set(FIELD_DESTINATION, address.busName);
  headers.set(FIELD_INTERFACE, address.interface);
  headers.set(FIELD_MEMBER, method);
  if (signature !== undefined) {
    headers.set(FIELD_SIGNATURE, signature);
  }
  return serialise(MESSAGE_TYPE_METHOD_CALL, 1, headers, signature ?? "", body ?? []);
}
