(* SPDX-FileCopyrightText: 2026 Dan Connolly *)
(* SPDX-License-Identifier: Apache-2.0 *)

(* Minimal XDG desktop notifier in pure OCaml.
   Speaks just enough D-Bus over a Unix socket to call
   org.freedesktop.Notifications.Notify. *)

let ( let* ) = Result.bind

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
  (* body *)
  put_string "ocaml-notify";         (* app_name *)
  put_u32 0;                         (* replaces_id *)
  put_string "";                     (* app_icon *)
  put_string "ocaml-notify";         (* summary *)
  put_string body_text;             (* body *)
  put_u32 0;                         (* actions: empty array *)
  put_u32 0;                         (* hints: empty array a{sv} *)
  put_u32 0;                         (* expire_timeout *)
  let body_len = Buffer.length buf - 16 - hdr_len in
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

(* Read one reply chunk; a short timeout turns EAGAIN into a clean stop. *)
let recv_reply fd =
  let chunk = Bytes.create 4096 in
  try
    let n = Unix.read fd chunk 0 4096 in
    if n = 0 then "" else Bytes.sub_string chunk 0 n
  with Unix.Unix_error (Unix.EAGAIN, _, _) -> ""

let send fd payload =
  let n = Unix.write_substring fd payload 0 (String.length payload) in
  if n <> String.length payload then
    Error "short write"
  else Ok ()

let authenticate fd =
  let auth =
    "\000AUTH EXTERNAL 31303030\r\nNEGOTIATE_UNIX_FD\r\nBEGIN\r\n"
  in
  let* () = send fd auth in
  ignore (recv_reply fd);
  Ok ()

let notify body_text =
  let bus = "/run/user/1000/bus" in
  let fd = Unix.socket Unix.PF_UNIX Unix.SOCK_STREAM 0 in
  let result =
    try
      Unix.connect fd (Unix.ADDR_UNIX bus);
      Unix.setsockopt_float fd Unix.SO_RCVTIMEO 2.0;
      let* () = authenticate fd in
      let* () = send fd (build_hello ()) in
      ignore (recv_reply fd);
      let* () = send fd (build_notify body_text) in
      ignore (recv_reply fd);
      Ok ()
    with Unix.Unix_error (e, _, _) ->
      Error (Unix.error_message e)
  in
  Unix.close fd;
  result

let () =
  let args = Array.to_list Sys.argv in
  let args = match args with
    | _ :: "--" :: rest -> rest
    | rest -> rest
  in
  match args with
  | "--dump-hello" :: _ ->
    print_string (build_hello ())
  | "--dump-notify" :: _ ->
    print_string (build_notify "test")
  | body :: _ ->
    (match notify body with
     | Ok () -> ()
     | Error e -> prerr_endline ("notify: " ^ e); exit 1)
  | [] ->
    prerr_endline "usage: notify <message>";
    exit 1
