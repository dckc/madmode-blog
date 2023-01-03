title: Toward capabilities all the way down with Genode on a Thinkpad
date: 2023-01-03
tags: [capabilities, security, vm, storage, pc, hardware, osdev]
published: true

In this year's holiday lull, what I really wanted to do was outfit a "capabilities all the way down" [Genode](https://genode.org/) workstation, but I spent most of it recovering from [Flickr going back on their 1TB storage offer](https://blog.flickr.net/en/2022/04/19/update-free-account-limit-changes-and-enforcement-start-may-1-2022/).

Sculpt is Genode-based OS with the [NOVA microhypervisor](http://hypervisor.org/) at the bottom:

> ... the NOVA microhypervisor uses a capability-based authorization model and provides only basic mechanisms for virtualization, spatial and temporal separation, scheduling, communication, and management of platform resources.

NOVA isn't formally verified like seL4, but it's tiny (9,000 LOC):

> ![figure 1](https://user-images.githubusercontent.com/150986/210296418-9ce6f1e6-ce31-4328-96e9-8009a815d7cc.png)  
> Figure 1: Comparison of the TCB size of virtual environments.
> -- [Steinberg 2010](http://hypervisor.org/eurosys2010.pdf)

... not to mention mature: that peer-reviewed release was in 2010 and the [spec](https://github.com/alex-ab/NOVA/blob/a34076e/doc/specification.pdf) last changed in 2014.
It's clearly trustworthy enough for my hobby usage.

For reference, [genode sculpt-22.10 `ports/nova.port`](https://github.com/genodelabs/genode/blob/sculpt-22.10/repos/base-nova/ports/nova.port) points to [NOVA a34076e](https://github.com/alex-ab/NOVA/tree/a34076e), modified Sep 29. So they do continue to make the occasional tweak here and there to the C++ code... prompted by Sculpt usage, I suspect.

The Sculpt release notes include a tutorial on how to boot it from a USB drive and play around with it; I managed to get that far back in 2018. This time, I got a more clear understanding of how [persistent configuration](https://genode.org/documentation/articles/sculpt-22-10#Making_customizations_permanent) on a partition of the USB drive works. A big clue is that the built-in "inspect" view is plenty for command-line file manipulation; there's no need to install and configure all the components of a shell.

I wanted to reproduce Schlatow's results from [Starting an existing Linux installation from Sculpt](https://genodians.org/jschlatow/2021-04-23-start-existing-linux-from-sculpt). I managed to

 - [partition the hard drive](https://github.com/dckc/madmode-blog/issues/49#issuecomment-1356447232)
   - considered [nix declarative disk partitioning with disko](https://github.com/nix-community/disko) a la [McGee's notes](https://lobste.rs/s/aamjm7/setting_up_my_new_laptop_nix_style)
     - learned a bit more about [nix flakes](https://nixos.org/manual/nix/unstable/command-ref/new-cli/nix3-flake.html)
     - tried to make my own flake; re-discovered [my problem with nix](https://lobste.rs/s/ff54p1/how_nix_nixos_get_so_close_perfect#c_po5s5h): unlike `apt` where if you get an option wrong, some C code tells you that you got an option wrong, nix just passes the wrong option down into interpreted code where you eventually get “string found where integer expected” or some such. As Phil Karlton would say, "yet another interpreted language without a debugger."
 - install linux on the internal SDD
 - install genode on another partition
   - though I couldn't get the grub config to work automatically

and I downloaded the components to run a VM, but when I tried to start it up, it couldn't find `/machine.vbox6`:

```
[runtime] child "vbox6"
[runtime]   RAM quota:  4402952K
[runtime]   cap quota:  7966
...
[runtime -> vbox6 -> vbox] main     Executable:  /virtualbox6
[runtime -> vbox6 -> vbox] Error: failed to init machine from settings
[runtime -> vbox6 -> vbox] Runtime error opening '/machine.vbox6' for reading: -102 (File not found.).
[runtime -> vbox6 -> vbox] /data/depot/genodelabs/src/vbox6/2022-10-11/src/virtualbox6/src/VBox/Main/src-server/MachineImpl.cpp[499] (nsresult Machine::initFromSettings(VirtualBox*, const com::Utf8Str&, const com::Guid*))
[core] attempted exec at non-executable memory (EXEC pf_addr=0x271dd78 pf_ip=0x271dd78 from pager_object: pd='init -> runtime -> vbox6 -> vbox' thread='ep') 
[core] page fault, pd='init -> runtime -> vbox6 -> vbox' thread='ep' cpu=0 ip=0x271dd78 address=0x271dd78 stack pointer=0x403fe6b8 qualifiers=0x15 IrUwP reason=3
[core] no RM attachment (READ pf_addr=0x0 pf_ip=0x16bb302 from pager_object: pd='init -> runtime -> vbox6 -> vbox' thread='Watcher') 
[core] page fault, pd='init -> runtime -> vbox6 -> vbox' thread='Watcher' cpu=0 ip=0x16bb302 address=0x0 stack pointer=0x409feb00 qualifiers=0x4 irUwp reason=1
```

After a [a bit of diigoing](https://www.diigo.com/user/dckc-madmode), I came to the conclusion that there's a significant gap in my education around using VirtualBox in general, never mind in Genode.
