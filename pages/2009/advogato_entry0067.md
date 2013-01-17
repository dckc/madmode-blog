title: more on music collection and office organization
date: 2009-05-01
tags: []
published: true

<b>more on music collection and office organization</b>

<p> I'm still not sure how to manage my music files. Now that I
have most of it on one big disk on a linux always-on machine
(I hesitate to say server as I don't have a clear back-up
strategy), I put our mac mini under the TV in the hearth,
replacing the XO-1 laptop, in order to do video as well as
just sound.

<p> It doesn't make much sense, after all, to try to stay
open-source-pure when it comes to listening to RIAA music
and watching hollywood movies; I might as well have Steve
Jobs negotiating my <a href="http://www.tbray.org/ongoing/When/200x/2003/07/12/WebsThePlace">sharecropping</a>
deal.

<p> <a href="/proj/mpd/">mpd</a> uses .m3u files. They're pretty
simple, but for archival purposes, I try to stick to XHTML.
I wrote another little python ditty to do the conversion:
see m3uin.py in r423:4a5a8b2d237c of
<a href="http://bitbucket.org/DanC/palmagent/">palmagent hg
repo</a>.

<p> I run it like this:

<p> <pre>
$ python ~/projects/palmagent/m3uin.py
/var/lib/mpd/playlists/Three\ Chords\ and\ the\ Truth.m3u
&gt;three_chords.html
</pre>

<p> and out comes:

<p> <blockquote><ol>
<li>
from <cite>A Song's Best Friend_ The Very Best Of John Denver [Disc
1]</cite>
<br> by <span><b>John Denver</b></span>
<br><a href="artists-popular/John%20Denver/A%20Song%27s%20Best%20Friend_%20The%20Very%20Best%20Of%20John%20Denver%20%5BDisc%201%5D/1-04%20Poems%2C%20Prayers%20And%20Promises.mp3"><em>Poems, Prayers And Promises</em></a>

<p> <li>
from <cite>WOW Worship (orange)</cite>
<br> by <span><b>Compilations</b></span>
<br><a href="artists-popular/Compilations/WOW%20Worship%20%28orange%29/1-01%20Did%20you%20Feel%20the%20Mountains%20Tremble.mp3"><em>Did you Feel the Mountains
Tremble</em></a>

<p> <li>
from <cite>Family Music Party</cite>
<br> by <span><b>Trout Fishing In America</b></span>
<br><a href="artists-popular/Trout%20Fishing%20In%20America/Family%20Music%20Party/14%20-%20Back%20When%20I%20Could%20Fly.flac"><em>Back When I Could Fly</em></a>
</ol>
</blockquote>

<p> Not only can us humans make sense of that, but it's 
got RDFa attributes sprinkled here
and there that make it yummy Semantic Web Data
so that we can delegate processing to machines:

<p> <pre>
Jukebox$ xsltproc --novalid
http://www.w3.org/2008/07/rdfa-xslt three_chords.html 
&gt;three_chords.rdf
Jukebox$ rapper three_chords.rdf -o turtle | less
rapper: Parsing file three_chords.rdf with parser rdfxml
rapper: Serializing with serializer turtle
rapper: Parsing returned 77 triples
</pre>

<p> and out comes:

<p> <pre>
@prefix h: &lt;http://www.w3.org/1999/xhtml&gt; .
@prefix dc: &lt;http://purl.org/dc/elements/1.1/&gt; .
@prefix foaf: &lt;http://xmlns.com/foaf/0.1/&gt; .
@prefix mo: &lt;http://purl.org/ontology/mo/&gt; .

<p> &lt;three_chords.rdf#album1&gt;
    dc:title "A Song's Best Friend_ The Very Best Of John
Denver [Disc 1]" ;
    mo:track
&lt;artists-popular/John%20Denver/A%20Song%27s%20Best%20Friend_%20The%20Very%20Best%20Of%20John%20Denver%20%5BDisc%201%5D/1-04%20Poems%2C%20Prayers%20And%20Promises.mp3&gt;
;
    a mo:Record ;
    foaf:maker &lt;three_chords.rdf#agent1&gt; .

<p> &lt;three_chords.rdf#agent1&gt;
    a foaf:Agent ;
    foaf:name "John Denver" .

<p> </pre>


<p> In my March 2008 item, <a href="http://dig.csail.mit.edu/breadcrumbs/node/228">hAudio
for microformats mixtapes, in progress</a>, I tried using
microformats but struggled since hAudio was still sparsely
documented and changing. In contrast, RDFa and the music
ontology were pretty easy to work with.

<p> As I said in my Aug 2008 item, <a href="http://dig.csail.mit.edu/breadcrumbs/node/240">The details of data in documents; GRDDL,
profiles, and HTML5</a>, one of the options
is that "People who want to put data in their HTML
documents use <a href="http://esw.w3.org/topic/RDFa">RDFa</a>".

<p> I'm looking into getting metadata from the audio
file, not just the path name. In particular,
using the <a href="http://code.google.com/p/quodlibet/wiki/Mutagen">mutagen</a>
library I can see that iTunes stores CDDB IDs when it rips
music and I'd like to use those to ground
my data globally:

<p> <pre>
MPEG 1 layer 3, 160000 bps, 44100 Hz, 246.81 seconds (audio/mp3)
COMM=iTunNORM='eng'= 00000550 000001F3 00002A22 00002F25
00021A29 000219F5 0000707F 00006A4C 0003536D 0002B40A
TPE1=John Denver
TDRC=2004
TIT2=Poems, Prayers And Promises
TENC=iTunes v4.7
TRCK=4/20
TPOS=1/2
TALB=A Song's Best Friend: The Very Best Of John Denver [Disc 1]
COMM=iTunes_CDDB_IDs='eng'=20+F0DCFC688BB846194D1DA27AC6EAF16D+4607205
TCON=Country
TCOM=John Denver
</pre>


<p> Yet ToDo: connect this with <a href="http://neurocommons.org/page/ImmPort/PDB">ImmPort/PDB</a>
in neurocommons/science commons/creative commons work (<a href="http://svn.neurocommons.org/svn/trunk/convert/pdb-immport/">pdb-immport</a>
code in SVN),
 <a href="http://www.thenationaldialogue.org/ideas/linked-open-data">Linked
Open Data</a> for the U.S.A. recovery IT infrastructure,
and maybe XBRL stuff.


<p> See Also:

<p> <ul>
<li>
2007-07-22 <a href="http://www.advogato.org/person/connolly/diary/53.html">Music
Collections and Office Organization</a>

<p> <li>
2009-01-01 <a href="http://www.advogato.org/person/connolly/diary/61.html"><cite>Still
struggling to catalog CDs</cite></a>


</ul>