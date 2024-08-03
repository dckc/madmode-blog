
# per https://guix.gnu.org/manual/en/html_node/Invoking-guix-system.html

build: etc/config.scm
	guix system build -d $<

# enable networking; 1 GiB of RAM
VM_HW_FLAGS=-m 1024 -smp 2 -nic user,model=virtio-net-pci

HEADLESS=--no-graphic

vm: etc/config.scm
	guix system vm $< $(HEADLESS)

# NOTE: the root file system of the VM is mounted volatile
# TODO: --expose read-only, --share read/write
run: etc/config.scm
	$$(guix system vm $< $(HEADLESS)) $(VM_HW_FLAGS)

##
# North American Substitutes
#
# https://lists.gnu.org/archive/html/guix-devel/2024-07/msg00033.html
authz-us: genenetwork.org.pub
	sudo guix archive --authorize < $<

authz-guix2: guix2.pub
	sudo guix archive --authorize < $<

##
# Partition, format physical disk

TARGET=/dev/disk/by-id/ata-Samsung_SSD_860_EVO_500GB_S598NJ0NA42542A

restore-partition-table: partition-table.bak
	sudo sfdisk $(TARGET) < $<

partition-table.bak: $(TARGET) init-partition-table efi-partition root-partition
	sudo sfdisk -d $(TARGET) | tee $@

init-partition-table: $(TARGET)
	sudo parted -s $(TARGET) -- mklabel gpt

efi-partition: $(TARGET)
	# creating a new EFI system partition
	# per https://wiki.archlinux.org/title/Parted
	sudo parted -s $(TARGET) -- mkpart ESP fat32 1MiB 1024MiB
	sudo parted -s $(TARGET) -- set 1 esp on
	sudo parted -s $(TARGET) -- print

root-partition: $(TARGET)
	# one root partition using 100% of remaining space
	sudo parted -s $(TARGET) -- mkpart ps23-root ext4 1024MiB 100%

format-target: $(TARGET)-part1 $(TARGET)-part2
	sudo mkfs.vfat -n ESP $$(realpath $(TARGET)-part1)
	sudo mkfs.ext4 -L ps23-root -F $$(realpath $(TARGET)-part2)

mount-target:
	sudo mount $$(realpath $(TARGET)-part2) /mnt/
	sudo mkdir -p /mnt/boot/efi
	sudo mount $$(realpath $(TARGET)-part1) /mnt/boot/efi

unmount-target:
	sudo umount /mnt/boot/efi
	sudo umount /mnt

init: etc/config.scm
	# herd start cow-store /mnt
	mkdir -p /mnt/etc
	cp $< /mnt/etc/config.scm
	guix system init /mnt/etc/config.scm /mnt

etc/config.scm: dckc.keys

dckc.keys:
	wget https://github.com/dckc.keys
