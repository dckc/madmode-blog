date: 2006-01-03
title: 'On Google, Jabber, and Jingle and good and evil in IM and IP networks'
published: True
tags: ['breadcrumbs']

<p>The 14 December <a
href="http://google-code-updates.blogspot.com/2005/12/jingle-bells.html">jingle
announcement</a> gives a hint into google's approach to adding voice
to their Google Talk offering. Actually, it gives quite a bit more
than a hint; it comes with a <a
href="http://www.jabber.org/jeps/jep-0166.html">jingle spec</a> and an
open source library implementation.</p>

<p>Google Talk has had pretty good "do no evil" karma since it
started. The dominant commercial IM services (AOL/Yahoo/Microsoft) are
each a world unto themselves. Your AIM screen name is just
<tt>jim47</tt> or whatever, not <tt>jim47@aol.com</tt> like an email
address, and while clients like trillian and gaim can connect to them
all, that's not something the big three encourage. Google Talk uses
gmail addresses and the Jabber/XMPP protocol, which has the same
network topology as email. While google isn't opening their service to
actual server-to-server federation until they get a better handle on
some operational issues (think: spam), they are using open protocols
and they actively support <a
href="http://gaim.sourceforge.net/about.php">gaim</a> development.</p>

<p>Apple's <a
href="http://www.apple.com/macosx/features/ichat/">iChat</a> uses
Jabber at some level too, though I haven't worked out the
interoperability issues in practice. I think the last time I tried was
before the Tiger release of OS X, when the Jabber support was much
more under-the-covers.</p>

<p>The popularity of multi-protocol clients like gaim and trillian
surprises me: after all, you can't have one chat room with AIM
<em>and</em> MSN messenger users connected. Evidently this just not a
big deal.  "IRC and instant messaging are very different paradigms,"
says the <a href="http://trac.adiumx.com/wiki/GettingOnIRC">Adium X: IRC
Howto</a>. I guess I'm just too old school to get it; in the <a
href="http://esw.w3.org/topic/InternetRelayChat ">internet relay chat
usage</a> that I'm used to, channels (aka chat rooms) are the norm and
private channels are the exception. I gather IM is the other way
around. I have played with Jabber's support for bridging to other networks, but I have yet to find a reliable combination of:</p>
<ul>
<li>a jabber client with bridging support that I can figure out how to use</li>
<li>and either
<ul>
<li>server software with bridging support that I can figure out how to use, or </li>
<li>an existing service with bridging support that I can use and trust (since my credentials pass thru their service)</li>
</ul>
</li>
</ul>

<p>The Jabber protocol has lots of pieces and extensions an such. There's a whole JEP process, in addition to the XMPP process where jabber technology feeds into the IETF. I don't quite have my head around the whole thing. I discovered that there are older and newer protocols for doing chat rooms in jabber that don't mix well. I wonder which of them, if either, the IETF has endorsed. An <a href="http://www.xmpp.org/summary.html">XMPP summary</a> shows JEP-0045 for Multi-User Chat but no RFC. And I don't see XMPP among <a href="http://www.ietf.org/html.charters/wg-dir.html">IETF Working Groups</a> any more. I wonder what's up. The <a href="http://mail.jabber.org/pipermail/xmppwg/">xmppwg mailing list archives</a> show pretty recent activity.</p>

<p>The $2.6Bn aquisition of <a href="http://en.wikipedia.org/wiki/Skype">skype</a> by Ebay shows the value of networks of
IM and voice users. Skype has a novel topology based on the same p2p
designers that did Kazaa. As I understand it, they mostly use the p2p
network for <strong>firewall traversal, which is the biggest
problem</strong>, in practice, with deploying consumer voice
chat. They keep the protocol details to themselves, though, and they
have the only implementation, as a consequence. They have a
centralized user directory too.</p>

<p>In <a href="http://www.w3.org/2005/03dc-msp/trip.html">my visit to
the 62nd IETF in Minneapolis, MN</a>, I learned what a sore spot
firewall traversal is in Internet standardization. "Just use IPV6 and
don't waste your time with those kludges" goes the one side; "but NAT
works today" goes the other. Ugh. And since <a
href="http://www.w3.org/News/2005#x20050420a">W3C started working more
actively with developing countries</a>, I hear more about the
political aspects of IPV6. In the 1st world, we can dismiss claims
that IPV4 addresses are running out as technically overblown, since we
can afford to pay for the management fees and the NAT boxes. But the
scarcity is a real economic issue in the developing world; plus it
concentrates power in a way that engenders distrust.</p>

<p>Back to network topologies... the fact that Jabber has the same
topology as conventional (SMTP) email means that it's subject to the
same sorts of spam issues. I wonder if anybody has considered the <a
href="http://www.im2000.org/">IM2000</a> approach of redesigning the
mail system as a pull delivery rather than as a push delivery system,
so that recipients no longer bear the costs of receiving and storing
unwanted messages. In an IM2000 world, senders have to <em>hold
still</em> long enough to deliver a message, which makes it much
easier to hold them accountable for nastiness.</p>