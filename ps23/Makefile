
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
