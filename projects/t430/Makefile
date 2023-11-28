# NOTE: many commands require root; use sudo make ...

# Disk is partitioned for dual boot, inspired by
#
# - Starting an existing Linux installation from Sculpt
#   April 23 2021 by Johannes Schlatow
#   https://genodians.org/jschlatow/2021-04-23-start-existing-linux-from-sculpt
DISK=/dev/sda

sda-sfdisk.txt:
	sfdisk --list $(DISK) >$@

sda-sfdisk.dump:
	sfdisk --dump $(DISK) >$@

sda-sfdisk.json:
	sfdisk --json $(DISK) >$@


# Original VM setup based on...
#
#  - How to install a fresh VM on Sculpt
#    October 27 2022 by Johannes Schlatow
#    https://genodians.org/jschlatow/2022-10-27-fresh-vm-on-sculpt
GENODE=/GENODE

# Virtual Disk Image (vdi)
#

machine.vdi:
	exit 1 # don't do this again
	VBoxManage createmedium --filename $(GENODE)/vm/debian/machine.vdi \
	                          --size 10000 --variant Fixed

# Note especially the UUID, for use in machine.vbox6
machine.vdi.info:
	VBoxManage showmediuminfo $(GENODE)/vm/debian/machine.vdi | tee $@


# legacy grub for booting in vbox
# https://genodians.org/jschlatow/2021-04-23-start-existing-linux-from-sculpt

legacy-grub:
	grub-install --target=i386-pc --boot-directory=/boot /dev/sda
	grub-mkconfig -o /boot/grub/grub.cfg

# "If CONFIG_SATA_AHCI=m, make sure that your initramfs contains the
# ahci module"
check-ahci:
	zgrep CONFIG_SATA_AHCI /boot/config-5.15.0-56-generic
	lsinitramfs /boot/initrd.img | grep ahci

# CONFIG_SATA_AHCI=m
# CONFIG_SATA_AHCI_PLATFORM=m

# usr/lib/modules/5.15.0-58-generic/kernel/drivers/ata/ahci.ko

vm-launcher: \
	$(GENODE)/config/22.10/launcher/vm \
	$(GENODE)/vm/debian/machine.vbox6 \
	$(GENODE)/vm/debian/linux.vmdk

# "in order to make the system bootable with VirtualBox but not
# interfere with the partitions that are used by my Sculpt system, I
# must prepare a special vmdk file:"

vmdk: $(GENODE)/vm/debian/linux.vmdk $(GENODE)/vm/debian/linux-pt.vmdk

linux.vmdk:
	VBoxManage internalcommands createrawvmdk -filename linux.vmdk \
	  -rawdisk /dev/sda -partitions 1,4,5,6 -relative

$(GENODE)/vm/debian/linux.vmdk: linux.vmdk
	cp $< $@

$(GENODE)/vm/debian/linux-pt.vmdk: linux-pt.vmdk
	cp $< $@

# http://genodians.org/skalk/2019-03-18-hybrid-packages

hybrid-packages: \
	GENODE/depot/local/pkg/vbox6 \
	$(GENODE)/depot/local/raw/vbox6/2022-04-27/init.config

GENODE/depot/local/pkg/vbox6/2022-10-13/README: $(GENODE)/depot/local/pkg/vbox6/2022-10-13/README
	mkdir -p GENODE/depot/local/pkg
	mkdir -p GENODE/depot/local/raw
	cp -r $(GENODE)/depot/genodelabs/pkg/vbox6 GENODE/depot/local/pkg/
	cp -r $(GENODE)/depot/genodelabs/raw/vbox6 GENODE/depot/local/raw/

# Then you alter the configuration of the Virtualbox component in depot/local/raw/vbox5-nova-sculpt/{yyyy-mm-dd}/init.config

$(GENODE)/depot/local/raw/vbox6/2022-04-27/init.config: GENODE/depot/local/raw/vbox6/2022-04-27/init.config
	mkdir -p $(GENODE)/depot/local/pkg
	mkdir -p $(GENODE)/depot/local/raw
	cp -r GENODE/depot/local/raw/vbox6 $(GENODE)/depot/local/raw/vbox6
	cp -r GENODE/depot/local/pkg/vbox6 $(GENODE)/depot/local/pkg/vbox6

$(GENODE)/config/22.10/launcher/vm: GENODE/config/22.10/launcher/vm
	cp $< $@

$(GENODE)/vm/debian/machine.vbox6: GENODE/vm/debian/machine.vbox6
	cp $< $@
