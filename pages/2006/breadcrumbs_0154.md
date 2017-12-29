date: 2006-07-31
title: 'OpenID, verisign, and my life: mediawiki, bugzilla, mailman, roundup, ...'
published: True
tags: ['breadcrumbs']

<div>
<p>Please, don't ask me to manage another password!
In fact, how about getting rid of most of the ones I already
manage?</p>

<ul>

<li>For the <a href="http://esw.w3.org/topic/DanConnolly">ESW
wiki</a>, there's <a
href="http://www.openidenabled.com/software/moinmoin">MoinMoin support
for OpenID</a></li>

<li>For the <a
href="http://microformats.org/wiki/User:DanC">microformats wiki</a>,
there's <a
href="http://www.openidenabled.com/software/mediawiki/">media wiki
support for OpenID</a></li>

<li>For <a
href="https://lists.csail.mit.edu/mailman/listinfo/tabulator-announce">CSAIL
mailing lists</a> there's <a
href="http://www.openidenabled.com/software/mailman/">mailman support
for OpenID</a></li>

<li>For <a href="http://www.w3.org/Bugs/">W3C qa tools bugs</a>,
there's <a href="https://bugzilla.mozilla.org/show_bug.cgi?id=294608">a patch to bugzilla</a>
</li>

<li>For this breadcrumbs site, there's <a href="http://www.openidenabled.com/software/drupal/">drupal support for OpenID</a></li>

</ul>

<p>I have sent support requests for some of these; the response
was understandable, if disappointing: <em>when debian/ubuntu supports
it, or at least when the core MailMain/mediawiki guys support it,
we'll give it a try</em>. I opened <a
href="http://dig.csail.mit.edu/issues/tabulator/issue18">Issue 18:
OpenID support in roundup</a> too; there are good OpenID libraries
in python, after all.</p>


<p>A nice thing about OpenID is that the service provider doesn't have
to manage passwords either.  I was thinking about where my OpenID
password(s) <em>should</em> live, and I realized the answer is:
nowhere. If we put the key fingerprint in the OpenID persona URL, I
can build an OpenID server does public key challenge-response
authentication and doesn't store any passwords at all.</p>

<p>As I sat down to tinker with that idea, I rememberd the <a
href="https://pip.verisignlabs.com/">verisign labs openid service</a>
and gave it a try. Boy, it's nice! They use the user-chosen photo
anti-phishing trick and provide nice audit trails. So it will
probably be quite a while before I feel the need to code my
own OpenID server.</p>

<p>I'm still <a href="http://dig.csail.mit.edu/breadcrumbs/node/55"
>hoping for mac keychain support for OpenID</a>.
Meanwhile, has anybody seen a nice gnome applet for keeping the
state of my ssh-agent credentials and my CSAIL kerberos credentials
visible?</p>

</div>
