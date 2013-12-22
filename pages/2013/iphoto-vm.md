title: Toward a virtual iPhoto archive
date: 2013-12-22
published: true
tags: [photo, vm, mac]
summary: "I'm looking into using a Mac OS VM (aka
	hackintosh) to access my old iPhoto
	libraries, at least long enough to migrate them to another platform."

The macbook that hold our oldest (digital) family photos is aging
rapidly (keyboard and mouse went out years ago; battery hardly
works). I set it up as a home theater PC and media workstation back in
August 2012, but despite having a big 32" (TV) screen, we don't use it
much. Every time I sit down to it, it wants to spend 20 minutes
updating all the software. So I'm looking into using a Mac OS VM (aka
[hackintosh](http://www.hackintosh.com/)) to access the iPhoto
libraries, at least long enough to migrate them to another platform.

The path is reasonably well-trodden:

 * [How to install a Snow Leopard Hackintosh in Virtualbox](http://www.macbreaker.com/2012/02/snow-leopard-virtualbox.html)
   Feb 8, 2012, MacBreaker

But there's a catch:

> This guide does not cover AMD processors

I found a work-around:
[Empire EFI with AMD support](http://prasys.info/2010/01/empire-efi-v-1-085-is-out/). My
[mac vm bookmarks on diigo](https://www.diigo.com/user/dckc-madmode/vm+mac)
from Nov 2013 detail a few other known issues.

I can boot to Mac OS X by way of a (virtual) install DVD, but I can't
get the normal bootloader path to work. (*Oops... I neglected to
record the symptoms.*)

I haven't really peeled back all the layers to understand how things
work; perhaps I should forgo using pre-packaged stuff and Use The
Source, Luke.

Wish me luck.
