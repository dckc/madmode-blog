date: 2010-08-09
published: true
tags: []
title: Setting up project tracking with trac, hg, and a little help from my friends
  on freenode
updated: 2010-09-17


<div class="separator" style="clear: both; text-align: center;"><a href="http://www.kumc.edu/guides/jobguide.html" imageanchor="1" style="clear: left; float: left; margin-bottom: 1em; margin-right: 1em;"><img border="0" src="https://www.kumc.edu/templates/images/masthead_logo.gif" /></a></div><div style="text-align: right;"><b>We're hiring!</b>&nbsp;Interested? Apply for the&nbsp;<a href="https://jobs.kumc.edu/applicants/jsp/shared/position/JobDetails_css.jsp?postingId=371958">Biomedical Informatics Software Engineer position</a>.</div><br />
<br />
One of my first tasks here was setting up version control. The guy who hired me, Russ, had experience with svn and especially <a href="http://trac.edgewall.org/wiki/TracBrowser">TracBrowser</a>&nbsp;and was aware of the trend toward distributed version control. While git has a 1st-mover advantage and bzr is maturing, I have been using mercurial (hg) since before github and the like made git's user interface tolerable and before bzr's performance was acceptable. Between Joel Spolsky's excellent <i><a href="http://hginit.com/top/">Hg Init</a></i> tutorial and the <a href="http://tortoisehg.bitbucket.org/">TortoiseHg</a> windows shell integration, it wasn't hard to get mercurial adopted as our version control system.<br />
<br />
<a name='more'></a><br />
<br />
Of the three, bzr is the only one that does 1st-class renames (including directories); I'm betting we won't need to cross that bridge for some time.<br />
<br />
Mercurial's limitations around big files never bothered me before; I formed my version control habits with CVS, which handles binary files about as well as my teenage boys handle vegetables: only when given very specific instructions and even then, not gracefully. But there are a lot of Microsoft Office documents around here, this being an enterprise with largely pre-web computing norms.&nbsp;As a web guy, my sentiments are largely with Edd:<br />
<span class="Apple-style-span" style="color: #333333; font-family: arial, sans-serif; font-size: 13px;"><br />
</span><br />
<blockquote>But really, office documents make me cry.<br />
<br />
--&nbsp;<a class="bookmark_title " href="http://bitten.twiceshy.org/platform-agnostic-productivity">Platform agnostic productivity - once bitten</a></blockquote><br />
But that's where the information is, so I took a few a MS Word documents and put them in our mercurial repository. Once I realized what a hassle it would be to merge diffs in MS Word documents (is it even possible?) I realized it made more sense to put them in our trac wiki as attachments.<br />
<br />
Trac turns out to be a great fit for our group. I knew from experience that bugzilla is a hassle that's only worthwhile in communities several orders of magnitude larger than ours. My other experience was with <a href="http://roundup.sourceforge.net/">roundup</a>, whose web interface is so smooth that you can just about&nbsp;capture status at the rate &nbsp;developers discuss issues around a table. I knew that I wanted an issue tracking system, but I wasn't sure whether the integrated wiki and source code browsers would help us out or just get in the way. The wiki turns out to be a great catalyst for the switch from mailing copies around at each iteration to working in a shared web space. MS Word documents can be thrown in as attachments at first and migrated to hypertext in due course.<br />
<br />
At first the tickets were just a way for me to track my own work, but we're getting pretty good at using trac for an approximation of the <a href="http://xprogramming.com/xpmag/whatisxp#planning">XP planning game</a>: Russ plays business customer and I represent development. Sometimes sketching milestones and breaking them down into tickets is straightforward enough, but sometimes I don't understand what he's asking for, so I ask him to tell me stories about how it works, and we capture those in the wiki.<br />
<br />
It's working well enough that some people are considering it as an alternative to MS Sharepoint in a few cases. I wonder how the cost of setting sharepoint compares to what I've been through with trac:<br />
<br />
<ul><li>The initial stand-alone installation of trac worked fine, but when I tried to integrate it with apache via mod_wsgi, I ran into shared library conflicts. Fortunately,&nbsp;<a href="http://code.google.com/p/modwsgi/wiki/IssuesWithExpatLibrary">IssuesWithExpatLibrary</a> are well documented and the fix was just:</li>

<ul><li><span class="Apple-style-span" style="font-family: 'Courier New', Courier, monospace;">sudo zypper install libexpat-devel</span><br />
<i>zypper? what's that?</i>&nbsp;It's the SuSE equivalent to apt-get. The enterprise investment in Novell spills over into using SuSE linux rather than debian or Ubuntu.</li>
<li>rebuild apache with&nbsp;<span class="Apple-style-span" style="font-family: monospace; font-size: small; line-height: 16px;">--with-expat=/usr/lib</span></li>
</ul>
<li>Trac has a <a href="http://trac-hacks.org/wiki/TracCasPlugin">traccas plug-in</a> for the campus single sign-on system,&nbsp;<a href="http://www.jasig.org/cas">CAS</a>. I ran into redirect loops when I first set it up; not to fear: it's a a known bug (<a href="http://trac-hacks.org/ticket/4025">ticket 4025</a>) and the fix was just to give &nbsp;<span class="Apple-style-span" style="font-family: 'Courier New', Courier, monospace;">repository_dir</span> a good value in the trac.ini configuration file.</li>
<li>In one of the projects here, we provide requirements to a vendor. To help track which requirements are satisfied by a recent code drop, I took the MS Word document with the current table of requirements, saved it as HTML, tidied it, shuffled the columns around a bit with a 50-line python script, and imported it with the&nbsp;<a href="http://trac-hacks.org/wiki/TicketImportPlugin">TicketImport plug-in</a>&nbsp;(which is really great because it can do updates as well as inserts).</li>

<ul><li>It seemed a little silly to use .xls rather than .csv for the import, but the data had unicode quotes and the&nbsp;<a href="http://pypi.python.org/pypi/xlwt/0.7.2">xlwt</a>&nbsp;package is unicode-happy while python's csv module isn't.</li>
</ul>
<li>One of the services provided by our department has an established workflow. I'm experimenting with representing it in trac. I added a custom <a href="http://trac.edgewall.org/wiki/TicketTypes">ticket type</a> and used the <a href="http://trac-hacks.org/wiki/MultipleWorkflowPlugin">MultipleWorkflow plug-in</a> to give it a custom workflow. The jury is still out on whether we'll adopt trac to manage this service.</li>
</ul>The difference in license fees is easy enough to compute: it's whatever sharepoint costs minus zero, since all of the above is free software. Perhaps I spent more time setting it up than sharepoint administrators do, but I suspect that even so, there's some leftover that I should arrange to donate to <a href="http://freenode.net/">freenode</a>, which provides discussion facilities: the #trac channel (thanks coderanger!) and #mercurial and #pythonpaste and #httpd and #suse. Next time you're stuck or you just want to bounce ideas off others that are likely to be interested, give it a try.