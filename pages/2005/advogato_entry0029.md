title: 'Bugs on top of bugs on top of paperwork: frustration on so many levels'
date: 2005-07-15
tags: []
published: true

<b class="title">Bugs on top of bugs on top of paperwork: frustration on so many levels</b>

<p> So I'm trying to send an expense report.

<p> The bane of my existence is doing things that I know the computer could do for me.<a href="#ref1">*</a>

<p> Filling out shipping waybills is <em>definitely</em> one of them. I've tried the <a href="https://www.fedex.com/">fedex</a> online shipping interface, but it's pretty javascripty and klunky, and I've never made it past the form that asks for my credit card number, since my employer always pays to have these expense reports shipped.

<p> <p> <p> <p> But the last time I tried to send an expense report via fedex, I got a bill for $30 because I neglected to check exactly the right "bill to sender" box on the paper waybill. When I called fedex, they could see that I  clearly meant to bill the recipient, since I wrote the account number right there, and they fixed the billing problem. So today I'm  motivated to invest quite a bit more in getting online shipping working.

<p> <p> <p> <p> So I fill out the account application forms. One of them asks whether I want to create a new fedex account or use an existing one, but it doesn't accept the account number I have for my employer, so I create a new one, even though I don't want to. And there's this confusing stuff about a 10% discount.

<p> <p> <p> <p> I fought thru all that and got to a form that looked just like a paper waybill. Now we're getting somewhere. It has a "bill to recipient" option but when I submit the form, I get "invalid account". So I find the tech support number and get in the hold queue. While I'm waiting on hold, a friendly voice informs me that they have online chat support. I'm a pretty big fan of online chat, so I try it out.

<p> <p> <p> <p> It's java. I've had mixed luck with java applets, but thanks to <a href="http://www.debian-administration.org/articles/142">a great article on installing Sun's java on debian</a>, my Java installation is pretty shiny and I'm willing to give it a try. Just as I was starting to have a meaningful exchange with a fedex support guy, it started doing a peg-the-cpu-and-update-the-scrollbar-a-zillion-times thing. It recovered once, then did it again. I closed the window but the CPU stayed pegged. Uh-oh; I thought I'd have to restart firefox and lose days worth of state. But eventually the CPU load subsided.

<p> <p> <p> <p> Meanwhile, my turn in the hold queue came up, and in an IRC chat with our admin folks, I discover that I've been putting an extra digit in the account on my waybills. Also, I had used a "verify address" feature, which filled in the full 10 digit zip, but the account I was billing to only had the 5 digit zip. I don't know who thought that "invalid account" was a sufficient diagnostic for that failure mode. With those two problems addressed, I got as far as printing a waybill, only to see my phone number represented as (161)739-5555; their profile forms don't grok international +1-... syntax, so I had to put just the bare 10 digits in there. Finally, I got the computer to fill out the waybill for me.

<p> <p> <p> The next hurdle was getting a priceline receipt printed. 
I have a .pdf file and a .ps file (derived from the .pdf via pdf2ps, I think). If I ask cups to print the .ps file to my networked HP printer, somewhere along the line it gets scaled up 4x, and I get only the top-left quarter of the receipt filling the whole page. The pdf file looks funny in evince. I check it with acroread and it works, so I try printing it and I win. But evince is otherwise such a nice piece of software that I want to help them fix this problem.

<p> <p> <p> So I try, once again, to figure out how to report problems in debian. The gnome menus aren't much help, but it's pretty easy to find <a href="https://www.debian.org/Bugs/Reporting">How to report a bug in Debian</a> via the evince package page. I like the idea of an emacs interface, so I <tt>apt-get install debbugs-el</tt> and type <tt>M-x debian-bug</tt>. No joy. Since I haven't restarted emacs, it hasn't loaded the package. I have to find the .elc and <tt>M-x load-file</tt> it. Then it pleasantly guides me thru filling out a bug report. But I want to attach some files to the bug report, and I can't see how to do that in emacs mail mode. Oh well, I'll attach them to follow-up messages.

<p> <p> <p> Emacs reports success when I hit <tt>ctrl-c ctrl-c</tt> to send the message; but I use an ssh tunnel to send my mail, and I haven't told emacs about it. So where did that message go? It's frozen in an exim4 queue. I don't really want to manage an MTA on this machine, but lots of debian packages that I use require one. There is a "don't do anything" configuration option, and I'm pretty sure I chose that one when I installed exim4. Now I'm trying to remember how to reconfigure it. I see several references to a debconf(7) man page that I can't find. I eventually figure out the magic incantation: <tt>sudo /usr/sbin/dpkg-reconfigure  -plow exim4-config</tt>. But even after I configure it to send mail, the message stays frozen in the queue. I give up at this point and copy the contents of the message to a text file, and use <tt>EDITOR=gedit reportbug</tt>. I ask in the <tt>#debian</tt> channel about how to attach files to bug reports; somebody there confirms that attaching them to follow-up messages is a reasonable thing to do, but also suggests just composing the message that reportbug would send in my normal mailer and using it to attach them. "I don't usually bother with reportbug" he says.

<p> <p> <p> <b>argh!</b> The primary interface for reporting debian bugs is so unusable that the developers (ok, one developer) don't even use it?

<p> <p> <p> So I press on. I don't regularly use my ISP's SMTP server, but somehow reportbug knows its address and sends the bug report.

<p> <p> <p> While I'm waiting for the acknowledgement, I try to figure out the relationship between reportbug and bug-buddy. I recall that bug-buddy feeds into the upstream gnome bug system, and I have a vague recollection that debian wants you to file bugs in the debian bug tracking system, not upstream. Plus, bug-buddy doesn't seem to have an interface for attaching files either.

<p> <p> <p> Ah... the acknowledgement is here now: <a href="https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=318122">#318122</a>.


<p> @@tags: usability debian linux-printing-swamp

<p> *<a name="ref1" href="https://www.nature.com/nature/webmatters/xml/xml.html">yours truely, Oct '98</a>
<p> <p> <p> advogato <em>still</em> doesn't grok rss:title. I'm tring a class="title" microformat to that maybe I can recover/convert...
