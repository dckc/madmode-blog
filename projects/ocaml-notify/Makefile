.PHONY: build run test clean

build:
	ocamlopt unix.cmxa -c dbus_payload.ml
	ocamlopt unix.cmxa dbus_payload.cmx -o notify-bin notify.ml

run: build
	./notify-bin "hello from ocaml"

test:
	ocamlopt unix.cmxa -c dbus_payload.ml
	ocamlopt unix.cmxa dbus_payload.cmx -o test/test_payload test/test_payload.ml
	./test/test_payload

clean:
	rm -f notify-bin notify.cmi notify.cmx notify.o dbus_payload.cmi dbus_payload.cmx dbus_payload.o
	rm -f test/test_payload test/test_payload.cmi test/test_payload.cmx test/test_payload.o
