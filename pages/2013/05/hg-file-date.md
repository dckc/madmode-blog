date: 2013-05-04
published: true
tags: [scm, integrity]
title: Preserving file modification dates in mercurial

Sometimes I come back to a file I worked on and I wish I would have
checked it in. I like to pretend I did by using the file modification
date as the commit date. I just `ls -l xyz` and then `hg commit -dWHEN
xyz`.  But converting the `ls` output into mercurial date format is
error prone; I always get it wrong and then have to `hg help dates`.

This is something the computer can do for me, no?

Yes: the gnu `date` command and `hg` both support RFC822 date format:

    hg commit -d"`date --rfc-822 --reference=xyz`" xyz

Note the ""s around the ``s. Ah, the joys of shell quoting.

----

p.s. git equivalent:

```
[alias]
        modcommit = "!git add \"$1\" && GIT_AUTHOR_DATE=\"$(date -Iseconds -r \"$1\")\" git commit -m \"WIP: $1\""
```
