date: 2010-01-20
title: 'Existentials in ACL2 and Milawa make sense; how about level breakers?'
published: True
tags: ['breadcrumbs', 'reflection', 'logic', 'proof', 'Austin']

<p>Since my <a href="/breadcrumbs/node/160">Sep 2006 visit to the ACL 2 seminar</a>, I&#39;ve been trying to get my head around existentials in ACL2. The lightbulb finally went off this week while reading Jared&#39;s Dec 2009 <a href="http://www.cs.utexas.edu/users/jared/milawa/Web/">Milawa</a> thesis.</p><blockquote><p>3.7 Provability</p><p>Now that we have a proof checker, we can use existential quantification to<br />decide whether a particular formula is provable. <strong>Recall from page 61 the notion<br />of a witnessing (Skolem) function.</strong> We begin by introducing a witnessing function,<br />logic.provable-witness, whose defining axiom is as follows.</p><p><br />Definition 92: logic.provable-witness<br />(por* (pequal* ...))</p><p>Intuitively, this axiom can be understood as: if there exists an appeal which is<br />a valid proof of x, then (logic.provable-witness x axioms thms atbl) is such<br />an appeal. </p></blockquote><p>Ding! Now I get it.</p><p>This witnessing stuff is published in other <a href="http://www.cs.utexas.edu/users/moore/publications/acl2-papers.html">ACL publications</a>, noteably:</p><ul><li>Structured Theory Development for a Mechanized Logic, M. Kaufmann and J Moore, Journal of Automated Reasoning 26, no. 2 (2001), pp. 161-203.</li></ul><p>But I can&#39;t fit those in my tiny brain.</p><p>Thanks, Jared, for explaining it at my speed!</p><p>Here&#39;s hoping I can turn this new knowledge into code that converts N3Rules to ACL2 and/or Milawa&#39;s format. N3Rules covers RDF, RDFs, and, I think, OWL2-RL and some parts of RIF. Roughly <a href="http://lists.w3.org/Archives/Public/public-cwm-talk/2009JulSep/0009.html">what stuff FuXi covers</a>.</p><p>I&#39;m somewhat hopeful that the rest of N3 is just quoting. That&#39;s the intuition that got me looking into ACL2 and Milawa again after working on some <a href="http://www.w3.org/2001/tag/dj9/story.html">TAG stuff using N3Logic to encode ABLP logic</a>. Last time I tried turning N3 {} terms in to lisp quote expressions was when looking at <a href="/breadcrumbs/node/193">IKL as a semantic framework for N3</a>. I didn&#39;t like the results that time; I&#39;m not sure why I expect it to be different this time, but somehow I do...</p><p>Another question that&#39;s keeping me up at night lately: is there a way to fit <a href="http://www.w3.org/2000/10/swap/doc/Reach">level-breakers such as log:uri</a> (or <a href="http://logic.stanford.edu/kif/dpans.html#10.1">name and denotation, if not wtr from KIF</a>) in the Milawa architecture somehow?</p><p>&nbsp;</p>