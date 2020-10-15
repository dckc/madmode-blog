----
title: What I use: emacs to vs-codium
tags: ["writing", "programming", "collaboration"]
published: false
date: 2020-10-15
----

I'm an emacs addict but the Agoric and RChain communities, like many others, are picking up vs-code.

I use vs-codium, the community build with the non-open-source bits trimmed off. It seems to use a different plugin market; for example, the live sharing collaboration plugin wasn't in the usual place. But it's easy enough to find with a web search, download, and install.

I'm also outfitting a new machine, which makes me wonder: how to manage the list of plugins?

The answer to how to manage my emacs config and packages is mostly: I don't. I'm addicted to flycheck for python, but each time I outfit a new machine, the norms for setting it up have probably evolved sufficiently that starting fresh with a web search is probably less trouble than trying to get some old, poorly maintained config code to work.

I mostly don't customize my emacs setup in case I want to work at someone else's computer... or a computer that I'm outfitting.

boy this font is small... ah... zoom-in just like a web browser. vs-codium is an electron app, after all.

not sure I like the blue background either...

ugh... it crashed when I tried out the zen mode. But it didn't lose my work. IntegrityIsJobOne.

hp laptop customization: tracpad click-on-touch

ctrl key is pretty far out of the way. I did swap with alt on my chromebook. Might try that out.

blogging... vs-codium says python isn't installed. Let's try `nix-shell` and `shell.nix`... ok, wish for `pipenv` granted... but then `pipenv install` fails with some obscure error message. Oh well... the elves at netlify grok. So I'll just use local markdown preview rather than the `site` script.

```
[connolly@capnb:~/projects/madmode-blog]$ nix-shell

[nix-shell:~/projects/madmode-blog]$ pipenv install
Installing dependencies from Pipfile.lock (0e78e6)…
An error occurred while installing argh==0.15.1 --hash=sha256:8cca1201af8c15b7e77577ecddbca7cc867f943cb0bd2fb5c38461662b1aa80b! Will try again.
...
--hash=sha256:e5f4a1f98b52b18a93da705a7458e55afb26f32bff83ff5d19189f92462d65c4! Will try again.
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 15/15 — 00:00:00
Installing initially failed dependencies…
  ☤  ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 15/15 — 00:00:01
[pipenv.exceptions.InstallError]:   File "/nix/store/gsrk6xbwymglyy4yw8lamx1gccv3ygmn-pipenv-2018.11.26/lib/python3.7/site-packages/pipenv/cli/command.py", line 254, in install
[pipenv.exceptions.InstallError]:       editable_packages=state.installstate.editables,
[pipenv.exceptions.InstallError]:   File "/nix/store/gsrk6xbwymglyy4yw8lamx1gccv3ygmn-pipenv-2018.11.26/lib/python3.7/site-packages/pipenv/core.py", line 1874, in do_install
[pipenv.exceptions.InstallError]:       keep_outdated=keep_outdated
[pipenv.exceptions.InstallError]:   File "/nix/store/gsrk6xbwymglyy4yw8lamx1gccv3ygmn-pipenv-2018.11.26/lib/python3.7/site-packages/pipenv/core.py", line 1253, in do_init
[pipenv.exceptions.InstallError]:       pypi_mirror=pypi_mirror,
[pipenv.exceptions.InstallError]:   File "/nix/store/gsrk6xbwymglyy4yw8lamx1gccv3ygmn-pipenv-2018.11.26/lib/python3.7/site-packages/pipenv/core.py", line 862, in do_install_dependencies
[pipenv.exceptions.InstallError]:       _cleanup_procs(procs, False, failed_deps_queue, retry=False)
[pipenv.exceptions.InstallError]:   File "/nix/store/gsrk6xbwymglyy4yw8lamx1gccv3ygmn-pipenv-2018.11.26/lib/python3.7/site-packages/pipenv/core.py", line 681, in _cleanup_procs
[pipenv.exceptions.InstallError]:       raise exceptions.InstallError(c.dep.name, extra=err_lines)
[pipenv.exceptions.InstallError]: []
[pipenv.exceptions.InstallError]: ['Traceback (most recent call last):', '  File "/home/connolly/.local/share/virtualenvs/madmode-blog-1UB6vfSQ/bin/pip", line 5, in <module>', '    from pip._internal.cli.main import main', 'ImportError: No module named main']
ERROR: ERROR: Package installation failed...
```

I much prefer docopt to argh anyway.

bearded theme solarized light. I like it.

yikes! how do I push this without magit?!