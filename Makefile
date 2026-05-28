yo: yo.zig dbus_msg.zig generate_payload.zig
	zig build-exe -O ReleaseSmall --color off --name yo yo.zig

yo-strip: yo
	cp yo yo-strip
	strip yo-strip

hello.bin notify.bin: generate_payload.py
	python3 generate_payload.py

run: yo
	./yo

test: hello.bin notify.bin
	python3 send_test.py

trace: yo
	strace -e trace=read,write ./yo

analyze: yo yo-strip
	python3 tools/analyze.py yo yo-strip

analyze-functions: yo
	python3 tools/analyze.py yo --functions

AWESOME_OCAP=$(HOME)/projects/awesome-ocap
ocap-devtools:
	mkdir -p docs/
	cp -rp $(AWESOME_OCAP)/style-guide/*.md docs/
	mkdir -p tools
	cp -rp $(AWESOME_OCAP)/tools/disciplined_python_check.py tools/

zig-version:
	./tools/zig-version.sh

zig-tree-check:
	./tools/zig-tree-check.sh

clean:
	rm -f ./yo yo-strip hello.bin notify.bin
