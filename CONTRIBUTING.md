## Building

This is a static site; it should build just about anywhere:

```
pipenv install
pipenv run python ./site build
pipenv run python -m pagefind --site build
```

`./site build` freezes the Flask app into `build/` (Frozen-Flask), and
pagefind adds a search index. The result is plain files. Flask, Werkzeug,
and Jinja never serve a live request, and every input (pages, templates,
images) is my own content.


## Python

The pinned version is in `runtime.txt` and in `python_version` in
`Pipfile`; keep them in sync. Any way of getting that version works:
system packages, `uv python`, mise, ...

Python has one feature release per year (October), each supported for 5
years, no LTS (PEP 602). So the pinned version goes end-of-life on a
predictable schedule, and after that, tools that install Python may stop
offering it. Plan to revisit in October.

 - 3.10: EOL Oct 2026; moved off it 2026-10-29
 - 3.13: current; EOL **Oct 2029**

Known blockers for 3.14 (as of 2026-10-29):

 - Flask 2.2 uses `pkgutil.get_loader`, removed in 3.14 → needs Flask 3.x,
   and so Werkzeug 3.x and Flask 3-compatible Frozen-Flask, FlatPages,
   Flask-Assets
 - Pillow 11 has no cp314 wheels → `pillow = "~=12.0"` or later
 - `site` uses `Image.ANTIALIAS`, removed in Pillow 10 (not reached by
   the current build, apparently)


Builds are reproducible except the timestamp in `feeds/posts/default`,
so `diff -r` of before/after `build/` dirs is a good check when changing
Python or dependencies.


## pipenv

`Pipfile.lock` is the source of truth for what gets installed. Always run
things via `pipenv run`, rather than relying on which `python` is first on
`PATH`.

I install pipenv with `pipx install pipenv`. When the system Python
upgrades (e.g. 3.12 → 3.14), the pipx venv breaks with
`ModuleNotFoundError: No module named 'pipenv'`; fix with
`pipx reinstall pipenv`.


### Strategy: keep dependencies boring

Security alerts (Dependabot) are mostly moot here: they need untrusted
images, requests, or templates, and there are none. I bulk-dismissed them
as "tolerable risk" 2026-10-29. Don't chase upgrades for their sake; the
goal is a build that's boring, and the main thing that makes it
interesting is the Python version reaching end-of-life.


## Hosting: Netlify

From [Migrated from github pages to netlify for continuous deployment,
SSL](https://www.madmode.com/2019/netlify-deploy-https.html) (2019):

> **Holy shnikeys! it worked 1st try with no tweaks whatsoever!** I told
> it my build command was `./site build` and it picked up my
> `requirements.txt`, installed the dependencies, built the site and
> deployed it.

It has mostly stayed out of the way since: it runs the build command
above (`netlify.toml`) and serves `build/`. It reads
`runtime.txt` and installs that Python via mise. Little else here is
Netlify-specific.

The build environment does change underneath: the image name stays
"noble-new-builds" while the image itself is updated. In Apr 2026, an
update put mise shims ahead of the pipenv virtualenv on `PATH`, so plain
`python` lost the site's packages; hence `pipenv run` everywhere (02d5b22).
