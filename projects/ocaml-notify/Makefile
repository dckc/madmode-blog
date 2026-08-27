OCAMLOPT = ocamlopt -I +unix
OCAMLC   = ocamlc -I +unix

.PHONY: all run interp test clean

all: notify-bin

# native module (also produces dbus_payload.cmi)
dbus_payload.cmx dbus_payload.cmi dbus_payload.o: dbus_payload.ml
	$(OCAMLOPT) unix.cmxa -c dbus_payload.ml

# bytecode module for the interpreter driver; reuses the native .cmi
dbus_payload.cmo: dbus_payload.cmx
	$(OCAMLC) -c dbus_payload.ml

notify-bin: notify.ml dbus_payload.cmx
	$(OCAMLOPT) unix.cmxa dbus_payload.cmx -o notify-bin notify.ml

test/test_payload: test/test_payload.ml dbus_payload.cmx
	$(OCAMLOPT) unix.cmxa dbus_payload.cmx -o test/test_payload test/test_payload.ml

run: notify-bin
	./notify-bin "hello from ocaml"

interp: dbus_payload.cmo
	ocaml -I +unix -I . unix.cma notify_interp.ml -- "hello from ocaml"

test: test/test_payload
	./test/test_payload

clean:
	rm -f notify-bin notify.cmi notify.cmx notify.o
	rm -f dbus_payload.cmi dbus_payload.cmx dbus_payload.cmo dbus_payload.o
	rm -f test/test_payload test/test_payload.cmi test/test_payload.cmx test/test_payload.o
