title: Building a PC... end of an era?
date: 2005-02-07
tags: []
published: true

<b>Building a PC... end of an era?</b>

<p> <blockquote>
The kids' PC was noisy and slow. The Mac mini buzz was very tempting,
but after going over Micro Center specials and a linux hardware buying
guide with Brennan, we chose to build/upgrade our own, for under $150.
<br />-- <a href="http://dm93.org/2005/0501pchw/">Building a PC</a>
</blockquote>

<p> <p>I wanted to pass on this experience to my son
before Hollywood makes it illegal (due to DCMA++,
<a href="http://www.microsoft.com/mscorp/twc/twc_whitepaper.mspx">Trustworthy Computing</a>, ...) or something else destroys
the commodity PC
hardware market.

<p> <p>When I eventually got the thing working, the boot time is long enough and it's quiet enough that I'm thinking of leaving it on all the time. And it's orders of magnitude faster than the machine it replaces, making me wonder what to do with all this compute power, beside cartoon network games and tuxracer...

<p> <b>Family Finances and Entertainment, Ubuntu, and Debian</b>

<p> <p>I think the machine should make a nice PVR (or at
least to <a href="http://dm93.org/z2001/LegacyVideo">convert VHS tapes to digital video</a>); too bad
there are no Ubunutu packages for freevo nor mythtv.
There are <a href="http://freevo.sourceforge.net/cgi-bin/doc/FreevoAptDebian">external debian repositories with freevo packages</a>,
so I went to install debian on the 2nd disk, using a netinst
CD I burned just a few months ago. It tried to get a DHCP
lease using the ehternet controller on the motherboard, but
the connection to this machine is wireless, thru a
<a href="http://www.microcenter.com/single_product_results.phtml?product_id=150261">Microcenter: D-Link DWL-G520</a> that I got for
$27.99 after rebate. It's listed among the
<a href="http://www.mattfoster.clara.co.uk/madwifi-hw.htm">madwifi supported hardware</a>; of course, the madwifi HAL isn't
open source;
Ubuntu supports it via a <tt>restricted-modules</tt> package, but the debian installer does not. I considered
building a kernel module from source, but I have
a bad taste in my mouth maintaining a
<a href="http://dm93.org/z2001/WinFourLinOnDebian">WinFourLinOnDebian</a>
kernel. You see, I still rely on Quicken for family
finances; the open source alternatives are missing
features that I rely on (budgeting, quick-zoom reports, ...).


<p> I once dispaired that open source would ever produce a competitive web browser, and that day has clearly arrived, so I remain hopeful that open source will conquer the wifi and PVR applications, though the challenges are formidable.