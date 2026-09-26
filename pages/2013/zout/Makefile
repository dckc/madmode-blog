# Assemble a Zope 2.7.7 instance from the 2004 Zope data and run zout2.py.
#
# Use the loose 2004zbak/Data.fs (last txn 2004-09-22), not the tgz's
# var/Data.fs (2004-08-02): the tgz dump is missing TheOriginalHypertext,
# while 2004zbak/Z2.log shows the page being served in September 2004.
# Copy it into a writable /tmp instance — the read-only squashfs mount
# blocked Zope's startup writes (Data.fs.lock, product install, app init).

DATA_FS  ?= /home/connolly-annex-2025-01/personal-sites/zope-migrate/2004zbak/Data.fs
INSTANCE ?= /tmp/zope-instance
OUT      ?= /tmp/zout-out
PATH_CAP ?= /

help:
	@echo 'make instance   assemble $(INSTANCE) around $(DATA_FS)'
	@echo 'make products   install the 2004 third-party products (ZWiki, LocalFS)'
	@echo 'make zout       run zout2.py $(PATH_CAP) $(OUT)'
	@echo 'make clean      remove $(INSTANCE) and $(OUT)'

instance: $(INSTANCE)/.instance

$(INSTANCE)/.instance: $(DATA_FS) zope.conf.in Makefile
	mkdir -p $(INSTANCE)/etc $(INSTANCE)/log $(INSTANCE)/Products $(INSTANCE)/Extensions $(INSTANCE)/import $(INSTANCE)/var
	cp $(DATA_FS) $(INSTANCE)/var/Data.fs
	sed 's|@INSTANCE@|$(INSTANCE)|' zope.conf.in > $(INSTANCE)/etc/zope.conf
	touch $@

products: $(INSTANCE)/.products

$(INSTANCE)/.products: $(INSTANCE)/.instance flake.nix flake.lock
	rm -rf $(INSTANCE)/Products
	cp -rL --no-preserve=ownership $$(nix build --no-link --print-out-paths .#products) $(INSTANCE)/Products
	chmod -R u+w $(INSTANCE)/Products
	touch $@

zout: $(INSTANCE)/.products
	mkdir -p $(OUT)
	INSTANCE_HOME=$(INSTANCE) nix develop --command python zout2.py "$(PATH_CAP)" "$(OUT)"

clean:
	rm -rf $(INSTANCE) $(OUT)

.PHONY: help instance products zout clean
