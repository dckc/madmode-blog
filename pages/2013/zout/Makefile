# Assemble a Zope 2.7.7 instance from the 2004 var/ backup and run zout2.py.
#
# The backup tgz is a plain var/ tree, so extract it straight into a
# writable /tmp instance (the read-only squashfs mount blocked Zope's
# startup writes: Data.fs.lock, product install, app init).

TGZ      ?= /run/media/connolly/sannex1tb/annex/personal-sites/zope-migrate/2004zbak/zope-var-bak.tgz
INSTANCE ?= /tmp/zope-instance
OUT      ?= /tmp/zout-out
PATH_CAP ?= /

help:
	@echo 'make instance   assemble $(INSTANCE) from $(TGZ)'
	@echo 'make products   install the 2004 third-party products (ZWiki, LocalFS)'
	@echo 'make zout       run zout2.py $(PATH_CAP) $(OUT)'
	@echo 'make clean      remove $(INSTANCE) and $(OUT)'

instance: $(INSTANCE)/.instance

$(INSTANCE)/.instance: $(TGZ) zope.conf.in
	mkdir -p $(INSTANCE)/etc $(INSTANCE)/log $(INSTANCE)/Products $(INSTANCE)/Extensions $(INSTANCE)/import
	tar -xzf $(TGZ) -C $(INSTANCE)
	sed 's|@INSTANCE@|$(INSTANCE)|' zope.conf.in > $(INSTANCE)/etc/zope.conf
	touch $@

zout: $(INSTANCE)/.instance
products: $(INSTANCE)/.products

$(INSTANCE)/.products: $(INSTANCE)/.instance flake.nix flake.lock
	rm -rf $(INSTANCE)/Products
	cp -rL --no-preserve=ownership $$(nix build --no-link --print-out-paths .#products) $(INSTANCE)/Products
	chmod -R u+w $(INSTANCE)/Products
	touch $@

	mkdir -p $(OUT)
	INSTANCE_HOME=$(INSTANCE) nix develop --command python zout2.py "$(PATH_CAP)" "$(OUT)"

clean:
	rm -rf $(INSTANCE) $(OUT)

.PHONY: help instance products zout clean
