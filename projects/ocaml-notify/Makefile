OCAMLOPT = ocamlopt
OCAMLC   = ocamlc
OCAMLFLAGS = -I +unix

.PHONY: all run interp test clean

all: notify-bin notify.byte

# native module; the recipe produces all three files together
dbus_msg.cmx dbus_msg.cmi dbus_msg.o &: dbus_msg.ml
	$(OCAMLOPT) $(OCAMLFLAGS) unix.cmxa -c dbus_msg.ml

# bytecode module for the interpreter driver; reuses the native .cmi
dbus_msg.cmo: dbus_msg.cmx
	$(OCAMLC) $(OCAMLFLAGS) -c dbus_msg.ml

notify-bin: notify.ml dbus_msg.cmx
	$(OCAMLOPT) $(OCAMLFLAGS) unix.cmxa dbus_msg.cmx -o notify-bin notify.ml

notify.byte: notify.ml dbus_msg.cmo
	$(OCAMLC) $(OCAMLFLAGS) unix.cma dbus_msg.cmo -o notify.byte notify.ml

test/test_payload: test/test_payload.ml dbus_msg.cmx
	$(OCAMLOPT) $(OCAMLFLAGS) unix.cmxa dbus_msg.cmx -o test/test_payload test/test_payload.ml

run: notify-bin
	./notify-bin "hello from ocaml"

interp: notify.byte
	ocamlrun notify.byte "hello from ocaml"

test: test/test_payload
	./test/test_payload

clean:
	rm -f notify-bin notify.byte notify.cmi notify.cmx notify.o
	rm -f dbus_msg.cmi dbus_msg.cmx dbus_msg.cmo dbus_msg.o
	rm -f test/test_payload test/test_payload.cmi test/test_payload.cmx test/test_payload.o
