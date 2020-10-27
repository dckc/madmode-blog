date: 2007-05-17
title: 'IKL by Hayes et al. provides a semantics for N3?'
published: True
tags: ['breadcrumbs', 'reflection', 'semantic-web', 'logic', 'proof']

<p>One my <a href="/breadcrumbs/node/192">trip to Duke</a>, just after I arrived on Thursday, Pat Hayes gave a talk about <a href="http://www.ihmc.us/users/phayes/IKL/GUIDE/GUIDE.html">IKL</a>; it&#39;s a logic with nice Web-like properties such as <em>any collection of well-formed IKL sentences is itself well-formed</em>. As he was talking, I saw lots of parallels to N3... propositions as terms, log:uri, etc.</p><p>By Friday night I was exhuasted from travel, lack of sleep, and conference-going, but I couldn&#39;t get the IKL/N3 ideas out of my head, so I had to code it up as another output mode of <a href="http://www.w3.org/2000/10/swap/n3absyn.py">n3absyn.py</a>.</p><p>The <a href="http://lists.w3.org/Archives/Public/www-archive/2007Apr/0056.html">superman case</a> works, though it&#39;s a bit surprising that <u>rdf:type</u> gets contextualized along with superman. The <a href="http://lists.w3.org/Archives/Public/www-archive/2007Apr/thread.html#msg57">thread</a> continues with the case of &quot;if your homepage says you&#39;re vegetarian, then for the purpose of registration for this conference, you&#39;re vegetarian&quot;. I&#39;m still puzzling over Pat&#39;s explanation a bit, but it seems to make sense. </p>  <p>Along with the <a href="http://www.ihmc.us/users/phayes/IKL/SPEC/SPEC.html">IKL spec</a> and <a href="http://www.ihmc.us/users/phayes/IKL/GUIDE/GUIDE.html">IKL Guide</a>, Pat also suggests:</p> <ul><li><a href="http://ontolog.cim3.net/cgi-bin/wiki.pl?ConferenceCall_2006_10_26">conference call on IKL</a>, including a slideshow and even a recorded talk</li> <li> another <a href="http://www.ihmc.us/users/phayes/IKL/IKRIS_MV.ppt">slightly earlier powerpoint slideshow</a></li> </ul>  