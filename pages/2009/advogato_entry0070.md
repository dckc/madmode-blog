title: All knotted up about media management
date: 2009-11-23
tags: [photo, mac, digital media, geo, music, mixtape]
published: true

<b>All knotted up about media management</b>

<p> Another installment in the <a href="http://dm93.org/z2001/ToMacOrNotToMac">to-mac-or-not-to-mac</a>
series... I recently replaced my 2004 era G4 powerbook with
a MacBook Air. Hulu works a lot better with a modern CPU ;-)
I'm hooked on <a href="http://www.hulu.com/flash-forward">Flash Forward
now</a>. And <a href="http://www.getmiro.com/">Miro</a>
"just worked" to grab some Ted talks for watching on the plane.

<p> The MacBook Air comes with new Apple software too: iLife '09
has face recognition
and map integration.

<p> It looks like google's cross-platform tool does face
recognition and map integration too:
<a href="http://googlephotos.blogspot.com/2009/09/announcing-picasa-35-now-with-name-tags.html">Google
Photos Blog: Announcing Picasa 3.5, now with name tags,
better geotagging and more</a>. After watching
the <a href="http://www.chromium.org/chromium-os">chromium
"everything lives in the cloud" OS videos</a>,
it's hardly surprising to see 
Google talking about photo libraries in their offer of <a href="http://feedproxy.google.com/~r/blogspot/MKuf/~3/MtV96hoUvQY/twice-storage-for-quarter-of-price.html">twice
the storage for a quarter of the price</a>, i.e. 20 GB for
only $5 a year.

<p> Google says most people have less than 10GB of photos; we
have the same order of magnitude (~32GB, including videos).
How long would it take to upload all that content? It took
hours just to copy it across our LAN (details below).
I got <a href="http://blog.lathi.net/articles/2006/08/28/iphoto-library-sharing-across-a-network">LAN
access to the iPhoto Library</a> working, but it was
annoyingly slow.

<p> Then there's music...

<p> A Google <a href="http://feedproxy.google.com/~r/blogspot/MKuf/~3/oQ11Ur5dH1g/even-more-music-for-you-to-find-with.html">music
search</a> item reminds me about Lala (hi Anselm!) and
Pandora. Unlike photos, the music I listen to is mostly
stuff I didn't record, so it makes a lot of sense that it
lives in the cloud... if only caching were a *lot* better. I
want the iPod wear-it-on-your-arm-while-you-run experience.

<p> I read about <a href="http://mobile.slashdot.org/story/09/11/21/2351245/Ten-Things-Mobile-Phones-Will-Make-Obsolete">mobile
phones taking over as everything from watches to media
players</a> but watch batteries last years, an ipod shuffle
goes several trips on one charge, and my cellphone needs
charging every day.

<p> Also, I want the few kilobytes of precious data (playlists,
star ratings, and the like) managed as *my* data, separate
from the gigabytes of recorded mp3 data. Last.fm goes one
way... with scrobbling from iTunes to the cloud. How much
would I be willing to pay for a subscription to all my "mix
tape" style playlists? Hmm.

<p> And how long before <a href="http://www.kickstarter.com/projects/textfiles/the-jason-scott-sabbatical">patronage</a>
returns as the dominant business model for creative work?
Will the music of my kids' formative years be as free as Ted
videos?


<p> <hr>
<b>Details: Photo library stats</b>

<p> This past weekend, I copied the family photo library from my
wife's laptop (she's the shutterbug) to the linux box in the
closet and then to my new macbook air. It's 32GB including
videos. I didn't record the time exactly but it seemed to
take around 5hours.

<p> Using iPhoto Library Manager, I split it into two albums:
the most recent 9 months and everything older. Copying the 9
month segment using rsync over wifi concluded thus:

<p> <pre>
sent 9195085734 bytes  received 190748 bytes  1379946.95
bytes/sec
total size is 9193422268  speedup is 1.00
</pre>

<p> That's 8.5GB in just under 2 hours, which suggests 5hrs is
in the ballpark.

<p> music stats...

<p> <pre>
sent 3877121671 bytes  received 36170 bytes  2818726.17
bytes/sec
total size is 3876532701  speedup is 1.00
</pre>





<p> star ratings in iTunes
</hr>