title: "Trying znc IRC bouncer to stay in touch with the ocap community"
date: 2020-01-17
tags: [collaboration, capabilities, "what-i-use", sysadmin]
published: true

I'm typically connected to IRC channels for a few ocap projects etc.:

[#erights](http://www.erights.org/)
[#genode](https://genode.org/community/index)
[#idris](https://www.idris-lang.org/)
[#indieweb](https://indieweb.org/IRC)
[#monte](http://www.monte-language.org/#IRC)
[#ocaml](https://ocaml.org/community/mailing_lists.html)
[#sandstorm](https://sandstorm.io/community)
[#swig](https://www.w3.org/2001/sw/interest/#swig_chan)

I use [hexchat](https://packages.ubuntu.com/bionic/hexchat) to connect
to these channels on [freenode](https://freenode.net/) but netsplits
and other failure modes inherent in
[IRC](https://en.wikipedia.org/wiki/Internet_Relay_Chat) make for
annoying little gaps in the connection from time to time.

An ice storm here in Kansas City gives me a chance to install the
[znc](https://packages.ubuntu.com/bionic/net/znc) IRC bouncer in my
home office, after a few months of positive experience at work.

Both `znc --makeconf` and [HexChat znc
config](https://wiki.znc.in/HexChat) want me to specify passwords,
servers, and channels.  I don't have a clear mental model of how it's
supposed to work, but I managed to muddle through, I think. _Where to
back up the config? Passwords don't fit in a dotfiles repo... ok, kbfs
+= `znc-irc-bouncer-config.tgz`, `hexchat-irc-client-config.tgz`._
