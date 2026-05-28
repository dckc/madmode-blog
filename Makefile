yo: yo.zig hello.bin notify.bin
	zig build-exe -O ReleaseSmall --color off --name yo yo.zig

hello.bin notify.bin: generate_payload.py
	python3 generate_payload.py

run: yo
	./yo

test: hello.bin notify.bin
	python3 send_test.py

trace: yo
	strace -e trace=read,write ./yo

clean:
	rm -f ./yo hello.bin notify.bin
