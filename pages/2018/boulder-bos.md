title: Smart Contracts for Health Research Data Sharing
tags: [capabilities, smart-contracts, travel, presentation, BOS, Boulder, health, data, research, rchain, Agoric]
date: 2018-07-12
published: true

I'm under contract with RChain, two days a week from June to December,
to work on [smart contracts for health research data
sharing][788]. I'm still at KUMC for the other three days a week.

[788]: https://github.com/rchain/bounties/issues/788

## RChain Devcon Boulder

In April, I was invited to [RChain Devcon][R2] in Boulder. I enjoyed
Greg's [RChain VM talk][lgm]. (_More on that later, I hope._) Vlad's
CBC Casper talk was mostly familiar; I think I got most of it from
[his devcon three talk][vz], which was just my speed.

I gave a short talk about [Getting Involved in the RChain Bounty
Program][rb] ([video][rbv]).

TimBL had written [The web is under threat][tbl], which I used as a
springboard for [Can RChain Answer?][dc] ([video][dcv]). My summary
slide is:

> It has a lot of the right pieces:
>
> - Object Capability Discipline
> - Support for Formal Verification
> - Integrated Economics with Network Architecture
> - Scalability
>     - Down to transistors
>     - Up to the globe
> - Visionary Leadership
> - Cooperative Governance

I did a quick run up of capabilities from simple closure-based objects
to sealing and unsealing to capability-based money as in [Miller,
Morningstar, and Franz][MF] from FC 2000, including:

> Before presenting the following simple example of capability-based
> money, we must attempt to head off a confusion this example
> repeatedly causes. **We are not proposing to actually do money this
> way!** A desirable money system must also provide for: ... blinding,
> non-repudiation, accounting controls, and backing (redeemability).

Then—tada!—I showed that **RChain _does_ propose to do money this
way** by translating the E code to [MakeMint.rho][]:

```{rholang}
   contract MakeMint(return) = {
     new pairCh, thisMint, internalMakePurse in {
       MakeBrandPair!(*pairCh) | for(@p <- pairCh) {
       ...
```

[R2]: https://developer.rchain.coop/conference
[lgm]: https://www.youtube.com/watch?v=3R3IL1bGm0s&t=617s
[vz]: https://www.youtube.com/watch?v=z3sY8zZRPtw
[rb]: https://docs.google.com/presentation/d/1B2Vu8o3ACwruY6HY1ayXRQ4qkNKsMy4hdbOdxrCHI2o/edit
[rbv]: https://www.youtube.com/watch?v=HsQTDNEIbjs&t=1s
[tbl]: https://webfoundation.org/2018/03/web-birthday-29/
[dc]: https://docs.google.com/presentation/d/1GOboFZj311rfGExrtCFp3aaQ2vYhxHqX3qnix21nqo4/edit
[dcv]: https://www.youtube.com/watch?v=ZnBbi6ifzdo&t=849s
[MF]: http://erights.org/elib/capability/ode/index.html
[MakeMint.rho]: https://github.com/rchain/rchain/blob/master/casper/src/main/rholang/MakeMint.rho


## HERON Clinical Data Repository Access Policy

The main smart contract I want to work on is an evolution of the
[HERON policy enforcement layer][ha], a bunch of python / PHP / SQL
code that enforces the policy around access to KUMC's clinical data
repository on ~500K patients: you have to be qualified faculty or
sponsored by one, and your human subjects training has to be current
and you have to sign a couple forms:

![flow of authority](https://informatics.kumc.edu/work/graphviz/a02d7fe066856aadf1894e50f41f4b2aa27ca3b4.dot.png)

Once you get through all that, you can use the i2b2 ad-hoc query
interface to do "cohort discovery"; for example, to find out if enough
of the right kind of patients come through KU Med for the study you
want to do.

[ha]: https://informatics.kumc.edu/work/wiki/HeronAdminDev


## i2b2 Harvard Symposium

The [i2b2 tranSMART Foundation Harvard Symposium][i2] was this year's
annual meeting of the i2b2 user community. Automation of regulatory
processes is a regular topic and this year [John Halamka][JH] spoke on
_Emerging Models of Data Flow - APIs, Blockchain and Cloud_.  He cut
through a lot of the mystery around blockchain technology with a great
illustration of one-way hashing. :)

<img
src="https://lh3.googleusercontent.com/6w32pE2Tpc6ZHzHSWKR-TmNvIvL1Nl_21z3UAYFdCukNr-MJcDlPpVTy1HRnTOcrVD2jTt59TQeaD4WEmcftD8PtxAQWeA-OIlRJ8mageizVjdaTUCCL2ENSjmHulogCqPtwcYeQ-Q=w640-h480"
width="640" height="480" />

[i2]: http://transmartfoundation.org/harvard-symposium-2018/
[JH]: http://geekdoctor.blogspot.com/


## Decentralized identity, verifiable claims

