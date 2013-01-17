title: 22 Oct 2006
date: 2006-10-22
tags: []
published: true

Yesterday I plugged in a new 22" monitor that wants
1680x1050. Gnome was only offering up to 1280x1024 or
something, so I chose that. Then I logged out of X and did
`dpkg-reconfigure xserver-xorg` and set up X to do
1680x1050. When I logged in, my gnome session was set up for
1280x1024, which caused the monitor to go into a "input not
supported" mode (because 1280x1024 was no longer in the xorg
modeline perhaps?). I had to login using failsafe terminal
mode, manually start a window manager and web browser,
google to discover the name of gnome-control-center, and
then tell gnome the right resolution, logout, and log in again.

<p> <a
href="https://features.launchpad.net/distros/ubuntu/+spec/bullet-proof-x">bullet-proof-x</a>
looks like a good idea, to me. That's an ubuntu goal, but I
hope it makes it to debian soon.

<p> Boy do I miss <a
href="http://www.debian.org/News/weekly/">debian weekly
news</a>. That's where this <a
href="http://www.debian.org/News/weekly/2006/39/">Dunc-Tank
bruhaha</a> hits the pavement, for me.

<p> And I haven't updated my sid install for a few weeks because
 I'm hoping the <a
href="http://en.wikipedia.org/wiki/Iceweasel">firefox
trademark issue</a> will blow over.
