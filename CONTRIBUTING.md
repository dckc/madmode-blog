## Dependencies

Use `pipenv install` to install dependencies.


### Dependency Bootstrap: direnv, pipenv

 - direnv: I used `nix-env -i direnv`
   - The usual `apt install direnv` most likely works fine.
   - To get nix, I used their curl/bash recipe.
 - pipenv: I used `~/pyenv/pip-user/pip install pipenv --user`
   - to get pip, I used `virtualenv ~/pyenv/pip-user`
     - to get virtualenv, I downloaded the .tar file from pypi

Then `direnv allow` consults `.envrc` which says to use pipenv layout.


### Sync requirements.txt with Pipfile

```
(grep '^#' requirements.txt; pipenv lock --requirements) >,tmp && mv ,tmp requirements.txt
```

## stuff from Pipfile

```
# direct imports from ./site, in source order
```

```
# ISSUE: bummer. Flask-Markdown uses positional arguments
# ISSUE: I can haz footnotes?
# https://python-markdown.github.io/change_log/release-3.0/#positional-arguments-deprecated
```

```
# https://github.com/python-poetry/poetry/issues/1487
# https://github.com/Python-Markdown/markdown/blob/master/markdown/util.py#L85
# <PY310 use backport
importlib_metadata = "*"
```
