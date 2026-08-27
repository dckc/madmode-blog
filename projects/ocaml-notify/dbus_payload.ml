(* SPDX-FileCopyrightText: 2026 Dan Connolly *)
(* SPDX-License-Identifier: Apache-2.0 *)

(* Hand-rolled D-Bus wire format for the XDG Notifications Notify call.
   Reference: D-Bus Specification v0.43, 2024-10-29, §2 Message Protocol.
   https://dbus.freedesktop.org/doc/dbus-specification.html *)

let buf = Buffer.create 512

let put_byte b = Buffer.add_char buf (Char.chr b)
let put_bytes s = Buffer.add_string buf s

let put_u32 n =
  put_byte (n land 0xff);
  put_byte ((n lsr 8) land 0xff);
  put_byte ((n lsr 16) land 0xff);
  put_byte ((n lsr 24) land 0xff)

let align () =
  let pad = (4 - (Buffer.length buf mod 4)) mod 4 in
  for _ = 1 to pad do put_byte 0 done

let align8 () =
  let pad = (8 - (Buffer.length buf mod 8)) mod 8 in
  for _ = 1 to pad do put_byte 0 done

let put_string s =
  put_u32 (String.length s);
  put_bytes s;
  put_byte 0

let put_signature s =
  put_byte (String.length s);
  put_bytes s;
  put_byte 0

(* Notify signature: susssasa{sv}i *)
let build_notify body_text =
  Buffer.clear buf;
  (* header *)
  put_byte (Char.code 'l');          (* little endian *)
  put_byte 1;                        (* METHOD_CALL *)
  put_byte 0; put_byte 1;            (* flags, protocol version *)
  put_u32 0;                         (* body length, patched later *)
  put_u32 2;                         (* serial *)
  put_u32 0;                         (* header length, patched later *)
  (* header fields *)
  put_byte 1; put_signature "o"; align (); put_string "/org/freedesktop/Notifications";
  align8 ();
  put_byte 2; put_signature "s"; align (); put_string "org.freedesktop.Notifications";
  align8 ();
  put_byte 3; put_signature "s"; align (); put_string "Notify";
  align8 ();
  put_byte 6; put_signature "s"; align (); put_string "org.freedesktop.Notifications";
  align8 ();
  put_byte 8; put_signature "g"; put_signature "susssasa{sv}i";
  let hdr_len = Buffer.length buf - 16 in
  (* body: aligned to 8 bytes after the header *)
  align8 ();
  let body_start = Buffer.length buf in
  (* body, signature susssasa{sv}i *)
  align (); put_string "ocaml-notify";         (* app_name s *)
  align (); put_u32 0;                         (* replaces_id u *)
  align (); put_string "";                     (* app_icon s *)
  align (); put_string "ocaml-notify";         (* summary s *)
  align (); put_string body_text;              (* body s *)
  align (); put_u32 0;                         (* actions as: empty *)
  align8 (); put_u32 0;                        (* hints a{sv}: length, 8-aligned *)
  align8 ();                                   (* a{sv} pads to 8 after length *)
  align (); put_u32 (-1);                      (* expire_timeout i: -1 = never *)
  let body_len = Buffer.length buf - body_start in
  let s = Bytes.of_string (Buffer.contents buf) in
  let set_u32 off v =
    Bytes.set s off (Char.chr (v land 0xff));
    Bytes.set s (off + 1) (Char.chr ((v lsr 8) land 0xff));
    Bytes.set s (off + 2) (Char.chr ((v lsr 16) land 0xff));
    Bytes.set s (off + 3) (Char.chr ((v lsr 24) land 0xff))
  in
  set_u32 4 body_len;
  set_u32 12 hdr_len;
  Bytes.to_string s

let build_hello () =
  Buffer.clear buf;
  put_byte (Char.code 'l');
  put_byte 1;
  put_byte 0; put_byte 1;
  put_u32 0;
  put_u32 1;
  put_u32 0;
  put_byte 1; put_signature "o"; align (); put_string "/org/freedesktop/DBus";
  align8 ();
  put_byte 2; put_signature "s"; align (); put_string "org.freedesktop.DBus";
  align8 ();
  put_byte 3; put_signature "s"; align (); put_string "Hello";
  align8 ();
  put_byte 6; put_signature "s"; align (); put_string "org.freedesktop.DBus";
  let hdr_len = Buffer.length buf - 16 in
  align8 ();                                   (* pad to 8 for empty body *)
  let s = Bytes.of_string (Buffer.contents buf) in
  let set_u32 off v =
    Bytes.set s off (Char.chr (v land 0xff));
    Bytes.set s (off + 1) (Char.chr ((v lsr 8) land 0xff));
    Bytes.set s (off + 2) (Char.chr ((v lsr 16) land 0xff));
    Bytes.set s (off + 3) (Char.chr ((v lsr 24) land 0xff))
  in
  set_u32 4 0;
  set_u32 12 hdr_len;
  Bytes.to_string s
