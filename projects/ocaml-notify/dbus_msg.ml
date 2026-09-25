(* SPDX-FileCopyrightText: 2026 Dan Connolly *)
(* SPDX-License-Identifier: Apache-2.0 *)

(* Minimal D-Bus message implementation — replaces the hand-rolled builders.

   D-Bus wire format follows the D-Bus Specification v0.43, 2024-10-29.
   https://dbus.freedesktop.org/doc/dbus-specification.html
     §2 Message Protocol — wire format, endianness, header layout
     §2.2 Type System — type codes, alignment rules, marshalling
     §2.3.1 Header Fields — field codes (PATH, INTERFACE, MEMBER, etc.)

   API (dbus_address, new_method_call, message) modeled after Jeepney v0.9.0,
   2025-02-27, by Thomas Kluyver.  https://jeepney.readthedocs.io/en/latest/
*)

let message_type_method_call = 1

let field_path = 1
let field_interface = 2
let field_member = 3
let field_destination = 6
let field_signature = 8

type dbus_address = {
  object_path : string;
  bus_name : string;
  interface : string;
}

(* Body values. The type of each is fixed by the accompanying signature
   string passed to new_method_call. *)
type value =
  | Int of int
  | Int64 of int64
  | Float of float
  | Str of string              (* s, o *)
  | Signature of string        (* g *)
  | Array of value list
  | Dict of (value * value) list
  | Variant of string * value  (* signature, value *)
  | Struct of value list

type message = {
  header : (int * value) list;
  body : value list;
  message_type : int;
  signature : string;
}

let make_address ~object_path ~bus_name ~interface =
  { object_path; bus_name; interface }

let new_method_call address method_ ?(signature = "") ?(body = []) () =
  let signature_field =
    if signature = "" then [] else [ (field_signature, Signature signature) ]
  in
  {
    header =
      (field_path, Str address.object_path)
      :: (field_destination, Str address.bus_name)
      :: (field_interface, Str address.interface)
      :: (field_member, Str method_) :: signature_field;
    body;
    message_type = message_type_method_call;
    signature;
  }

(* ------------------------------------------------------------------ *)
(* marshalling                                                         *)
(* ------------------------------------------------------------------ *)

let add_byte buf b = Buffer.add_char buf (Char.chr b)

let add_u16 buf n =
  add_byte buf (n land 0xff);
  add_byte buf ((n lsr 8) land 0xff)

let add_u32 buf n =
  add_byte buf (n land 0xff);
  add_byte buf ((n lsr 8) land 0xff);
  add_byte buf ((n lsr 16) land 0xff);
  add_byte buf ((n lsr 24) land 0xff)

let add_u64 buf n =
  for i = 0 to 7 do
    add_byte buf
      (Int64.to_int (Int64.logand (Int64.shift_right_logical n (8 * i)) 0xffL))
  done

let align buf a =
  let pad = (a - (Buffer.length buf mod a)) mod a in
  for _ = 1 to pad do add_byte buf 0 done

let pack_string buf s =
  add_u32 buf (String.length s);
  Buffer.add_string buf s;
  add_byte buf 0

let pack_signature buf s =
  add_byte buf (String.length s);
  Buffer.add_string buf s;
  add_byte buf 0

let rec parse_sigs sigstr =
  let n = String.length sigstr in
  let i = ref 0 in
  let acc = ref [] in
  while !i < n do
    let c = sigstr.[!i] in
    if c = 'a' then
      if !i + 1 < n && sigstr.[!i + 1] = '{' then begin
        let end_ = String.index_from sigstr (!i + 2) '}' in
        acc := String.sub sigstr !i (end_ - !i + 1) :: !acc;
        i := end_ + 1
      end
      else begin
        acc := String.sub sigstr !i 2 :: !acc;
        i := !i + 2
      end
    else if c = '(' then begin
      let end_ = String.index_from sigstr (!i + 1) ')' in
      acc := String.sub sigstr !i (end_ - !i + 1) :: !acc;
      i := end_ + 1
    end
    else begin
      acc := String.make 1 c :: !acc;
      i := !i + 1
    end
  done;
  List.rev !acc

let rec sig_align sigstr =
  if String.length sigstr = 0 then 1
  else
    match sigstr.[0] with
    | 'a' ->
        if String.length sigstr > 1 && sigstr.[1] = '{' then 8
        else
          let elem =
            sig_align (String.sub sigstr 1 (String.length sigstr - 1))
          in
          max 4 elem
    | '(' ->
        let inner = String.sub sigstr 1 (String.length sigstr - 2) in
        if String.length inner = 0 then 1
        else
          List.fold_left (fun acc s -> max acc (sig_align s)) 1
            (parse_sigs inner)
    | c -> (
        match c with
        | 'y' | 'g' | 'v' -> 1
        | 'n' | 'q' -> 2
        | 'b' | 'i' | 'u' | 's' | 'o' | 'h' -> 4
        | 'x' | 't' | 'd' -> 8
        | _ -> 1)

