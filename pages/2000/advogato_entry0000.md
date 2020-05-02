title: 13 Sep 2000
date: 2000-09-13
tags: ['sysadmin', 'writing']
published: true

<p>
hmm... I wonder if this would be a good place for
<a
href="http://www.w3.org/People/Connolly/drafts/web-research.html">research
notebook</a> noodling.


<p> <p>If I ask for help here, I wonder if anybody
will happen along and provide it.
Hardware problems I'm wrestling with:

<p> <ul>
<li>my 802.11 card, which worked for a while, doesn't any
more; <pre>Sep 12 19:01:52 shoal kernel: eth1: WaveLAN/IEEE,
io_addr 0x100, irq 5, mac_address 00:E0:63:50:4D:36
Sep 12 19:03:51 shoal kernel: eth1: Transmit timeout.
</pre>

<li>printing is flakey. the debian lprng package failed,
silently, to install. I think it was related to
the fact that I disabled the lp0 module to free
up an IRQ for the 802.11 card, but I'm not sure.
It really bothers me that there was no error
message (that I can find, anyway).
<li>burning CD ROMs doesn't work. I paid
the extra money for a nice SCSI CD ROM burner --
a plextor -- and it works about 1 in 5 times.
It's never worked at the advertised write
rate, 2x. The low reliability discourages
me from even trying
<li>sound is goofy. I got the driver to work
(@@details) but now sounds, played thru
esd, "stretch out" as if played thru a
loopback/delay for about 5x their normal
duration
</ul>


<p> <p>Hmm... this textarea interface is a little too
constraining for comfort. Can I come back later
and add details to these problem reports?
I wonder what that wiki
tag is... maybe that would be more comfortable.

