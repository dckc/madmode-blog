date: 2006-01-09
title: 'Arpeggio in D, a little three chord ditty'
published: True
tags: ['breadcrumbs']

<p>I ran across <a href="http://wolog.net/167009.html">Ping on improvisation</a> the other day. It seems he learned to play mostly from sheet music. I mostly learned by playing in a music group at church. I learned a few chords in a classroom setting, but mostly, I would sit down in the church group and George or Rudy would lead the group and I would try my best to follow. My crowing achievement was one day when neither of them was available; it was just me and a gal on flute, and we pulled it off. Unlike my friends with real talent that learned to play better than I ever will in their first year, it took me at least five years to achieve that level of competence on folk guitar. I need to hear the song <em>and</em> see the chords before I can play it. My ear training is proceeding very, very slowly; it took me years to learn to tune my own guitar.</p>

<p>I have picked up several guitars over the years, but it was years of wishing before we got a <a href="http://www.flickr.com/photos/dckc/82516278/">piano for our house</a> this year. It was out of tune enough that I could tell, and I had to leave it that way for a month while it settled. On the day of the tuning appointment, I was tidying up the piano room a bit and I couldn't help but sit down and plunk around a bit. The piano tuner  came in and asked if I was the piano player in the house; I said no, not really; my son was taking lessons; I just fake it, using my basic three-chord guitar sense. I was relieved that he didn't sneer at this approach, but rather agreed that they should teach chord progressions and the like to beginning piano players. In <a href="http://en.wikipedia.org/wiki/Ray_%28film%29">Ray</a>, there's a flashback that shows him learning more that way.</p>

<p>Anyway, I found <a href="http://wolog.net/167009.html">Ping's piece on music</a> just as I was running out of steam for technical work, so I headed down to the piano and worked on a few of the easier pieces of my guitar music. I goofed or got frustrated with one or something... and then I wandered into this 1-5-1 bass arpeggio<a href="#musterm">*</a> thing in D... first just I/IV I/IV... then before long the V chord (A) shows up... and after that got monotonous, a Bm bridge showed up. And then I could hear a melody in my head. I can't play well enough to do both the melody and the bass line at the same time, but going back and forth, I sorta worked it out: <img src="http://dm93.org/2006improv/arpegd-4.png" alt="a bit of sheet music" /></p>

<p>On the one hand, it's so simple that it's sort of embarrassing to call it an original composition. But it's not every day that my muse visits me this way, and I'm so in the habit of sharing in the Web that I started thinking about all the issues around <a href="http://meta.wikimedia.org/wiki/Music_markup">music markup</a> in the Web.</p>

<p>I'm not talking about mp3 vs ogg; I'm talking about sharing something editable:</p>

<blockquote>
<p>There are very few data formats I trust... when I use
the computer to capture my knowledge, I pretty
much stick to plain text, XML (esp XHTML, or at least HTML that
tidy can turn into XHTML for me), RCS/CVS, and RFC822/MIME.</p>

<p>I use JPG, PNG, and PDF if I must,
but not for capturing knowledge for exchange, revision, etc.</p>

<div><cite><a href="http://lists.w3.org/Archives/Public/www-rdf-interest/2000Jul/0020.html">July 2000 to rdf-interest</a></cite></div>
</blockquote>

<p>GarageBand is a blast; I'm really afraid of becoming addicted to it and locking up all my music in there. Version 2 has support for western music notation. Plus, it lets you record tracks separately and mix them. So I gave that a whirl; you can listen to
<a href="http://dm93.org/2006improv/arpeg-d.mpg">arpeg-d.mpg</a>,
mistakes and all;
but there doesn't seem to be any way to get the music notation <em>out</em> of GarageBand. <q>The extraction of data created in GarageBand does not appear to be an easy task</q> -- <cite><a href="http://homepage.mac.com/beryrinaldo/ddm/">Dent du Midi FAQ</a></cite>.</p>

<p>This is not the first time I have been in this position; I wrote a few songs in college and transcribed them on my Macintosh SE circa 1988. When I recovered the files a couple years ago, I searched for a more modern format and found <a href="http://en.wikipedia.org/wiki/ABC_%28musical_notation%29">ABC music notation</a> that is editable and convertable to postscript sheet music and MIDI; fortunately, the Studio Session format documentation survived and I could write a <a href="http://dev.w3.org/cvsweb/2002/songvert/">a python ditty</a> to convert my data.</p>

<p>So tonight I captured <cite>Arpeggio in D</cite> for sharing:</p>

<ul>
<li><a href="http://dm93.org/2006improv/arpegd.abc">arpegd.abc editable notation</a></li>
<li>
<a href="http://dm93.org/2006improv/arpegd.pdf">arpegd.pdf sheet music</a>, and</li>
<li>
<a href="http://dm93.org/2006improv/arpegd.midi">arpegd.midi playable music note data</a></li>
</ul>

<p>... and a <a href="http://dm93.org/2006improv/Makefile
">makefile</a> to tie them together. I haven't really decided on the melody for the bridge, and abc2midi doesn't grok the bass cleff extension so the bass should sound two octaves lower. But there you have it.</p>


<p><em id="musterm">* reading up on <a href="http://en.wikipedia.org/wiki/Musical_terminology">musical terminology</a>, I see that I'm perhaps misusing the term <em>arpeggio</em>; it's really a broken chord.</em></p>

<p>see also: 
<a href="http://www.advogato.org/person/connolly/diary.html?start=41">advogato item</a>, 
<a href="http://dm93.org/z2001/ThreeChordsAndTheTruth">notes on debian linux and music tools</a></p>