let rec pack_value buf sigstr v =
  let c = sigstr.[0] in
  match (c, v) with
  | 'y', Int n -> add_byte buf n
  | 'b', Int n -> add_u32 buf (if n <> 0 then 1 else 0)
  | 'n', Int n -> add_u16 buf n
  | 'q', Int n -> add_u16 buf n
  | 'i', Int n -> add_u32 buf n
  | 'u', Int n -> add_u32 buf n
  | 'x', Int64 n -> add_u64 buf n
  | 't', Int64 n -> add_u64 buf n
  | 'd', Float f -> add_u64 buf (Int64.bits_of_float f)
  | ('s' | 'o'), Str s -> pack_string buf s
  | 'g', Signature s -> pack_signature buf s
  | 'h', Int n -> add_u32 buf n
  | 'v', Variant (sigv, vv) ->
      pack_signature buf sigv;
      align buf (sig_align sigv);
      pack_value buf sigv vv
  | 'a', _ ->
      if String.length sigstr > 1 && sigstr.[1] = '{' then
        pack_array_dict buf sigstr v
      else pack_array buf sigstr v
  | '(', Struct vs -> pack_struct buf sigstr vs
  | _ -> invalid_arg "pack_value"

and pack_array buf sigstr v =
  let elem_sig = String.sub sigstr 1 (String.length sigstr - 1) in
  let items = match v with Array vs -> vs | _ -> invalid_arg "array" in
  align buf 4;
  add_u32 buf (List.length items);
  align buf (sig_align elem_sig);
  List.iter (fun item -> pack_value buf elem_sig item) items

and pack_array_dict buf sigstr v =
  let key_sig = String.make 1 sigstr.[2] in
  let value_sig = String.sub sigstr 3 (String.length sigstr - 4) in
  let items = match v with Dict l -> l | _ -> invalid_arg "dict" in
  align buf 4;
  add_u32 buf (List.length items);
  align buf 8;
  List.iter
    (fun (k, vv) ->
      align buf 8;
      pack_value buf key_sig k;
      pack_value buf "v" (Variant (value_sig, vv)))
    items

and pack_struct buf sigstr vs =
  let inner = parse_sigs (String.sub sigstr 1 (String.length sigstr - 2)) in
  List.iter2
    (fun sig_ item ->
      align buf (sig_align sig_);
      pack_value buf sig_ item)
    inner vs

and pack_header_field buf code sig_ value =
  add_byte buf code;
  pack_signature buf sig_;
  align buf (sig_align sig_);
  pack_value buf sig_ value

(* ------------------------------------------------------------------ *)
(* serialisation                                                        *)
(* ------------------------------------------------------------------ *)

let field_order = [ field_path; field_interface; field_member; field_destination; field_signature ]

let field_type code =
  match code with
  | 1 -> "o"
  | 2 -> "s"
  | 3 -> "s"
  | 6 -> "s"
  | 8 -> "g"
  | _ -> invalid_arg "field_type"

let serialise ?(serial = 1) msg =
  let buf = Buffer.create 512 in
  let body_buf = Buffer.create 256 in
  if msg.signature <> "" then
    pack_value body_buf ("(" ^ msg.signature ^ ")") (Struct msg.body);
  let hdr_buf = Buffer.create 256 in
  let first = ref true in
  List.iter
    (fun code ->
      match List.assoc_opt code msg.header with
      | None -> ()
      | Some v ->
          if not !first then align hdr_buf 8;
          first := false;
          pack_header_field hdr_buf code (field_type code) v)
    field_order;
  add_byte buf (Char.code 'l');
  add_byte buf msg.message_type;
  add_byte buf 0;
  add_byte buf 1;
  add_u32 buf (Buffer.length body_buf);
  add_u32 buf serial;
  add_u32 buf (Buffer.length hdr_buf);
  Buffer.add_buffer buf hdr_buf;
  align buf 8;
  Buffer.add_buffer buf body_buf;
  Buffer.contents buf

(* ------------------------------------------------------------------ *)
(* payloads for this notifier                                          *)
(* ------------------------------------------------------------------ *)

let build_hello () =
  let addr =
    make_address
      ~object_path:"/org/freedesktop/DBus"
      ~bus_name:"org.freedesktop.DBus"
      ~interface:"org.freedesktop.DBus"
  in
  serialise ~serial:1 (new_method_call addr "Hello" ())

let build_notify body_text =
  let addr =
    make_address
      ~object_path:"/org/freedesktop/Notifications"
      ~bus_name:"org.freedesktop.Notifications"
      ~interface:"org.freedesktop.Notifications"
  in
  let body =
    [ Str "ocaml-notify"; Int 0; Str ""; Str "ocaml-notify"; Str body_text;
      Array []; Dict []; Int (-1) ]
  in
  serialise ~serial:2
    (new_method_call addr "Notify" ~signature:"susssasa{sv}i" ~body ())
