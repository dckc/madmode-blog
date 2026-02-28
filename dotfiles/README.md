# Dotfiles

Mostly I avoid bespoke configuration to minimize friction when I
outfit a new computer or use someone else's.

But I also have a habit of using version control to record when I
learned things; for example:

 - 2019-04-11 14:32 76e4827 How to: Change / Setup bash custom prompt (PS1)

I'm a recovering emacs addict; emacs packaging still seems wierd; I
have been struggling with melpa for ages:

 - 2019-03-15 20:21 efae18a melpa-init

At KUMC, I did a lot of data science work with jupyter, pandas,
and such. Whoever argued with me about conda at that PyData
conference, you were right:

 - 2019-04-11 14:33 ca61c6d bashrc: miniconda

I got addicted to flycheck for python. I got a little annoyed when I
had to reconstruct the configuration. I started pushing it down into
projects using `direnv`, leaving just a bit of global configuration:

 - 2019-05-29 17:49 d472973 direnv hook

While working on rholang, I tried to use emacs for scala dev. It works
OK as a text editor, but a type-aware IDE with integrated test runner
and such is a big boost. Intellij IDEA just works; I never did get
ensime really working.

 - 2019-06-15 10:15 ec41e8a scala / ensime (WIP)
 - 2019-06-15 10:13 b2224eb rholang dev

Agoric is all about JavaScript. We use typescript types (mostly in
JSDoc). I miss flow:

 - 2019-01-12 12:10 b0f6ad7 initial commit: js-dev-flow

But Agoric is also the first place since Convex in the '90s
where I've done C development:

 - 2021-01-26 15:33 88f75f5 Moddable SDK C style settings

Lately I have been adding Caja right-click actions for little one-file
workflows (PDF text extraction, Discover CSV to OFX, notebook conversion).
The GUI launch context is exactly where PATH/venv/direnv assumptions break,
so using `uvx` for python tooling keeps those actions self-contained.

 - 2026-02-28 (WIP) caja-actions: notebook conversion via uvx
