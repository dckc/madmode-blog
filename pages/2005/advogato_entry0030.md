title: 15 Jul 2005
date: 2005-07-15
tags: ['python', 'scm']
published: true

I finally got a copy of the contents of <a href="http://dm93.org/z2001/">my personal wiki</a> converted to clean XHTML, one of the <a href="http://lists.w3.org/Archives/Public/www-rdf-interest/2000Jul/0020">few formats I trust</a>. After fixing a bunch of low level escape markup problems with regex foo, I remembered that wiki rendering mixes up tag nesting. So I needed <a href="http://www.w3.org/People/Raggett/tidy/">tidy</a>. <a href="http://effbot.org/zone/element-index.htm">ElementTree</a> and <a href="http://effbot.org/zone/element-tidylib.htm">TidyHTMLTreeBuilder</a> to the rescue! Now the hard part: migrating from the wiki genre to the journal/blog genre.

<p> <p> This work started in a CVS repository that I keep on a mac that goes to sleep at night. I usually <tt>etherwake</tt> it, but tonight I used <a href="http://www.selenic.com/mercurial/">hg</a> and committed changes right on the machine I'm working on, and pushed them to another machine when I finished.
I missed emacs integration, but not too badly.

<p> <p> I like the idea of all my machines acting as peers, but I wonder if I'll lose track of which changes are where. And I wonder when to add to an existing project/repository and when to make a new one. When it comes to moving files around, hg is less constrained than CVS but still has limitations. And moving things in the web involves redirects, if not broken links. If I want to publish the code, I doubt I'll use an hg server or even an hg CGI; I'd probably use a commit hook to update some static files, or not even bother with a repository on the server but just use rsync.


<p> <p> Tags: <a rel="tag" href="http://del.icio.us/connolly/python">python</a> <a rel="tag" href="http://del.icio.us/connolly/scm">scm</a>
