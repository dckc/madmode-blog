(* SPDX-FileCopyrightText: 2026 Dan Connolly *)
(* SPDX-License-Identifier: Apache-2.0 *)

(* Interpreter driver: the toplevel only executes the first file given on
   the command line, so #load the compiled dbus_payload module and #use the
   main program. Build the module first with: ocamlc -c dbus_payload.ml *)
#load "dbus_payload.cmo";;
#use "notify.ml";;
