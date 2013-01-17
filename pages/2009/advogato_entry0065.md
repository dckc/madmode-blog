title: 18 Apr 2009
date: 2009-04-18
tags: []
published: true

I'm trying out a new netbook

<p> <p> <p> The keyboard is quite small; at first, touch-typing
didn't 
work 
at all, but I seem to be getting the hang of it. It's a 
good thing clicking on the trackpad works; the button is 
hopeless.

<p> <p> <p> I hope/plan to have it run Ubuntu as well as the
WinXP that 
came on it, but I'm really struggling to get Ubuntu on it:

<p> <p> <p>   * The ubuntu "jaunty jackalope" image (@@link) is
1GB, 
which takes quite a while to download and even longer to 
write to the SD card (I seem to get 1.1 Mb/sec sustained).
  * This machine won't boot from its media card slot 
(@@cite source)

<p> <p> <p> I managed to boot debian-from-scratch with an
external CD, 
but it couldn't recognize the ethernet card. What's the 
equivalent of lsusb under WinXP?

<p> <p> <p> I'm using Opera rather than firefox just now; I
figure if 
I'm gonna use a closed-source operating system (Win XP) I 
might as well try Opera while I'm at it. Boy, is Internet 
Explorer bloated with ads and such.

<p> <p> <p> The google toolbar seems to bind a bunch of keys that I 
accidentally hit on occasion. Annoying.

<p> <p> <p> This machine is an Acer; I could swear I asked the
guy at 
Micro Center for an MSI Wind.

<p> <p> <p> The USB disk enclosure is wrong again too: it's IDE
when I 
need SATA. And the $20 wifi router won't play nice with my 
Brother HL-5250DN printer.

<p> <p> Let's try copying the image to a Lexar SDHC 4BG card and see
if it's any faster...

<p> <pre>
connolly@pav:~/Desktop$ dmesg | grep Attach


<p> [82241.020775] sd 9:0:0:0: [<b>sdk</b>] Attached SCSI disk

<p> connolly@pav:~/Desktop$ sudo dd
if=jaunty-netbook-remix-i386.iso of=/dev/<b>sdk</b> bs=1M
</pre>

<p> wow! MUCH faster!

<p> <pre>
692+1 records in
692+1 records out
725796864 bytes (726 MB) copied, 14.9489 s, <b>48.6 MB/s</b>
</pre>


