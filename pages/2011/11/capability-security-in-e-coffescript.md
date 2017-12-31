date: 2011-11-23
published: true
tags: ["security", "capabilities", "programming", 'scala']
title: Capability Security in E, coffescript, python, dart, and scala
updated: 2011-11-23


A couple months ago, I inherited some Java code and took on the task of fixing a bug in it. The bug turned out to be a consequence of a silent failure; eek! And there were precious few tests and no way to test the parts without being connected to LDAP servers and SQL databases and such. This started me on an exploration of <a href="http://jakegoulding.com/blog/2011/10/10/learned-about-testing-last-year/">current best practices in testing</a>. And since the job of this code was policy enforcement around patient data, I could finally justify getting my hands dirty with <a href="http://en.wikipedia.org/wiki/Capability-based_security">capability-based</a> security. I discovered, as many others have, that both testability and security are well served by some of the same basic object-oriented techniques.<br />
<br />
 Dependency injection frameworks always smelled like overkill to me, but after watching <a href="http://misko.hevery.com/2011/02/14/video-recording-slides-psychology-of-testing-at-wealthfront-engineering/">Miško Hevery on testability</a>, I was convinced. <i>If you're in the mood for text rather than video, see his <a href="http://misko.hevery.com/code-reviewers-guide/">Guide: Writing Testable Code</a>.</i> Basically, instead of having some policy enforcement object constructor call an LDAP connection constructor, the policy enforcement object takes the LDAP connection as a constructor argument. "Don't call us; we'll call you" is a handy mnemonic. This lets you substitute a mock LDAP connection for testing.<br />
<br />
It also forms patterns of cooperation without vulnerability.<br />
<br />
For example, take a look at the <a href="http://www.erights.org/elib/capability/ode/ode-capabilities.html">simple money example in E</a> and the underlying <a href="http://wiki.erights.org/wiki/Walnut/Secure_Distributed_Computing/Capability_Patterns#Sealers_and_Unsealers">sealer/unsealer</a> pattern.<br />
<br />
I have been using these as an exercise to explore some of the recent programming language developments:<br />
<ul>
<li><a href="https://bitbucket.org/DanC/coffee-craft/src/682d06f02e99/money.coffee">money.coffee</a> in August </li>
<li><a href="http://informatics.kumc.edu/work/browser/raven-j/heron_wsgi/admin_lib/sealing.py">sealing.py</a> in October </li>
<li><a href="https://gist.github.com/1357307">money.dart</a> November 10 </li>
<li><a href="https://gist.github.com/1357438">money.scala</a> November 11</li>
</ul>
The coffeescript translation seems completely natural, to me. Given the right static scope (i.e. without most of the JavaScript standard library), I think it has the same security properties as the E version. And the E idioms seemed to translate quite directly.<br />
<br />
Python has not only the API authority issues, but also untold introspection loopholes. Plus, I had to kludge around read-only closures and no-assignment-in-lambdas; and while simulating E's method suite idiom is not <i>too</i> ugly, tools like pyflakes don't recognize the results.<br />
<br />
Dart is a big disappointment. Everywhere else I look, Google is pushing capability security. But Dart lacks nested classes, so translating E method suites results in something that is only vaguely recognizable, let alone comprehensible.<br />
<br />
Scala works reasonably well. The <a href="http://gitorious.org/repo-roscidus/e-core/blobs/fdf9643e419eea182b4d8d983f5b9955c7b73967/src/jsrc/org/erights/e/elib/sealing/SealedBox.java">Java implementation of sealing</a> relies more on&nbsp; strong typing than the object graph for rights amplification; I might want to think that over some more. Also, It's a little boring to spell out the types. I might have to try it in Haskell. But on the other hand, as <a href="http://brendaneich.com/2010/08/static-analysis-ftw/">Brendan Eich observes</a>:<br />
<blockquote class="tr_bq">
Dynamic languages are <a href="http://weblogs.mozillazine.org/roadmap/archives/2008/04/popularity.html">popular</a>
 in large part because programmers can keep types latent in the code, 
with type checking done imperfectly (yet often more quickly and 
expressively) in the programmers’ heads and unit tests, and therefore 
programmers can do more with less code writing in a dynamic language 
than they could using a static language.</blockquote>
The balance between static and dynamic languages also shows up in development tools. I had the eclipse with the <a href="http://code.google.com/p/joe-e/">Joe-E</a> verifier, maven, and mercurial working all together at home one evening. The code really does just about write itself at that point. But when I tried to reproduce it at work, I got so frustrated that I retreated to emacs and python and looking up function arguments manually. The python version of the project has gotten complex enough that I'm starting to miss some of the whole-program consistency that Java tools give, but I'm getting by with a bottom-up approach: flymake, doctest, and the like.<br />
<br />
<br />
