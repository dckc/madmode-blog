
for fun, I fed du output into https://bost.ocks.org/mike/treemap/  #sysadmin
https://twitter.com/dckc/status/751895518192672768

but I couldn't find it.

So:


connolly@pav:~$ find . -printf '%T+ %T@ %s %p\n' >/tmp/index-files-home.txt
connolly@pav:~$ grep 2016-07-09 /tmp/index-files-home.txt |grep -v cargo/registry |grep -v node_modules

2016-07-09+16:40:23.3899267530 1468100423.3899267530 4096 ./disk-space-fun/Zoomable Treemaps_files
