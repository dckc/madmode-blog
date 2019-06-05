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
