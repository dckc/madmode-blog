date: 2012-07-08
published: true
tags: [mobile, digital media, music, android]
title: Nokia Lumia 710 with Windows Phone 7 is an eye-opener
updated: 2012-07-11


At first, the conversation was about a new iPod touch vs. a mobile phone. The battery in my youngest son's aging iPod touch lasts about half an hour now, and his birthday is coming up. He was leaning toward a new iPod touch, but the reason we get mobile phones for our boys is so that mom's taxi service can reach them, and the lack of a phone for him has caused some issues in that area recently.<br />
<br />
So we took him to the T-Mobile store to shop for a phone. We're OK to pay a few more dollars a month to add him to our family plan (especially since we can drop the land line) but we're not getting him a data plan.<br />
<br />
We had just about decided on some Samsung talk-and-text model when the clerk said "I can show you a touchscreen phone that doesn't require a data plan." It was the Nokia Lumia 710 with Windows Phone 7.&nbsp;<b>The price? Just $50*</b>&nbsp;(with the usual 2 year contract).<br />
<br />
I have spent a couple decades avoiding the influence of Microsoft in my life, and especially in the Web, but Microsoft is motivated to be more open and interoperable in the mobile space, since they don't dominate it. &nbsp;Plus, a good friend of mine gushes about his new Windows Mobile phone, a complete turn-around compared to his endless gripes and frustrations with his original Windows Mobile phone. So I was open to it. But even $50 is&nbsp;$40 more than the other phone, so I asked my son if he was sufficiently interested to contribute a certain chunk of the price. Yes, he said, without hesitation, and we went for it.<br />
<br />
This thing has all the "wow! it can do <i>that</i> too?!" of my Samsung Vibrant with Android 2.2 and none of the "oops... hey! what? grrr..." surprise and frustration and waiting. The back button is as quick as it used to be on the sidekick/hiptop. I don't know why Android can't cache web pages worth a lick; didn't&nbsp;Andy Rubin design both platforms?<br />
<br />
The one bit of frustration is by design: until his birthday actually arrives, windowsmobile.com won't let him install any apps.<br />
<br />
So migrating his contacts was a bit of an adventure. We ended up <a href="http://follow.ourbunny.com/post/2148582357/download-iphone-contacts-to-linux">using python-idevicesync</a> on my linux box to get them in a vCard file for uploading into his google account (I set up <a href="http://lifehacker.com/5708219/why-you-should-use-google-apps-with-your-personal-domain-for-your-google-life">google apps for domains for our family</a> a few years back). Then the phone knew how to get the contacts from there.<br />
<br />
I didn't discover the shortest path to loading music right away. It has a micro-USB connector, but doesn't act like a flash drive. Evidently it speaks <a href="http://en.wikipedia.org/wiki/Media_Transfer_Protocol">music transfer protocol (MTP)</a>. The up-side is that it doesn't need to re-scan the entire flash filesystem every time you connect it to a computer (or turn it on). MTP is supported by rhythmbox and lots of other open source music managers, but evidently not quite the dialect of MTP that Windows Phone 7 uses. When I tried to drag a bunch of tracks over, Rhythmbox would copy one track and then stop. And it wouldn't set the artist/album/track metadata right. Evidently it was silently discarding an error (grrr!). <a href="http://gmtp.sourceforge.net/">gMTP</a> did better: it would report an error after each track, but when I acknowledged the error dialog, it would continue to the next track. It still didn't get the metadata right.<br />
<br />
This exercise prompted me to resume the <a href="http://www.madmode.com/2011/04/closing-music-sharing-loops-with-amazon.html">quest of cleaning up my music archive</a>, including convincing Ubuntu to share files with Mac OS X again (netatalk seems to be dying; ugh... samba config! caramba!).<br />
<br />
<b><a href="http://www.hardcoded.net/dupeguru_me/">dupeguru Music Edition</a>, where have you been all my life?!</b><br />
<br />
It cleaned up thousands of duplicate tracks in my filesystem and even cleaned up dead tracks in my iTunes database. <i>(Of course, I expected iTunes Home Sharing's ability to detect tracks that I already have to extend to the case of dragging and dropping the contents of a playlist, and I was wrong, so I have another batch of dups to clean up...)</i><br />
<br />
I expected&nbsp;&nbsp;to run into the same age restriction with&nbsp;Windows Phone 7 Connector for Mac as my son ran into with Zune on his netbook, but not so. I was able to use it to install a Windows Phone update, though it gave me a scare when it quit during the "do not disconnect" part of the update; I was mentally preparing to take the bricked phone back to the T-Mobile store when the phone rebooted and announced that the update was complete. Whew!<br />
<br />
Syncing music worked with Windows Phone 7 Connector. It got the metadata right, but I think it excluded some songs due to DRM that were actually not DRM-encumbered.<br />
<br />
I have had my eye on the Galaxy Nexus with Jellybean. $350 unlocked seemed like such a good deal, but now I wonder... do I really want to choose a phone based on my ability to tinker with it? With my Samsung Vibrant running Android 2.2, I'm constantly dreaming of ways to improve it. But that's because I'm constantly interrupted from what I was actually trying to do with the phone by some bug or performance issue.<br />
<br />
Wasn't it Ed Dumbill who said "I don't want to sysadmin my phone." Maybe I'd be happier with the no-user-serviceable-parts-inside product that Nokia, Microsoft, and T-Mobile are offering for hundreds less.<br />
<br />
<i>*EDIT: It looks like the $50 price we got at a local T-Mobile store is not widely available.&nbsp;<a href="http://wireless.amazon.com/Nokia-Lumia-710-Windows-T-Mobile/dp/B006U0X7UY/">Amazon wants $300</a>&nbsp;and gives a list price of $500.</i>