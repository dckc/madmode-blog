title: "Capability Security Advances: seL4, sandstorm, Rserve"
date: 2014-08-13
tags: [programming, security, capabilities, python, javascript, vm, seL4, kernel]
published: true
summary: seL4 is open source, sandstorm.io is coming, and Rserve has
         an ocap mode.

They did it. It's done. General Dynamics C4 Systems and NICTA released
[seL4][] under an open source license. I've been wishing for this
since 2012, when I bookmarked the [seL4 papers][] under
[security research][2].

[seL4]: http://sel4.systems/
[2]: https://www.diigo.com/user/dckc-madmode/security%20research?sort=created
[seL4 papers]: http://www.ertos.nicta.com.au/research/sel4/

Oh for time to study all the details! The formal model of C, the translator
from C to Isabelle, and on and on.

I wonder what it would take to put node-js on seL4, with no linux
kernel in between. Then, using [secure-ecmascript and such][3], we might
have a complete capability based platform.

[3]: http://research.google.com/pubs/pub40673.html

Meanwhile, [sandstorm][] is an emerging personal clound platform with
a capability security architecture ([cap'n proto][capnproto] etc.). I
pitched in to the kickstarter campaign because I really want to use it
but I doubt I'll find time to host it myself.

[sandstorm]: https://sandstorm.io/
[capnproto]: http://kentonv.github.io/capnproto/

But what really surprised me was that while wrestling with some python/R
foreign function interface issues, I discovered this bit of [rserve news][v1_7]:

> ## Additions in version 1.7
> ... Another major change is the new, optional object capability mode
> in which all commands are disabled except for CMD_OCcall. In this
> mode the server does not send an ID string, but instead sends a
> regular QAP1 message with CMD_OCinit. This message is guaranteed to
> have at least 16 bytes of payload so it will satisfy the read for an
> ID string. The command has been chosen to correspond to "RsOC" (in
> little-endian) as to identify this mode. The payload is DT_SEXP
> which holds all initial capabilities that can be used in
> CMD_OCcall. Each CMD_OCcall is DT_SEXP encoding a call (i.e.,
> LANGSXP) with an OCref object in place of the closure. Rserve will
> de-reference it before calling eval. The main purpose of this mode
> is to create a basis for a secure interface where arbitrary
> evaluation is not possible. Only code exposed by capabilities can be
> executed.

The [rcloud move to Rserve OCAP mode][73] seems to be done.  I filed a
[wish for support in pyRserve][5].

[73]: https://github.com/att/rcloud/issues/73
[v1_7]: http://rforge.net/Rserve/dev.html
[5]: https://github.com/ralhei/pyRserve/issues/5
