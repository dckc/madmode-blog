title: One-click dialing back in action
date: 2005-09-12
tags: ['UriSchemes', 'sysadmin', 'hCard']
published: true

<b class="title">One-click dialing back in action</b>

<p> Aha! <a href="http://guilds.net/resume">Ted</a> and <a href="http://people.w3.org/~dom/">Dom</a> showed me how to add a tel: URI scheme handler to firefox. It turns out that firefox consults the gnome configuration database, so this works:

<p> <tt>$ gconftool-2 -t string -s /desktop/gnome/url-handlers/tel/command "echo %s"</tt>

<p> In place of echo, I use a little script that Ted wrote that uses curl to drive <a href="https://secure.click2callu.com/">Vonage Third Party Call Control</a>. This works great with the <a href="http://www.advogato.org/person/connolly/diary.html?start=2">hack</a> to build an hCard version of my sidekick contacts!

<p> tags: <a href="http://esw.w3.org/topic/UriSchemes" rel="tag">UriSchemes</a>, <a rel="tag" href="http://del.icio.us/connolly/sysadmin">sysadmin</a>,
<a rel="tag" href="http://developers.technorati.com/wiki/hCard">hCard</a>.
