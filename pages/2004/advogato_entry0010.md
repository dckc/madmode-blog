title: A search for usb midi keyboard support and an example of great open source software marketing
date: 2004-03-26
tags: []
published: true

<b>A search for usb midi keyboard support and an example of great open source software marketing</b>



<p> <blockquote>Beast is a powerful music composition and modular synthesis application released as free software under the GNU GPL and GNU LGPL, that runs under unix. It supports a wide range of standards in the field, such as MIDI, WAV/AIFF/MP3/OggVorbis/etc audio files and LADSPA modules. It has excellent technical abilities like multitrack editing, unlimited undo/redo support, real-time synthesis support, 32bit audio rendering, full duplex support, multiprocessor support, precise timing down to sample granularity, on demand loading of partial wave files, on the fly decoding and full scriptability in scheme. The plugins, synthesis core and the user interface are actively being developed and translated into a variety of languages, regularly assimilating user feedback such as from our FeatureRequests page.
 --  <a href="http://beast.gtk.org/about.html">about beast</a>
</blockquote>

<p> Yay! That's exactly what I wanted to know about it.
(I'm still looking for a blurb about
<a href="http://plone.org/">plone</a> that will
serve the same purpose.)

<p> I have an m-audio keystation 49e usb-keyboard (a <a href="//www.apple.com/ilife/garageband/accessories.html">garage band accessory</a>) and I wanted to see if it would
work with any open source software.

<p> After restarting hotplug, I got as far as:

<p> <pre>Bus 002 Device 005: ID 0a4d:0090 Evolution Electronics, Ltd</pre>

<p> Then I tried apt-cache search midi, but (a) I couldn't
really tell from the descriptions which one was likely
to work, and (b) the first few I tried spewed
screenfuls of diagnostics and keeled over.
(<a href="//www.ilrt.bris.ac.uk/discovery/chatlogs/rdfig/2004-03-26.html#T03-09-20">notes</a> ).

<p> OK, so debian's core competency is not multimedia.
So I went up the food chain, to gnome... a search
for midi in their footnotes zine yielded a
<a href="http://www.gnomedesktop.org/article.php?sid=1708">beast release article</a>. So I followed the link and I was
very pleased to find an attractive website with both
the latest news <em>and</em> the basic about blurb above.

<p> Then I discovered there's a <a  href="http://packages.debian.org/beast">beast debian package</a> after all. I fired it up... no spew
of diagnostics... demo right there in the menu... and
it works! wow! (ok, a few diagnostics there, but
hey, I've got some candy already...). And in the help
menu, I find a quickstart guide! Yeah!

<p> Too many open source projects tout "it's completely
extensible: you can write your own modules!" before
they explain the hello-world features of the app.

<p> But using a midi keyboard wasn't covered in the quickstart
guide.

<p> But hey! There's an IRC channel... and the developer
was right there and gave me some real-time support...
enough to discover that /dev/midi wasn't working.
(cat should show output when you play the keys.)

<p> Now that I've done my chearleading, anybody wanna help
me out? send me some mail or visit
<a href="http://wiki.debian.net/index.cgi?QandA">QandA
in the debian wiki</a> and help the whole community out.

<p> hotplug seems to relate the device to the  "audio" module in 2.4.16. Do I need to use alsa?

<p> <p>
I read the <a href="//www.midi-howto.com/">linux midi howto</a>, but it doesn't suggest any software that you can use to confirm that your hardware setup is right. in particular, it says to look at /dev/sndstat, but I get "no such device", even though sound output is working fine. 

