---
title: Javascript on genode, genode on HP Envy 15
date: 2020-07-12
published: true
tags: ["capabilities", "genode", "javascript", "hardware"]
summary: "Achievements unlocked: Moddable XS JavaScript engine onr genode and HP
         Envy Notebook PC running free software."
---

Genode is a microkernel operating system with capability-based
security; in the 20.05 release they added [capability-based security
using seccomp on Linux][lxcap]. That got me excited enough to make
some real progress on JavaScript on Genode using the Moddable XS
engine and on Genode on an HP Envy laptop.

[lxcap]: https://genode.org/documentation/release-notes/20.05#Capability-based_security_using_seccomp_on_Linux

In [genode-js-xs](https://github.com/dckc/genode-js-xs) I got this
JavaScript code running on genode:

```
export default function main() {
    let message = "Hello, world - sample";
    trace(message + "\n");
}
```

It works like this, once it's built (see below):

```
goa-hello$ goa run
[goa-hello:make] recursive make: make
Genode 20.02-1-gac1b2ec24e
17592186044415 MiB RAM and 8997 caps assigned to init
[init -> goa-hello] Hello before libc
[init -> goa-hello] hello via stdio
[init -> goa-hello] Hello in libc
[init -> goa-hello] lin_xs_cli: loading top-level main.js
[init -> goa-hello]  lin_xs_cli: loaded
[init -> goa-hello] lin_xs_cli: invoking main(argv)
[init -> goa-hello] Hello, world - sample
[init -> goa-hello] main() returned immediate value (not a promise). exiting
[init -> goa-hello] Warning: rtc not configured, returning 0
Warning: blocking canceled in entrypoint constructor
[init] child "goa-hello" exited with exit value 0
```

I started with the hello package from then [Nov 2019 article
introducing goa](https://genodians.org/nfeske/2019-11-25-goa).

Then I grabbed the
[helloworld](https://github.com/Moddable-OpenSource/moddable/tree/public/examples/helloworld)
example from the Moddable XS SDK, generated C sources, and got it to
build.

Then I worked out getting `goa run` to work. My `artifacts` is
a bit of a kludge: it reaches out from `var/build` back to `src/bin`.

### before `goa build`: `gensrc`, `genode_platform`

There's a bit of an impedence mismatch between `goa build` and the
[Moddable SDK](https://github.com/Moddable-OpenSource/moddable/), so
use `make -C src gensrc` to generate C etc. before running `goa
build`.

We also extend the Moddable SDK to add a `genode` platform
using `make -C src genode_platform`.

### Next Steps

  - **event loop**: Figure out how to integrate the [port of glib to
    genode](https://github.com/genodelabs/genode-world/blob/master/ports/glib.port)
    to turn the event loop, which is currently commented out, back on.

  - **nix and dhall**: Compare goa to [genodepkgs](https://git.sr.ht/~ehmry/genodepkgs)


## NixOS 20.03 and Genode Sculpt 20.02 on the HP Envy 15

When my son upgraded his gaming laptop last year, I got his
hand-me-down [HP ENVY
15z-j100](https://support.hp.com/us-en/product/hp-envy-15-j100-notebook-pc-series/5401187/model/6521450?sku=E1R44AV)
and tried to boot it from free software.  I got Windows so messed up
that it could neither boot nor repair itself, so I set it aside in
frustration.

Prompted by my success with js on genode, I tried a Ubuntu 20.04 USB
stick (that I had made for my other son, who uses linux for his gaming
PC) and lo, it worked the first time. Ubuntu has gone to the trouble
to get their installation media working with secure boot.

[secure boot for NixOS](https://github.com/NixOS/nixpkgs/pull/53901)
looks really bleeding edge, but with a better understanding based on
[EFI Boot Loaders for Linux: Dealing with Secure
Boot](https://www.rodsbooks.com/efi-bootloaders/secureboot.html#hp705)
by Rod Smith, I managed to turn secure boot off and get NixOS installed.

With all this momentum, I did not give up when booting [Sculpt OS
20.02](https://genode.org/download/sculpt) quit with a just [screen
full of \(?\)s](https://github.com/alex-ab/g2fg/issues/1). They only
document support for Intel CPUs and this has an AMD A10-5750M, so it
looked like an AHCI driver problem or some such. But the screen wasn't
locked altogether. It responded to enter and to `clear`... aha!  It's
a grub prompt with a missing font. `terminal_output console` dealt
with the font issue and the solution turned out to be changing `hd0`
to `hd1` in a grub config file. Genode has no ath9k driver, so wifi
isn't working, but I have plenty of ethernet ports and cables. :)
