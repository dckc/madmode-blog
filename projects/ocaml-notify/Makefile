.PHONY: build run interp test clean

build:
	ocamlopt -I +unix unix.cmxa -c dbus_payload.ml
	ocamlopt -I +unix unix.cmxa dbus_payload.cmx -o notify-bin notify.ml

run: build
	./notify-bin "hello from ocaml"

interp:
	ocamlc -I +unix -c dbus_payload.ml
	ocaml -I +unix -I . unix.cma notify_interp.ml -- "hello from ocaml"

test:
	ocamlopt -I +unix unix.cmxa -c dbus_payload.ml
	ocamlopt -I +unix unix.cmxa dbus_payload.cmx -o test/test_payload test/test_payload.ml
	./test/test_payload

clean:
	rm -f notify-bin notify.cmi notify.cmx notify.o
	rm -f dbus_payload.cmi dbus_payload.cmx dbus_payload.cmo dbus_payload.o
	rm -f test/test_payload test/test_payload.cmi test/test_payload.cmx test/test_payload.o
