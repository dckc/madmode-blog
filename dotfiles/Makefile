# https://stackoverflow.com/a/64068109
makeFileDir := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

TARGETS=$(HOME)/.gitignore $(HOME)/.gitconfig $(HOME)/.bashrc $(HOME)/.hgrc.d \
	$(HOME)/.emacs.d $(HOME)/.config/nix/nix.conf \
	$(HOME)/.local/share/file-manager/actions \
	$(HOME)/.local/share/applications/obsidian.desktop \
	$(HOME)/.local/share/applications/emacs-magit.desktop \
	$(HOME)/.local/bin/obsidian \
	$(HOME)/.local/bin/magit-status \
	$(HOME)/.local/bin/svcmon \
	$(HOME)/.config/autostart/svcmon.desktop

all: $(TARGETS)

$(HOME)/.local/share/file-manager/actions:
	mkdir -p $(HOME)/.local/share/file-manager
	ln -s $(makeFileDir)caja-actions $@

$(HOME)/.local/share/applications/obsidian.desktop:
	ln -s $(makeFileDir)applications/obsidian.desktop $@

$(HOME)/.local/share/applications/emacs-magit.desktop:
	ln -s $(makeFileDir)applications/emacs-magit.desktop $@

$(HOME)/.local/bin/obsidian:
	ln -sf $(makeFileDir)bin/obsidian $@

$(HOME)/.local/bin/magit-status:
	ln -sf $(makeFileDir)bin/magit-status $@

$(HOME)/.local/bin/svcmon:
	ln -sf $(makeFileDir)bin/svcmon $@

$(HOME)/.config/autostart/svcmon.desktop:
	ln -s $(makeFileDir)autostart/svcmon.desktop $@

$(HOME)/.config/direnv:
	ln -s $(makeFileDir)direnv $@

$(HOME)/.config/nix/nix.conf:
	mkdir -p $(HOME)/.config/nix
	ln -s $(makeFileDir)nix-config/nix.conf $@

$(HOME)/.emacs.d:
	ln -s $(makeFileDir)/emacs.d $@

$(HOME)/.gitignore:
	ln -s $(makeFileDir).gitignore $@

$(HOME)/.gitconfig:
	ln -s $(makeFileDir)/git-config $@

$(HOME)/.bashrc:
	ln -s $(makeFileDir)/bashrc $@

$(HOME)/.hgrc.d:
	ln -s $(makeFileDir)/hgrc.d $@

clean:
	rm -f $(TARGETS)