While killing time in the airport, I managed to reach Manu Sporny. His
work around [verifyable prescriptions][vp] has certain parallels with
research data sharing. It wasn't all good news, but he did put me in
touch with a couple of his colleagues in the Boston area.

I had hoped to meet with [Chris Webber](https://dustycloud.org/) and
sync up on js libraries for [linked data
capabilities](https://w3c-ccg.github.io/ocap-ld/). Capability security
seems necessary and sufficient, to me, for decentralized access
control. As Stiegler put it in the [picture
book](http://erights.org/talks/efun/SecurityPictureBook.pdf):

> The patterns described in this picturebook are simple because they
> discard the modern fascination with the identities of the
> participants. Individual Authentication is so pervasive, it is now a
> part of the problem.
>
> Suppose that your car, instead of accepting a delegatable key,
> demanded that your driver’s license match the car’s title registry,
> which happens to be in your spouse’s name. Entrepreneurs would leap
> forward to develop ever more powerful "identity management" for
> automobiles. We would subcontract to security experts so our
> teenage daughters could borrow the car to buy milk. Heaven forfend
> that the daughter, breaking her leg, had to delegate to her best
> friend to get to the hospital.

Unfortunately, while Chris is closer to Boston these days, he's still a couple hours away.

But I did get to meet [Dmitri Zagidulin][DZ] over breakfast. He has
done javascript work both with TimBL and company on
[solid](https://github.com/solid/solid) and with Manu on decentralized
identifiers
(e.g. [did-io](https://github.com/digitalbazaar/did-io)). He isn't yet
working on linked data capabilities yet, so I twisted his arm in that
direction, and [away from
WebID](http://www.madmode.com/2011/07/secure-mashups-csrf-resistent.html).

Things started to click for him when I talked about verifyable claims
in terms of insurance and markets:

> Proof of identity, in so much as it involves revelation of the
> profile, or enables its revelation through the use of unique
> identifiers, is trade in an asset when the information revealed is
> more than the minimum required with current technology. -- [Vora
> et. al from HP at W3C 2001 DRM
> Workshop](https://www.w3.org/2000/12/drm-ws/pp/hp-poorvi2.html)

Take proof of age, for example. A smart contract for a client might
ask "who will bet me $10 at 50-to-1 that this request comes from
someone over 21 years of age?" A business where people are routinely
physically present is in a position to take such bets with high
confidence.

[DZ]: http://computingjoy.com/
[vp]: https://veres.io/use-cases/verifiable-prescriptions/


## Personal Health Records

Manu also put me in touch with [Adrian
Gropper](http://healthurl.com/www/Blogs_+.html), CTO of Patient
Privacy Rights. Meeting in the airport as he was arriving and I was
departing was a bit hectic, so I couldn't be sure whether I had read
the paper he and Mark Miller worked:

 - [Identity Hubs Capabilities Perspective][rwot] Rebooting the Web of
   Trust V, October 13, 2017 by Adrian Gropper, Drummond Reed, Mark
   S. Miller

His description of [HIEofone](http://hieofone.org/) increased the
priority of UMA in my things-to-study-in-more-depth list:

> HIE of One (Health Information Exchange of One) is a
> volunteer-driven open source project to combine emerging standards
> for access authorization (OpenID HEART) and emerging standards for
> blockchain-based self-sovereign identity (DID) into a
> patient-centered health record infrastructure.

He was one of several people on this trip that talked about FHIR
deployment in ways that make me want to look into it again. In
particular, he mentioned a FHIR sandbox by CMS, the medicare folks.

[rwot]: https://github.com/WebOfTrustInfo/rebooting-the-web-of-trust-fall2017/blob/master/final-documents/identity-hubs-capabilities-perspective.md

## OCap-safe JavaScript

On the way home, I got stuck in the Washington D.C. airport overnight
due to weather. I used the time to start
[tinyses2rho](https://github.com/dckc/tinyses2rho/), some exploratory
scala code to integrate TinySES with RChain.

TinySES is a small subset of JavaScript designed so that non-experts
can use to write non-trivial non-exploitable smart contracts. It comes
from Mark Miller and company, who have been working on object
capabilities and smart contracts at least as far back as the early
'90s, and recently [launched
Agoric](https://www.coindesk.com/new-startup-zooko-naval-betting-better-crypto-contracts/).

<a href='https://photos.google.com/share/AF1QipPEmCV0T84sLHj1L1zNUQ-eldo2SVxeNYYf49RhnQF-5kp6kHZua4BAbfgCDOrICw?key=cmVENTBqc2YwY2g2QzZxQkJjSUVvVXFYYXg3QTVB&source=ctrlq.org'><img alt='DCA in the wee hours' src='https://lh3.googleusercontent.com/rv9s-h-_E58jZftv4H1XcBlgGtx1hszNMMpXrQyMVDGuath90K8OtXn7_ItZxR0G6n-_1dEVujUf0ED_nKtPq8qZElbDRsAY7PkWvKyOGejZgAZVU6HLKmQ3cKOdF0Rf-gCrh0zM8w=w2400' /></a>
