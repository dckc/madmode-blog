title: Reviving Home Movies with kino and ffmpeg
date: 2009-01-08
tags: []
published: true

<strong>Reviving Home Movies with kino and ffmpeg</strong>

<p> <p> <p> I've tried digitizing movies before, but the codec
puzzles
were overwhelming. This year, Kino pretty much Just Works.
After one permissions issue with /dev/raw1394 , it ate hours
of video and produced nice collections of DV files with SMIL
wrappers (hmm... I wish SMIL were an XHTML microformat...
more on that another time). And it exports not only ogg but
also consumer technology: youtube-style .flv and
<a href="http://en.wikipedia.org/wiki/Xvid">XVid</a> that
works with the $20 DVD player I got via craigslist.
(Thanks for the clues, <a href="http://www.longtailvideo.com/">longtail video</a>.)

<p> <p> <p> <p> One reason I swapped this task back in was that
we ran
across home movies on decaying analog media when cleaning up
the basement. Another reason is all the storage space I have
since I couldn't pass up a Micro Center hot deal: $70 for
640GB of disk. That's 11 cents/GB.



<p> <p> <p> update: kivo is flaking out, as is dvgrab.

<p> <p> <p> It's sorta silly to use DV format to capture video
off VHS.
It's also silly to capture all the uninteresting bits at
high bit-rate. Better to make a cheapo FLV of the whole
thing and then go back over the interesting parts.

<p> <p> <p> ffmpeg to vcd works; to do svcd, need unstripped libs
per <a href="https://bugs.launchpad.net/medibuntu/+bug/269997">medbuntu
bug info</a>

<p> <p> <p> <pre>
$ ffmpeg -t 2:00:00 -f dv -i /dev/dv1394/0 -target ntsc-svcd
russia-vhs-capture.mpg
</pre>

<p> p.s. note <a href="http://www.tbray.org/ongoing/When/200x/2008/05/05/Video-Pain">Video
Pain</a> by Tim Bray, May 2008.