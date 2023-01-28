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
