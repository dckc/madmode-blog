# opencode web indicator — durable installation
# Usage:  make -C dotfiles -f opencode-indicator.mk
# (make -C sets CWD, so relative paths resolve against dotfiles/)

AYATANA_PKG  = gir1.2-ayatanaappindicator3-0.1
AYATANA_DOC  = /usr/share/doc/$(AYATANA_PKG)/copyright
PYGOBJECT_PKG = python3-gi
PYGOBJECT_DOC = /usr/share/doc/$(PYGOBJECT_PKG)/copyright

TARGETS = \
	$(HOME)/.local/bin/opencode-indicator.py \
	$(HOME)/.local/icons/opencode.svg \
	$(HOME)/.config/systemd/user/opencode-web.service \
	$(HOME)/.config/systemd/user/opencode-indicator.service

## Ready the Python indicator, register the service, and autostart the tray icon
all: deps $(TARGETS)
	systemctl --user daemon-reload && systemctl --user enable --now opencode-indicator.service

## Debian Ayatana + PyGObject packages (sudo)
deps: $(AYATANA_DOC) $(PYGOBJECT_DOC)
	@apt-cache show $(AYATANA_PKG) 2>/dev/null | grep -E '^(Version|SHA256):'
	@apt-cache show $(PYGOBJECT_PKG) 2>/dev/null | grep -E '^(Version|SHA256):'

$(AYATANA_DOC):
	sudo apt-get install -y $(AYATANA_PKG)

$(PYGOBJECT_DOC):
	sudo apt-get install -y $(PYGOBJECT_PKG)

# So systemd's ExecStart=%h/.local/bin/opencode-indicator.py resolves
$(HOME)/.local/bin/opencode-indicator.py:
	mkdir -p $(HOME)/.local/bin
	ln -sf $(CURDIR)/bin/opencode-indicator.py $@

# So the indicator can find its icon
$(HOME)/.local/icons/opencode.svg:
	mkdir -p $(HOME)/.local/icons
	ln -sf $(CURDIR)/icons/opencode.svg $@

# So `systemctl --user {start,stop} opencode-web` works
$(HOME)/.config/systemd/user/opencode-web.service:
	mkdir -p $(HOME)/.config/systemd/user
	ln -sf $(CURDIR)/systemd/user/opencode-web.service $@

# So the tray icon appears without manual launch after login
$(HOME)/.config/systemd/user/opencode-indicator.service:
	mkdir -p $(HOME)/.config/systemd/user
	ln -sf $(CURDIR)/systemd/user/opencode-indicator.service $@

## Remove all symlinks created here
clean:
	rm -f $(TARGETS)

## Show available targets
help:
	@awk 'BEGIN {d=""} /^## / {d=substr($$0,4)} /^[a-zA-Z0-9_.-]+:/ \
	  {if(d) {split($$0,t,":"); printf "  %-12s  %s\n", t[1], d; d=""}}' \
	  $(MAKEFILE_LIST)

.PHONY: all deps clean help
