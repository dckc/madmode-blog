title: 17 Oct 2005
date: 2005-10-17
tags: []
published: true

I upgraded <a href="http://dm93.org/z2001/AmdAntec">AmdAntec</a> over the weekend to Ubuntu breezy. Due to traffic, a straight <tt>apt-get dist-upgrade</tt> said it was going to take 14 hours, so I used bittorrent to grab the .iso, mounted it with losetup, and ran a little python BasicHttpServer.

<p> Ho-hum. The screen was stuck at 640x480 until I did <tt>dpkg-reconfigure xserver-xorg</tt> a few times. And I can't get sound to work (2.6.3 seems to be the last kernel that works with my sound card, and breezy defaults to 2.6.10).
