title: XO-1 as music front-end?
date: 2009-01-11
tags: []
published: true

<strong>XO-1 as music front-end?</strong>

<p> <p> <p> <blockquote>
Latest mt-daapd transcodes. Sweet. No more ripping flac to
mp3 just
for stupid iTunes
  -- <a href="http://identi.ca/notice/1550602">ndw 21 Dec
2008</a>
</blockquote>

<p> <p> <p> Perfect; now that I have a new big disk, I can take our
iTunes libraries, which have gotten sorta mixed up, and
merge them into one big honkin networked library.
<a href="http://wiki.mt-daapd.org/wiki/Quickstart_Ubuntu">mt-daapd
Ubuntu quickstart</a> worked fine.

<p> <p> <p> But... how to access the songs from the living room?
The roku soundbridge and stuff look nice, but I can't
justify the cost. Likewise airport express.

<p> <p> <p> It just hit me: my xo-1 has wifi and a headphone
jack.

<p> <p> <p><strong>update: it works!</strong> I used <a href="http://wiki.archlinux.org/index.php/Streaming_With_Icecast_and_MPD">mpd
with output to icecast2</a>. The documentation could use some
diagrams, but once I got the picture, it was
reasonably straightforward:
<ul>
<li>mpd indexes the music, takes commands over a network
protocol from various clients such as pympd (linux) and
theramin (mac), queues songs, and decodes and streams them

<p> <li>icecast takes streams and buffers and
multiplexes them to multiple clients
<li><a href="http://olpcnews.com/forum/index.php?topic=863.0">mplayer
on the XO-1</a>
listens to the stream and plays it thru the headphone
jack
<li>powered speakers in the living room play the results
</ul>

<p> <p> <p> For bonus points: I'd like to control it from my
sidekick
(or g1). That should be just a matter of setting up a
web-based mpd client and exposing it thru the firewall.


<p> <hr>
My related work:

<p> <ul>
<li>
 <cite><a href="http://dig.csail.mit.edu/breadcrumbs/node/228
">hAudio for microformats mixtapes, in progress</a></cite>
 by connolly on Thu, 2008-03-06


<p> <li>
<a href="http://homer.w3.org/~connolly/projects/cdcat/">cdcat
hg project</a>
2:20cfcde22c4e 2008-03-21 show barcodes not found in html output
</ul>

<p> Related work by others:

<p> <ul>
<li><cite><a href="http://siliconflorist.com/2009/01/08/using-your-android-phone-as-a-remote-for-controlling-music-playback/">Using
your Android phone as a remote for controlling music
playback</a></cite>

<p> Rick Turoczy | January 8, 2009 

</ul></hr>