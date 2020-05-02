title: My Capability Security 2017 Wish-List
date: 2017-01-02
tags: [security, capabilities, programming, javascript, rust]
published: true

Computers are getting faster, smaller, more connected, and more
capable, but when it comes to security,
[everything is broken][QN14]. Along with correct-by-construction
software (e.g. [Certified Programming with Dependent Types][cpdt]),
the best weapon I see is **object capability discipline**.

Before I get into my wish list of projects and issues, I'd like to
point out [dckc/awesome-ocap](https://github.com/dckc/awesome-ocap),
my list of capability security technology that is ready to use today,
including everything from [seL4](https://sel4.systems/), an open
source operating-system kernel with an end-to-end proof of
implementation correctness and security enforcement to
[Sandstorm](https://sandstorm.io/), a self-hostable SAAS platform.

[QN14]: https://medium.com/message/everything-is-broken-81e5f33a24e1
[cpdt]: http://adam.chlipala.net/cpdt/

## Secure module loading for node.js

The good parts of JavaScript line up well with object capability
discipline, but support in node.js for some of the best parts is
lacking and hence there's no guarantee that calling and enhanced
`sqrt()` from some npm module will not send an HTTP request to launch
missiles.

Mark Miller demonstrated the feasibility of secure loading as far back
as 2011 with [makeSimpleAMDLoader.js][]. I'm trying to fully
understand node's incomplete support for `Object.defineProperty` in
[ses/issues/6](https://github.com/drses/ses/issues/6).

Meanwhile, I'm having fun with Capper; see
[finquick](https://bitbucket.org/DanC/finquick).

[makeSimpleAMDLoader.js]: https://github.com/google/caja/blob/master/src/com/google/caja/ses/makeSimpleAMDLoader.js

## Sandstorm dev tools on Ubuntu 16.04

Ubuntu's 16.04 kernels handle pid namespaces in a way that interferes
with the sandstorm dev tools. Tracking issue:
[2526](https://github.com/sandstorm-io/sandstorm/issues/2526).

I figured out
[how to build sandstorm apps with nix][gist1],
but without the dev tools, the edit/test/debug cycle time is too long.

[gist1]: https://gist.github.com/dckc/2e6b5c8029246ab38c16e254fc3d3f4d

## Capability security for mainstream linux with CloudABI,  capsicum

While considering alternative kernels, I ran into
[a linking issue](https://github.com/dckc/madmode-blog/issues/20) when
trying to build a linux kernel that supports capsicum and
CloudABI. (There was a PPA for capsicum for a while...)

CloudABI or capsicum at work would be _so great_. But it's a long way
off... we're struggling to migrate to SuSE 12 so we can try out
Docker.

For example, a research workflow app I maintain needs to be able to
send mail, but
  - only from one address
  - only using templated bodies
  - only to users who have in some way asked for it

Design sketch: at at investigator request time, user grants
"capability to send app-template mail to addresses X, Y, Z".

As a demonstration, I'm [porting ZeroVault to CloudABI][porting] using
a [FreeBSD vagrant box VM][box]. It's pretty fun since Ed fixes
[my issues][] within a few hours of when I report them.

[box]: https://atlas.hashicorp.com/freebsd/boxes/FreeBSD-11.0-STABLE
[my issues]: https://github.com/NuxiNL/cloudabi-ports/issues?utf8=%E2%9C%93&q=%20is%3Aissue%20author%3Adckc%20
[porting]: https://github.com/dckc/ZeroVault/tree/cloudabi_wsgi

### bus1, Capability-based IPC for Linux

I'm heartened by [momentum around bus1](https://lwn.net/Articles/697191/).

On top of the lack of composability in the chmod/chgroup, there's a
mounting kludge tower of stuff like SELinux and (to a lesser extent?)
AppArmour. I was doing a storage audit and learning how `lsblk` gets
the serial number of my drives. I had heard of udev and systemd, but I
had no idea it uses [netlink](https://en.wikipedia.org/wiki/Netlink)
("a more flexible alternative to ioctl") to communicate with the
kernel.

## Object capability discipline for Docker

Is this even possible? I can't get my head around the Docker security story.

## Uniform, composable FFI and stdlib for pony

Pony aims to be a high-performance capability-secure language. I would
love to see it make some inroads on golang: while go addresses (many
of) the memory-safety issues of C/C++, its standard library is full of
ambient authority and its type system dooms developers to lots of
boilerplate maintenance.

I'm struggling (mostly for time) to convince the pony community that a
reasonably simple [policy][] can eradicate ambient authority from the
standard library.

In discussion of my [network API PR][301], I learned that the pony
designers don't (yet) see interposition as a key component of robust
composition.

[policy]: https://github.com/dckc/rfcs/blob/ffi-taming/text/0000-ffi-taming.md
[301]: https://github.com/ponylang/ponyc/pull/301

## Safe systems programming on seL4 and genode

The [genode May 2016 release][1605] included initial support for
rust. I haven't managed to try it out. Support for pony on genode has
only gotten as far as a [Dec 2015 twitter exchange][1512] as far as I
know.

[Robigalia](https://robigalia.org/) aims to be a persistent capability
OS built on seL4 and rust.

Rust on seL4 is pretty bleeding-edge:
[SEL4PROJ/rust-camkes-samples/issues/1][sel4-1] documents my trials
and tribulations. https://github.com/seL4/refos looks interesting.


[1605]: https://genode.org/documentation/release-notes/16.05
[1512]: https://twitter.com/ponylang/status/671971997753212928
[sel4-1]: https://github.com/SEL4PROJ/rust-camkes-samples/issues/1

## Object capability discipline support in rust

We supporters of the
[2012 proposals to isolate ambient authority in the rust stdlib][3094]
didn't make our case well enough for the 1.0 cut-off, but there is
renewed interst in
[refactoring std for ultimate portability][4301]. One result of this
could be a std alternative with no ambient authority.

[3094]: https://github.com/rust-lang/rust/issues/3094#issuecomment-9589749
[4301]: https://internals.rust-lang.org/t/refactoring-std-for-ultimate-portability/4301
