yo: yo.zig dbus_msg.zig generate_payload.zig
	zig build-exe -O ReleaseSmall --color off --name yo yo.zig

hello.bin notify.bin: generate_payload.py
	python3 generate_payload.py

run: yo
	./yo

test: hello.bin notify.bin
	python3 send_test.py

trace: yo
	strace -e trace=read,write ./yo

# TODO: pypy package?
# TODO: nix flake?
AWESOME_OCAP=$(HOME)/projects/awesome-ocap
ocap-devtools:
	mkdir -p docs/
	cp -rp $(AWESOME_OCAP)/style-guide/*.md docs/
	mkdir -p tools
	cp -rp $(HOME)/projects/awesome-ocap/tools/disciplined_python_check.py tools/

clean:
	rm -f ./yo hello.bin notify.bin
