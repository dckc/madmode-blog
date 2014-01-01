title: no longer happy with my personal wiki
date: 2005-06-10
tags: [aaronsw, publishing, writing]
published: true

I'm <a href="http://dm93.org/z2001/AboutThisWiki#msg20050608050701+0000@dm93.org">no longer happy with my personal wiki</a>; since upgrading to a version of zwiki that supports dated comments, I find that I'm more comfortable doing "episodic publishing" (i.e. blogging) than collaborating on collected wisdom. <b>A personal wiki is an oxymoron; the wiki genre is all about collaboration</b>.

<p> So I started thinking about how to migrate my content to a blogging system. The first step was to somehow grok all the data I've got in there. I asked in the #zope channel about .zexp format and was discouraged from peeking inside. I was advised to write an
<a href="http://www.zope.org/Documentation/Books/ZopeBook/2_6Edition/ScriptingZope.stx">external method</a> that runs inside Zope to export my data,
but by the time I saw that advice, I already had dumpwiki.xsl converting the zope XML export format to XHTML. The actual contents of the wiki pages was quoted, so I'm undoing that with python and <a href="http://www.aaronsw.com/2002/xmltramp/">xmltramp</a>. I think I hit a bug in the xmltramp serializer. Gotta look into that.

<p> Anyway... the #zope guys were surprised that I had never done any Zope methods. I explained that I use Zope because it's the only server you can apt-get and write to (with iPhoto or emacs eldav mode) out of the box, with elephant-never-forgets versioning.

<p> That got me thinking... with the <b>"cvs is good enough" orthodoxy eroding</b>, and all the work on subversion and arch and darcs, maybe it's time to take another look at the versioning part of WebDAV. Especially git, with its cryptographically secure history... because <b>the problem with   the <a href="http://www.oreillynet.com/pub/t/84">writeable web</a> is more social than technical.</b> People use sftp rather than HTTP because the social protocol is well known, not because FTP is a better protocol than HTTP for writing.

<p> Hmm... if I had a <a rel="tag" href="http://www.policyawareweb.org/">PAW</a> blog or a <a href="http://groups.csail.mit.edu/dig/" rel="tag">DIG</a> blog, this might belong there. Maybe reltag will work...

<p> I sure wish python had more penetration in the blogging world. PHP is clearly the server-side deployment vehicle these days, and javascript is the way to juice up clients, but <b>neither PHP nor javascript  meets the <a href="http://www.w3.org/TR/1998/NOTE-webarch-extlang-19980210#Ambiguity ">unambiguity requirement</a> that I think is critical for software engineering in the large.</b>
