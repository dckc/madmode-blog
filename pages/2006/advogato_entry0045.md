title: 14 Aug 2006
date: 2006-08-14
tags: []
published: true

<p>I'm trying out ubuntu today. The reasons are pretty arbitrary; I sat down to work on the family finances last night, but I wasn't really in the mood, so I revisited the ubuntu installation on the <a href="http://www.advogato.org/person/connolly/diary.html?start=17">PC I built with my son</a> back in Feb 2005.

<p> <p>I like the focus on <a
href="https://help.ubuntu.com/ubuntu/desktopguide/C/common-tasks-chap.html">common
tasks</a> such as playing music, video editing, etc. And I like the fact that they invite <a href="https://launchpad.net/people/connolly">support requests</a>, not just bug reports (though launchpad is Yet Another Password that I would rather manage with OpenID). So here are the
tasks I tried:

<p> <p> <b>Reading Mail</b>

<p> <p> <p>Evolution seems to get my mail over IMAP+SSL pretty straightforwardly,
though the password prompt reminded me that I'm not sure how secure
that "remember my password" option is.

<p> <p> <b>Writing Mail</b>

<p> <p> <p>I found the "bcc me on everything I send" option easily enough; the
last thing I want the computer to do is to <a
href="http://esw.w3.org/topic/IntegrityIsJobOne">record my knowledge
and then lose it</a>, after all.

<p> <p> <p>I realized I'm addicated to tab-completion of addressees, and I
don't know where evolution stores the addressbook. The question that
remains is whether to invest in figuring out how evolution works or to
invest more in <a
href="http://www.w3.org/2000/04/maillog2rdf/email.html">my RFC822/RDF
stuff</a> and maybe set up an LDAP proxy.

<p> <p> <p>Also... how do I copy my signatures from one machine to another?

<p> <p> <p>I wonder if it's using gconf; that thing feels too much like the
windows registry for my tastes. Centralized, hard to manage and
backup.

<p> <p> <b>Chatting with colleagues via IRC</b>

<p> <p> <p>At W3C, we do a lot of teleconferences with supplemental IRC
channels. You can do a lot of work asynchronously via email
and the web, but getting together real-time once a week seems
pretty important.

<p> <p> <p>I started up xchat-gnome and I was pretty happy until I realized it
wasn't logging all the notes I was taking. (<a
href="http://esw.w3.org/topic/IntegrityIsJobOne">integrity is job
one</a>). <a
href="http://bugzilla.gnome.org/show_bug.cgi?id=333493">Automatic
logging of conversations</a> is fixed as of 2006-07-27, but the latest
release is 0.13 of July 19th, 2006, but I'm running 0.11 from
dapper. I tried to <a
href="http://xchat-gnome.navi.cx/?page_id=3">build from source</a> but
quickly found myself in automake hell ( <em>***Error***: You must have
automake &gt;= 1.9 installed</em>)

<p> <p> <p>gaim is also installed (did it come out of the box with Ubuntu? I
can't remember; it is in the list of supported apps, in any case). I
tried it a while ago but I use normal punctuation for direct address
(i.e. "joenick, what do you think?" not "joenick: what do you think?")
and gaim doesn't grok an equivalent of <strong>/set completion_char
,</strong> .

<p> <p> <p>So with an <tt>apt-get install xchat</tt>, I'm back to what
I was using under debian.

<p> <p> <b>Posting to a weblog/journal</b>

<p> <p> <p>The gnome Applications menu is not reliable enough for me to look
there first as a habit; I did a google search for blog clients; I
found gnome-blog in the <a
href="http://codex.wordpress.org/Weblog_Client">wordpress clients
list</a>. apt told me it was already installed...
oh... there it is... Applications/Internet/Blog entry poster.

<p> <p> <p>real-time spell-check... do I like that? I'm not sure.  I don't see
a way to do <a
href="http://www.w3.org/DesignIssues/Editor.html#Excerpt">excerpting</a>,
and I don't see a way to edit the source directly.  Making a link was
pretty painless; but... ew... I can't follow it, nor select the
address. <b>bzzt.</b> might as well switch to emacs and nxml-mode; I
don't know if gnome-blog knows that <a
href="http://esw.w3.org/topic/IntegrityIsJobOne">integrity is job
one</a>, after all, and I think I'm not in the mood to test it just
now.


<p> <p> <p>I guess I'm already doing email the Ubuntu way under debian. For
the other tasks, the Ubuntu way didn't meet my needs and I had to drop
back to the geek/wizard tools that I'm using under debian. My one
foray into development landed in automake hell, but I'm not going to
fault Ubunutu for that.

<p> <p> <p>I still hesitate to invest heavily in Ubuntu given things like <a
href="http://kitenet.net/~joey/blog/entry/a_bad_taste_in_the_mouth_detailed_ubuntu_patch_review.html">Joey's
ubuntu gripes</a>. I heard various bits of ubuntu/debian coordination
from <a href="http://debconf6.debconf.org/">debconf6</a>; I wonder how
many of Joey's gripes are still outstanding.
