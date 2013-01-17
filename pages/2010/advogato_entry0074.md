title: 02 Jun 2010
date: 2010-06-02
tags: []
published: true

<div>In my original <a href="http://advogato.org/person/connolly/diary/51.html">April 2007 episode</a> about this 64bit machine, I went with 32bit (i386) Ubuntu because I got the impression that running quicken involved byzantine chroot/ia32-libs setup. I'm not sure whether those impressions were correct at the time, but they are no longer.&nbsp;Overall, now that I have stopped trying to do things my own special way, Ubuntu 10.4 lucid amd64 is working great.</div><br />
<a name='more'></a><br />
<br />
<br />
<div><div style="margin-bottom: 0px; margin-left: 0px; margin-right: 0px; margin-top: 0px;">As a developer, I am careful to rely only on free software so that that my contributions fit within the free software ecosystem, but as a user, I still rely on some proprietary software:</div></div><div><ul><li>Quicken: I started using it over 20 years ago, in the&nbsp;<a href="http://en.wikipedia.org/wiki/Macintosh_SE">Mac SE</a>&nbsp;era. I rely only on the user interface,&nbsp;<a href="http://dig.csail.mit.edu/breadcrumbs/node/96">exporting the data regularly</a>.</li>
<li>Skype: it's sometimes a critical link to my peers;&nbsp;<a href="http://dig.csail.mit.edu/breadcrumbs/node/63">standards-based chat</a>&nbsp;is catching up but hasn't overcome skype's 1st-mover status.</li>
<li>Flash: I don't actually rely on this, but I sure enjoy watching my shows on hulu when my wife is watching her shows on the TV.</li>
</ul></div><br />
My first approach to running quicken was to try to keep my old ~/.wine configuration in place, but after trying to debug that for a while, I discovered that the spring cleaning approach (blow it away and start over) worked just fine. This stuff all works out-of-the-box:<br />
<div><ul><li>quicken 2001 installs cleanly on a fresh wine installation</li>
<li>The <a href="http://www.skype.com/intl/en-us/get-skype/on-your-computer/linux/post-download/">skype for linux downloads</a> includes a  64 bit Ubuntu 10.4 package.</li>
<li>Adobe provides a 64bit linux version of flashplayer 10, and if you visit hulu, you can just follow your nose thru "install missing plugins" dialogs.</li>
</ul></div><div>In fact, my first approach to Ubuntu 10.4 was to try to keep everything in place and just upgrade my 32bit/i386 install rather than doing a clean install. And I took myself even further away from the normal path by trying to <a href="https://help.ubuntu.com/community/LucidUpgrades#Upgrading from a Torrent">upgrade from a torrent</a>. It seemed to make so much sense, since I could grab the whole CD image in about 15 minutes, and the installer estimated several hours to download the packages with http. But for the life of me, I couldn't get the installer to <i>use</i> the local CD image once I had it; it insisted in downloading from the net. I reported that as <a href="https://bugs.launchpad.net/ubuntu/+source/ubiquity/+bug/574686">Bug #574686</a> and gave in to the notion of downloading all the packages via http. But the result had rough edges that bothered me; flash and pulseaudio weren't getting along, among other things. So I decided to take the 64bit plunge.</div><div><br />
</div><div>Installation notes:</div><div><ul><li>I used the alternative CD, since I use LVM. It took 20 minutes to install from CD, once I was done with the partitioning stuff.</li>
<li>Did it really discover my timezone automatically? That surprised me.</li>
</ul>First impressions of 10.4 lucid:</div><div><ul><li><a href="http://www.webupd8.org/2010/03/almost-official-ubuntu-1004-lucid-will.html">Moving the window controls</a>... are they CRAZY?! The placement of those controls is deep in my muscle memory. Fortunately, going back to the clearlooks theme (System/Preferences/Appearance) fixed that quickly.</li>
<li>Why is there a Zim wiki item in the Applications/Accessories menu? There's no zim package installed, so it doesn't do anything. Was something from my previous installation detected?</li>
<li>empathy fails as an IRC client; it can't join <b>&amp;foo</b> channels.</li>
<li>Adding a printer gave me 2 options that I didn't understand (dnssd: or lpd:); my first guess (lpd:) was wrong, but when I picked the other option (dnssd:), it worked.</li>
<li>Sound works, including my iMic USB sound gizmo and my bluetooth headset.</li>
</ul>In fact, I no longer have to switch to my Macbook air to use skype audio/video.</div><div><br />
</div><div><small>For reference: RSA key fingerprint is e2:9d:a8:f7:31:e2:8a:d7:b5:b6:07:57:b5:d4:d8:fd.</small></div><div><br />
</div><div class="blogger-post-footer"><img width='1' height='1' src='https://blogger.googleusercontent.com/tracker/1117883616379032462-5071995171183816113?l=www.madmode.com' alt='' /></div>