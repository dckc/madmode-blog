Makefile conventions (evolved from a private ops repo):

- `make` for named checkpoints and target selection
- short targets; loops, conditionals, traps → script
- AWK for light text transforms (dedicated `.awk` if non-trivial)
- keep `help` accurate and current

`help` convention: `## description` before the target line, extracted by a small awk program that pairs `##` comments with the next `target:` line.

Example from [`opencode-indicator.mk`](../dotfiles/opencode-indicator.mk):

```makefile
## Link indicator script and systemd services, then reload
all: $(TARGETS)
	systemctl --user daemon-reload

## Show available targets
help:
	@awk 'BEGIN {d=""} /^## / {d=substr($$0,4)} \
	  /^[a-zA-Z0-9_.-]+:/ {if(d) {split($$0,t,":"); \
	  printf "  %-12s  %s\n", t[1], d; d=""}}' \
	  $(MAKEFILE_LIST)
```

Use `$(CURDIR)` for the working directory (set by `make -C`). No need for the
`$(makeFileDir)` dance — `make -C dotfiles` sets CWD, so `$(CURDIR)` resolves
against `dotfiles/`. Use `$(HOME)` for the target's home.

Use `ln -sf` for durable installation targets rather than copy, so updates flow
from the source tree automatically.

Even for package installation, target the actual installed file so make's
dependency model skips it when already present:

```makefile
AYATANA_PKG  = gir1.2-ayatanaappindicator3-0.1
AYATANA_DOC  = /usr/share/doc/$(AYATANA_PKG)/copyright

all: $(AYATANA_DOC) $(TARGETS)
	systemctl --user daemon-reload

$(AYATANA_DOC):
	sudo apt-get install -y $(AYATANA_PKG)
```

Factor the long path into a variable so the two occurrences are easy to verify
as identical.  Now `make all` runs `sudo apt-get install` only when the package
is missing — no explicit idempotence check, no phony alias.  Prefer
architecture-independent paths like `/usr/share/doc/<pkg>/copyright` so the
target works across platforms.
