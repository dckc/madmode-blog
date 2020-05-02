date: 2011-07-26
published: true
tags: [economics, security, web standards]
title: 'Secure Mashups: CSRF-resistent alternatives to WebID'
updated: 2011-07-26


I think <a href="http://www.w3.org/wiki/WebID">WebID</a> is headed in the wrong direction.&nbsp;It separates authorization from authentication, which is <a href="http://en.wikipedia.org/wiki/Ambient_authority">widely believed</a> to be a good practice, but proves spectacularly bad practice when it leads to <a href="http://en.wikipedia.org/wiki/Cross-site_request_forgery">cross-site request forgery</a>.&nbsp;&nbsp;I have tried to explain my misgivings to the WebID proponents, but I didn't have much in the way of an alternative to suggest. Until today, when I found <a href="http://www.sitelier.com/">Sitelier</a> and&nbsp;<a href="https://sites.google.com/site/belayresearchproject/">Belay Research</a>.<br />
<br />
<a name='more'></a>While evaluating&nbsp;<a href="http://static.springsource.org/spring-security/site/index.html">Spring Security</a>&nbsp;today, I went looking to see if it its role-based architecture is in any way compatible with capability-based approaches and I found <a href="http://www.eros-os.org/pipermail/cap-talk/2011-July/014943.html">this, from the Sitelier guys</a>:<br />
<br />
<blockquote>
In our view, the web right now is backwards: users have accounts on dozens&nbsp;of websites, all with their own logins and passwords, and our content and&nbsp;personal information is scattered all over the web, out of our control.&nbsp;Sitelier turns the situation around: when you install an app, you're&nbsp;effectively creating an account on <i>your</i> site for the app, which can then&nbsp;save its data (your data) there, so all your online information can live in&nbsp;one secure location that you control.</blockquote>
Replies pointed out related work such as&nbsp;<a href="https://sites.google.com/site/belayresearchproject/">Belay Research</a>&nbsp;and emphasized usability research. Indeed, my understanding since at least as far back as <a href="http://www.w3.org/QA/2008/12/web_applications_security_requ.html">my Dec 2008 post</a> is that the capability approach is the necessary and sufficient solution to the problem of secure mashups; the only question is: given the worse-is-better tendency in software deployment, is there any chance we can move the state-of-the-art that far?<br />
<br />
There are also some market forces to consider. If I host my own email, how do get sub-second search a la ad-powered gmail?<br />
<br />
<br />