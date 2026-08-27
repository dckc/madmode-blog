.PHONY: build run clean

build:
	ocamlopt unix.cmxa -o notify-bin notify.ml

run: build
	./notify-bin "hello from ocaml"

clean:
	rm -f notify-bin notify.cmi notify.cmx notify.o
