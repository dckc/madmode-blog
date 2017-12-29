date: 2006-03-21
title: 'no more life in a textarea: MozEx and emacs to the rescue!'
published: True
tags: ['breadcrumbs']

<div>

<p>I have been <a
href="http://ifindkarma.typepad.com/relax/2005/01/life_in_a_texta.html">living
in a textarea</a> since I started this blog, always a little nervous,
knowing that firefox doesn't know that <a
href="http://esw.w3.org/topic/IntegrityIsJobOne">integrity is job
one</a>. That is: Firefox doesn't guarantee to save all work, by
default; I don't consider that a big bug; it's a browser, not an
editor, after all. I outsourced bookmarking to <a
href="http://del.icio.us/connolly/w3c">delicious</a> because that's
knowledge capture, and I don't rely on my browser for that.</p>

<p>But as TimBL has been saying since at least as far back as his <a
href="http://www.w3.org/DesignIssues/Editor.html">1998 design
issues note</a>,</p>

<blockquote>
<p>If you think surfing hypertext is cool, that's because you haven't
tried writing it. If you have found your bookmarks/favorites have
become a more and more important part of your life, that's because you
have learned to put up with the simplest form of hypertext editing
there is as a compromise.</p>
</blockquote>

<p>Then we have <a href="http://weblog.infoworld.com/udell/2005/07/06.html">
Udell July 06, 2005</a>:</p>

<blockquote>
<p>Now, with oceanic quantities of text pouring through the TEXTAREAs
of blogging tools and webmail applications, the situation is just
insane.</p>
</blockquote>

<p>I'll say. Silly me, just last week at the <a
href="http://www.w3.org/2005/Security/usability-ws/">security
workshop</a> I jinxed myself by explaining to <a
href="http://www.xmlgrrl.com/blog/">Eve</a> that the first thing I do
with any mail client or other editor is type "Four score and seven
year ago--" and then <strong>yank the power cord</strong> and see how
robust the thing is. Emacs knows to save my work.  So does
evolution. Apple mail does too. Thunderbird doesn't, so I don't use
thunderbird, even though evolution isn't available for my laptop and
Apple's mailer doesn't handle threads as nicely, and does some really
annoying things with linebreaks and URIs.</p>

<p>Sure enough, while writing one of the next few items, firefox
crashed and took an hour's worth of work with it. It's completely
gone. The bits are nowhwere. I tried <tt>grep</tt> on the swapfile.
Nope. I was dumbfounded. I haven't let a computer throw away that
much of my work for years and years. I don't really do backups,
but I'm known as a "closet librarian" for my dilligence with
email and CVS:</p>

<blockquote>
<p>
There are very few data formats I trust... when I use
the computer to capture my knowledge, I pretty
much stick to plain text, XML (esp XHTML, or at least HTML that
tidy can turn into XHTML for me), RCS/CVS, and RFC822/MIME.
</p>
<cite><a href="http://lists.w3.org/Archives/Public/www-rdf-interest/2000Jul/0020">July 2000 to www-rdf-interest</a>
</cite>
</blockquote>

<p> I re-wrote <a
href="http://dig.csail.mit.edu/breadcrumbs/node/99">the item</a>, but
I'll never know if I covered all the same ground.</p>

<p>I had seen gizmos to integrate emacs with textareas.  This was
motivation to go find them. I'm happy to report that <a
href="http://www.gatsby.ucl.ac.uk/~iam23/code/mozex/">Mozex with UTF-8
in Firefox 1.5</a> works (after a couple <a
href="http://chatlogs.planetrdf.com/swig/2006-03-21#T03-50-25">configuration
hassles</a>). Thank you, Iain Murray! I found it via <a
href="http://en.wikipedia.org/wiki/Wikipedia:Text_editor_support">wikipedia
tools notes</a>.
</p>

<p>Yay! I get to use <a
href="http://www.thaiopensource.com/nxml-mode/">nxml-mode</a> when
writing weblog items!</p>

</div>