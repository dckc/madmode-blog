# agentsview — durable installation
# Usage:  make -C dotfiles -f agentsview.mk

TARGETS = \
	$(HOME)/.local/bin/agentsview \
	$(HOME)/.local/bin/agentsview-indicator.py \
	$(HOME)/.config/systemd/user/agentsview.service \
	$(HOME)/.config/systemd/user/agentsview-indicator.service

## Register the service and autostart the tray icon
all: deps $(TARGETS)
	systemctl --user daemon-reload && systemctl --user enable --now agentsview-indicator.service

## Ensure agentsview binary is installed via uv
deps:
	@uv tool install agentsview 2>/dev/null || uvx agentsview --version >/dev/null
	@echo "agentsview $$(agentsview --version 2>/dev/null || uvx agentsview --version)"

$(HOME)/.local/bin/agentsview:
	uv tool install agentsview

$(HOME)/.local/bin/agentsview-indicator.py:
	mkdir -p $(HOME)/.local/bin
	ln -sf $(CURDIR)/bin/agentsview-indicator.py $@

$(HOME)/.config/systemd/user/agentsview.service:
	mkdir -p $(HOME)/.config/systemd/user
	ln -sf $(CURDIR)/systemd/user/agentsview.service $@

$(HOME)/.config/systemd/user/agentsview-indicator.service:
	mkdir -p $(HOME)/.config/systemd/user
	ln -sf $(CURDIR)/systemd/user/agentsview-indicator.service $@

## Remove all symlinks created here
clean:
	rm -f $(TARGETS)

## Show available targets
help:
	@awk 'BEGIN {d=""} /^## / {d=substr($$0,4)} /^[a-zA-Z0-9_.-]+:/ \
	  {if(d) {split($$0,t,":"); printf "  %-12s  %s\n", t[1], d; d=""}}' \
	  $(MAKEFILE_LIST)

.PHONY: all deps clean help
