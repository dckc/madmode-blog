# https://stackoverflow.com/a/64068109
makeFileDir := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

TARGETS=$(HOME)/.gitconfig $(HOME)/.bashrc $(HOME)/.hgrc.d \
	$(HOME)/.emacs.d $(HOME)/.config/nix/nix.conf

all: $(TARGETS)

$(HOME)/.config/direnv:
	ln -s $(makeFileDir)direnv $@

$(HOME)/.config/nix/nix.conf:
	mkdir -p $(HOME)/.config/nix
	ln -s $(makeFileDir)nix-config/nix.conf $@

$(HOME)/.emacs.d:
	ln -s $(makeFileDir)/emacs.d $@

$(HOME)/.gitconfig:
	ln -s $(makeFileDir)/git-config $@

$(HOME)/.bashrc:
	ln -s $(makeFileDir)/bashrc $@

$(HOME)/.hgrc.d:
	ln -s $(makeFileDir)/hgrc.d $@

clean:
	rm -f $(TARGETS)
