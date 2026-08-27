(* SPDX-FileCopyrightText: 2026 Dan Connolly *)
(* SPDX-License-Identifier: Apache-2.0 *)

(* Minimal XDG desktop notifier in pure OCaml.
   Speaks just enough D-Bus over a Unix socket to call
   org.freedesktop.Notifications.Notify. *)

let ( let* ) = Result.bind

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
      let* () = send fd (Dbus_payload.build_hello ()) in
      ignore (recv_reply fd);
      let* () = send fd (Dbus_payload.build_notify body_text) in
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
    | _ :: rest -> rest
    | [] -> []
  in
  let args = match args with
    | "--" :: rest -> rest
    | rest -> rest
  in
  match args with
  | "--dump-hello" :: _ ->
    print_string (Dbus_payload.build_hello ())
  | "--dump-notify" :: _ ->
    print_string (Dbus_payload.build_notify "test")
  | body :: _ ->
    (match notify body with
     | Ok () -> ()
     | Error e -> prerr_endline ("notify: " ^ e); exit 1)
  | [] ->
    prerr_endline "usage: notify <message>";
    exit 1
