title: 30 Sep 2005
date: 2005-09-30
tags: ['python', 'scm', photo]
published: true
summary: So I want to post a journal/blog entry about my recent trip
	 to Edinburgh for a TAG meeting. How and where to post it?

So I want to <b>post a journal/blog entry</b> about my recent trip to Edinburgh for a TAG meeting. How and where to post it?
<ul>
<li>advogato? It's not really about open source. Advogato doesn't support offline editing -- well, I suppose I could upload it via <a href="http://www.advogato.org/xmlrpc.html">the XML-RPC control protocol</a>. Advogato seems to mangle my text. I like to keep to XHTML.
<li>w3.org? It's got product endorsements. I don't have an RSS feed there... though... hmm... I could use <a href="http://www.w3.org/2000/08/w3c-synd/">my XHTML site summary hack</a> to make one out of my homepage pretty easily. Unlike most weblog systems, posting the content would be a separate transaction from making the RSS entry, but maybe that's OK... it would let me use mailng lists posts as entries, as well as advogato posts, flickr photos, etc. It's not <a href="http://esw.w3.org/topic/ImmersiveHypertextEditing">ImmersiveHypertextEditing</a>, but emacs with nxml-mode combined with CVS and ssh is a pretty nice way to edit the web.
</ul>
<p> So I'm thinking about adding blog-smarts to dm93.org. 
As I mentioned <a href="http://www.advogato.org/person/connolly/diary.html?start=25">earlier</a>,
I'm disenchanted with ZopeDB as the back end. I liked Zope's ease of access control, but the cost of being different from apache is just too high. I'd sure like to see <a href="http://www.openid.net/">openid</a> support integrated with apache .htaccess stuff. Maybe a fastcgi auth hack of some sort. Anyway... back to blogging...
&lt;"&gt; I want to use the filesystem with <a href="http://www.selenic.com/mercurial/">hg</a>. I see there's a <a href="http://packages.debian.org/pyblosxom">
debian package for pyblosxom</a>.
I'm also interested in flickr's support for weblogging APIs. I see there's a
<a href="http://pyblosxom.sourceforge.net/blog/registry/xmlrpc/bloggerapi">bloggerapi module</a> for pyblosxom. I would prefer the Atom protocol.
I am reading <cite><a href="http://www.xml.com/pub/a/2004/04/14/atomwiki.html">An Atom-Powered Wiki</a></cite>
by Joe Gregorio April 14, 2004. I wonder if the protocol has changed much since then.
<p>update on <a href="http://www.advogato.org/person/connolly/diary.html?start=19">testing gnome blog etc.</a>: While waiting in the Kansas City airport recently, I had just enought time to download xjournal,
recommended by <a href="http://www.pure-mac.com/webed.html">Pure
Mac's list of web editors</a>. The "mood" field is kinda cool, as is the "get music button". I tried
to copy and paste from<a href="http://dm93.org/z2001/TravelCheckList">TravelCheckList</a>
in my wiki, but it came across as plain text. Bzzt.
<p> tags: <a href="http://del.icio.us/connolly/python" rel="tag">python</a>, <a href="http://del.icio.us/connolly/scm" rel="tag">scm</a>
