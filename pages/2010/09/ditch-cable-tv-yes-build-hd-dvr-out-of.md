date: 2010-09-17
published: true
tags: [video, pvr, digital media, tv, hardware, diy]
title: Ditch cable TV? Yes. Build an HD DVR out of old PC parts? Maybe not.
updated: 2011-05-09


This item was supposed to be entitled&nbsp;<i>Ditching cable for netflix/wii, broadcast HDTV, and a DIY PVR</i>. After watching the digital media marketplace and technology for&nbsp;years, I convinced my family it was time to go for it this summer. We're close, but due to one&nbsp;critical breakdown in my research, we're not quite there.<br />
<br />
<a name='more'></a><br />
<br />
<ol>
<li>Cancel TV part of double play TV+Internet subscription, reducing it by ~$60/month.<br />
<br />
We never did go for their triple play with phone service; I signed up for VoIP with <a href="http://www.viatalk.com/">ViaTalk</a> when we moved houses a couple years ago, and we've been pretty happy with it. While only the cable company can do on-screen caller-id, I'd rather have stuff like email and SMS notification for messages, for less money. Try it, and tell 'em Dan sent you (referral code 47340A17).<i><br />
Check.<br />
</i></li>
<li>Set up TV for broadcast HD TV.<br />
<br />
The salesperson at Best Buy recommended a $60 active antenna, but we went for the $30&nbsp;<a href="http://www.amazon.com/RCA-ANT1400-Multi-Directional-Digital-Passive/dp/B001GGAIIQ?ie=UTF8&amp;tag=danconnolly&amp;link_code=btl&amp;camp=213689&amp;creative=392969" target="_blank">RCA ANT1400 Multi-Directional Digital Flat Passive Home Theater Antenna (White)</a><img alt="" border="0" height="1" src="https://www.assoc-amazon.com/e/ir?t=danconnolly&amp;l=btl&amp;camp=213689&amp;creative=392969&amp;o=1&amp;a=B001GGAIIQ" style="border: none !important; margin: 0px !important; padding: 0px !important;" width="1" />&nbsp;and it works just fine, even in the basement.<br />
<i><span class="Apple-style-span" style="font-style: normal;"><i>Check</i></span><span class="Apple-style-span" style="font-style: normal;">.<br />
</span></i></li>
<li>Subscribe to Netflix.<br />
<br />
&nbsp;I wondered about the quality of streaming movies, and the first one we tried was pretty bad. We were planning to buy a <a href="http://www.amazon.com/Roku-N1100-HD-Player/dp/B001PIBE8I?ie=UTF8&amp;tag=danconnolly&amp;link_code=btl&amp;camp=213689&amp;creative=392969" target="_blank">Roku box</a>, but first we tried it on my laptop, a MacBook Air, hooked up to the TV. Big mistake. Turns out these things have a <a href="http://en.wikipedia.org/wiki/MacBook_Air#Issues">well-known cooling problem</a>, and "The problem is aggravated by system-intensive tasks such as video playback". Then we remembered Netflix started supporting streaming to&nbsp;<a href="http://www.amazon.com/Wii-Nintendo/dp/B0009VXBAQ?ie=UTF8&amp;tag=danconnolly&amp;link_code=btl&amp;camp=213689&amp;creative=392969" target="_blank">Wii consoles</a><img alt="" border="0" height="1" src="https://www.assoc-amazon.com/e/ir?t=danconnolly&amp;l=btl&amp;camp=213689&amp;creative=392969&amp;o=1&amp;a=B0009VXBAQ" style="border: none !important; margin: 0px !important; padding: 0px !important;" width="1" />, and we have one of those. It&nbsp;seemed too good to be true, but it's not. It's just like watching a DVD, as far as I can tell. We may or may not ever get a Roku.<br />
<i><span class="Apple-style-span" style="font-style: normal;"><i>Check.<br />
</i></span></i></li>
<li>Cobble together a PVR out of old PC parts.<br />
<br />
My wife misses some cable-network-only shows, but for the price of a new HD capture card (around $80) it looks like we should be able to timeshift broadcast favorites such as&nbsp;<i>Survivor</i> and <i>Big Bang Theory</i>.<br />
That was the theory, anyway.</li>
</ol>
I thought the hard part was video capture, encoding, and recording. Sucking in HD video through a USB gizmo seemed too good to be true; plus, the norm with USB gizmos is that half the smarts is in a proprietary, Windows-only driver.<br />
<br />
<iframe align="left" frameborder="0" marginheight="0" marginwidth="0" scrolling="no" src="http://rcm.amazon.com/e/cm?t=danconnolly&amp;o=1&amp;p=8&amp;l=bpl&amp;asins=B001DEYVXO&amp;fc1=000000&amp;IS2=1&amp;lt1=_blank&amp;m=amazon&amp;lc1=0000FF&amp;bc1=000000&amp;bg1=FFFFFF&amp;f=ifr" style="align: left; height: 245px; padding-right: 10px; padding-top: 5px; width: 131px;"></iframe><br />
But most of the HD capture cards plug into a PCI express slot, and I think my machines are too old to have one of those.&nbsp;<a href="http://www.hauppauge.com/site/support/linux.html">Hauppage linux support </a>and the <a href="http://www.linuxtv.org/wiki/index.php/Hauppauge_WinTV-HVR-950Q">linuxtv wiki</a> agreed that the <a href="http://www.amazon.com/Hauppauge-WinTV-HVR-950Q-Personal-Recorder-Control/dp/B001DEYVXO?ie=UTF8&amp;tag=danconnolly&amp;link_code=btl&amp;camp=213689&amp;creative=392969" target="_blank">Hauppauge WinTV-HVR-950Q</a><img alt="" border="0" height="1" src="https://www.assoc-amazon.com/e/ir?t=danconnolly&amp;l=btl&amp;camp=213689&amp;creative=392969&amp;o=1&amp;a=B001DEYVXO" style="border: none !important; margin: 0px !important; padding: 0px !important;" width="1" />&nbsp;was supported, and the Micro Center web site showed there were 2 in stock just down the road.<br />
<br />
After just a bit of puzzling over the docs for&nbsp;<a href="http://www.linuxtv.org/wiki/index.php/Testing_your_DVB_device">Testing your DVB device</a>, I figured out that I needed to tell the scanning tool to use the north america list of frequencies in order to build a <span class="Apple-style-span" style="font-family: 'Courier New', Courier, monospace;">channels.conf</span> file. &nbsp;After that, I just followed my nose through getting it to work with mplayer, freevo, and eventually, mythtv.<br />
<br />
All this was on my desktop machine. Now it was time to use this knowledge to get it running on an old klunker PC that I could put next to the TV downstairs. I shuffled some parts around between two old machines, plugged in the resulting frankenputer, and flipped the switch. Nothing. Maybe a short somewhere... disconnect the power supply from this and that and finally everything. Nope. She's dead, Jim.<br />
<br />
While thinking about re-shuffling the parts, I realized I had an old mac mini in the closet, not doing much other than sharing music.&nbsp;<a href="http://www.mythtv.org/wiki/MythTV_on_Mac_OS_X">MythTV on OS X</a>&nbsp;said:<br />
<br />
<blockquote>
<h3>
Frontend</h3>
To watch TV at acceptable speeds, you'll want at least an 800 MHz G4 or better.</blockquote>
<br />
Check... mine is a 1.42 GHz PowerPC G4.<br />
<br />
<blockquote style="background-color: #93c47d;">
<em>And now a word from my technical reviewer:</em><br />
<br />
If you've read this far, my 11 year old son, who reviewed this article for me, says you deserve a mini game:<br />
<br />
<b><a href="http://www.addictinggames.com/avalanche.html"><img src="http://www.addictinggames.com/fimages/4131.jpg" /> Avalanche</a><br />
Jump Little Guy! Jump and Be Free!</b><br />
<br />
Now back to our saga...</blockquote>
<br />
I plugged it into a monitor and after a couple mis-fires, found a working copy of MythFrontend. Aha! Nifty! The front end mac mini is talking to the back-end on my beefy linux desktop.<br />
<br />
Then I hit "watch TV." And... well...<br />
<br />
The software clearly worked as designed, decoding and displaying video just as fast as it could. But the hardware was too slow by an order of magnitude, maybe two. I got about one frame per second.<br />
<br />
With all the research I did on hardware for video capture, I missed the essential clue about playback:<br />
<br />
<blockquote>
To <b>playback HDTV content</b>, plan on a powerful CPU. "How powerful?" depends on a number of factors ...</blockquote>
<blockquote>
The Simple Answer: Once you are in the 3.2 Ghz P4-class of CPU you should have no issues with viewing HDTV.</blockquote>
<blockquote>
&nbsp;-- <a href="http://mythbuntu.org/wiki/hardware"><span class="Apple-style-span" style="color: black;">mythbuntu hardware wiki page</span></a>&nbsp;</blockquote>
<iframe align="left" frameborder="0" marginheight="0" marginwidth="0" scrolling="no" src="http://rcm.amazon.com/e/cm?t=danconnolly&amp;o=1&amp;p=8&amp;l=bpl&amp;asins=B003L0QF2S&amp;fc1=000000&amp;IS2=1&amp;lt1=_blank&amp;m=amazon&amp;lc1=0000FF&amp;bc1=000000&amp;bg1=FFFFFF&amp;f=ifr" style="align: left; height: 245px; padding-right: 10px; padding-top: 5px; width: 131px;"></iframe><br />
I suppose MythTV on old hardware made sense a few years ago for standard-def or even DVD content,&nbsp;but upgrading one of these old boxes for HD playback doesn't seem to make much sense when a new, quieter, low-power machine with native HDMI out like the&nbsp;<a href="http://www.amazon.com/Acer-AspireRevo-AR3610-U2002-Desktop-Dark/dp/B003L0QF2S?ie=UTF8&amp;tag=danconnolly&amp;link_code=btl&amp;camp=213689&amp;creative=392969" target="_blank">Acer AspireRevo</a><img alt="" border="0" height="1" src="https://www.assoc-amazon.com/e/ir?t=danconnolly&amp;l=btl&amp;camp=213689&amp;creative=392969&amp;o=1&amp;a=B003L0QF2S" style="border: none !important; margin: 0px !important; padding: 0px !important;" width="1" />&nbsp;goes for around $350.<br />
<br />
That's just six months of saving $60/month that we were paying the cable company for TV.