title: Adventures with Mono
date: 2005-08-05
tags: ['programming', 'debian', 'media']
published: true

<b class="title">Adventures with Mono</b>

<p> <p> I just wanted some background music for reading and maybe cleaning up my office a little...

<p> <p> But I'm not really willing to manage my own cache of popular music; the <a href="http://www.riaa.com/about/default.asp">RIAA</a>/<A href="http://www.ascap.com/about/">ASCAP</a> rules cramp my style, which is to store stuff in the web and point to it from whichever of my N machines I happen to be using.

<p> <p> <a href="http://en.wikipedia.org/wiki/Podcasting">podcasting</a> sure sounds cool, though I'm not sure I grok. I searched for a gnome podcast tool and found <a href="http://usefulinc.com/edd/blog/contents/2005/06/17-monopod/read">monopod</a>. No, there's no debian package for it, but I just got a copy of Edd's
<cite><a href="http://usefulinc.com/edd/books/mono-notebook">Mono: A Developer's Notebook</a></cite>, so I thought I'd try to build monopod from <a href="http://downloads.usefulinc.com/monopod/monopod-0.2.tar.gz">source</a>.

<p> <p> untar it; blow past README and INSTALL and go straight to  <tt>./configure &amp;&amp; make</tt> and so begins the game of hunt-the-build-deps...

<p> <p> <pre>
checking for mono &gt;= 1.1.6... Package mono was not found
</pre>

<p> <p> so I counter with

<p> <p> <pre>
$ sudo apt-get install mono-devel mono-gmcs
</pre>

<p> <p> but that turns out to be a diversion; what I really needed was...

<p> <p> <pre>
$ sudo apt-get install libmono-dev
</pre>

<p> <p> Next hurdle:

<p> <p> <pre>
checking for gtk-sharp-2.0 &gt;= 1.9.5... Package gtk-sharp-2.0 was not found ...
</pre>

<p> <p> Easy enough:

<p> <p> <pre>
$ sudo apt-get install gtk-sharp2
</pre>

<p> <p> And lo! the configure script wins, but make fails thusly:

<p> <p> <pre>
./ChannelWindow.cs(144) error CS1501: No overload for method `SetSortFunc' takes `2' arguments
</pre>

<p> <p> Unfortunately, C# is not like python and Modula-3; it
fails the <a href="http://www.w3.org/TR/1998/NOTE-webarch-extlang-19980210#Ambiguity">unambiguitiy requirement</a> so I can't tell just by looking at <tt>ChannelWindow.cs</tt> where <tt>SetSortFunc</tt> comes from. I can see that it comes from <tt>ListStore</tt>.
Maybe an IDE will teach me the tricks for navigating C# files...

<p> <p> <pre>
$ sudo apt-get install monodevelop
</pre>

<p> <p> but starting monodevelop loses with

<p> <p> <pre>
System.Reflection.TargetInvocationException: Exception has been thrown by the target of an invocation.
---&gt; System.IO.FileNotFoundException:
Could not find file "/usr/lib/monodoc/monodoc.xml". : /usr/lib/monodoc/monodoc.xml
</pre>

<p> <p> but thanks to <a href="http://www.debian.org/distrib/packages">debian package search</a> it's easy enough to find the relevant package:

<p> <p> <pre>
$ sudo apt-get install monodoc-manual
</pre>

<p> <p> and now I can open <tt>ChannelWindow.cs</tt> in monodevelop, but when I hover over <tt>ListStore</tt>, I don't get any lisp-machine-like context-sensitive help. 

<p> <p> There are only a few imports at the top:

<p> <p> <pre>
using System;
using Gtk;
using Mono.Posix;
</pre>


<p> <p> So I'm willing to try a brute-force search. Aha... <a href="http://www.go-mono.com/docs/monodoc.ashx?link=T%3aGtk.ListStore">ListStore</a> in the Gtk# docs.

<p> <p> <tt>SetSortFunc</tt> takes 4 args. How did this code ever compile? I check for version skew... apt-cache policy and the README agree: Gtk# version 1.9.5. I don't get it.
<em>postscript: Edd suspects ETOONEW; he uses mono 1.1.7 and I got 1.1.8</em>

<p>  I try filling in 0s for the arguments, but C# is too strongly typed for that. I try to figure out what the C# equivalent of <tt>None</tt> or <tt>nil</tt> is for a <a href="http://www.go-mono.com/docs/monodoc.ashx?link=ecmaspec%3a22">delegate</a>, but it doesn't jump out at me.

<p> <p> Then... duh.. there's a <a href="http://usefulinc.com/edd/blog/contents/2005/07/31-monopod/read">monopod 1.4 release</a>. I grab that, but building it fails with:

<p> <p> <pre>
Internal() warning CS8018: Could not find the symbol writer assembly (Mono.CSharp.Debugger.dll). This is normally an installation problem. Please make sure to compile and install the mcs/class/Mono.CSharp.Debugger directory.
</pre>

<p> <p> OK, I give.

<p> <p> In some ways, the mono platform is coming along more quickly than Java, but the fact remains: <b>it takes a long time to deploy a new platform</b>. The <a href="http://wiki.debian.net/?MonoDebianPla">MonoDebianPlan</a> shows lots of scary packaging issues.

<p> <p> Tags:
<a rel="tag" href="http://del.icio.us/connolly/programming">programming</a>, 
<a rel="tag" href="http://del.icio.us/connolly/debian">debian</a>,
<a rel="tag" href="http://del.icio.us/connolly/media">media</a>, 


<p> <p> See also: <a href="http://www.ilrt.bris.ac.uk/discovery/chatlogs/swig/2005-08-02#T04-13-51">#swig notes</a> from tonight's journey.


