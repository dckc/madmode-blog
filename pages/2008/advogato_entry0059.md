title: 30 Dec 2008
date: 2008-12-30
tags: ['media', 'video']
published: true

<p>woot! It works! Youtube videos on a <a href="http://www.visual-land.com/vl567i_black.html">$30
media player</a>!

<p> <p>The <a href="http://en.wikipedia.org/wiki/AMV_video_format">AMV
format</a> was new to me;
I found a 
 <a href="http://code.google.com/p/amv-codec-tools/wiki/HowToConvertToAMV">HowToConvertToAMV</a>
recipe,
but that lacks support for mp4a, the audio codec
used by youtube (at least the videos I tested).

<p> <p>Then I found <a href="http://www.robpoyntz.com/blog/?p=180">adding
--enable-faad to ffmpeg</a>
(don't forget to <tt>make distclean</tt>) and presto:

<p> <pre>
$ clive
'http://www.youtube.com/watch?v=3pYN42YyWp0&amp;feature=related'
clive 0.4.19 20080722  [Linux]
http://www.youtube.com/watch?v=3pYN42YyWp0&amp;feature=related&amp;fmt=
           100%
BrianReganWalkieTalkie.mp4                                 
              2.6MB
=&gt; 1 (2.6MB), failed: 0, skipped: 0.
BrianReganWalkieTalkie.mp4                    100%    2.6MB
 109.2KB/s 00:00:24

<p> $ ~/src/amv-codec-tools/AMVmuxer/ffmpeg/ffmpeg -i
BrianReganWalkieTalkie.mp4 -f amv -s 128x90 -r 16 -ac 1 -ar
22050 -qmin 3 -qmax 3 BrianReganWalkieTalkie.amv
FFmpeg version SVN-r589, Copyright (c) 2000-2007 Fabrice
Bellard, et al.
  configuration: --enable-gpl --enable-libfaad
  libavutil version: 49.5.0
  libavcodec version: 51.47.1
  libavformat version: 51.17.0
  built on Dec 30 2008 12:07:41, gcc: 4.3.2
Input #0, mov,mp4,m4a,3gp,3g2,mj2, from
'BrianReganWalkieTalkie.mp4':
  Duration: 00:01:13.7, start: 0.000000, bitrate: 291 kb/s
    Stream #0.0(und): Audio: mpeg4aac, 44100 Hz, stereo
    Stream #0.1(und): Video: h264, yuv420p, 320x240 [PAR 0:1
DAR 0:1], 30.00 fps(r)
PIX_FMT_YUV420P will be used as an intermediate format for
rescaling
Output #0, amv, to 'BrianReganWalkieTalkie.amv':
    Stream #0.0(und): Video: amv, yuvj420p, 128x90 [PAR 0:1
DAR 0:1], q=3-3, 200 kb/s, 16.00 fps(c)
    Stream #0.1(und): Audio: adpcm_ima_amv, 22050 Hz, mono,
64 kb/s
Stream mapping:
  Stream #0.1 -&gt; #0.0
  Stream #0.0 -&gt; #0.1
Press [q] to stop encoding
frame= 1172 fps=343 q=0.0 Lsize=    3878kB time=73.2
bitrate= 433.7kbits/s    
video:3062kB audio:802kB global headers:0kB muxing overhead
0.376436%
</pre>

<p> <p>Merry Christmas, Kyle!

<p> <p>It's not as nicely packaged as the Mac app Justin
uses with his ipod, but it's cheaper and
more <a href="http://www.freedom-to-tinker.com/">free</a>
(I'm not sure if it's quite open source; I don't
know the license details of the AMV code.)

<p> <p>See also: <a href="http://chatlogs.planetrdf.com/swig/2008-12-30#T18-14-45">#swig
chat, including notes on a mythv box.

<p> <p>tags:
<a href="http://delicious.com/connolly/media">media</a>,
<a href="http://delicious.com/connolly/video">video</a>
</a>