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


