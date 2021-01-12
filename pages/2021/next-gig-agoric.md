title: "What's Next: Agoric Computing"
date: 2021-01-11
tags: ["capabilities", "economics", "programming", "security"]
published: true
summary: After 15 years at W3C and 10 years at KUMC, my next gig is at Agoric.

After 15 years at W3C and 10 years at KU Med Center, my next gig is at
[Agoric](https://agoric.com/). Here I answer some questions, some
recently asked and some anticipated.

Q: I see a [NY Times feature][NYT] about Tim Berners Lee and his new
company, Inrupt. Did you work with Tim Berners-Lee?  
A: yes, from the early 1990s to 2010 we worked together building the Web at W3C.

[NYT]: https://www.nytimes.com/2021/01/10/technology/tim-berners-lee-privacy-internet.html

Q: Are you working with Tim at Inrupt?  
A: No, but I am starting a new job at Agoric.

Q: What is Agoric? What do they do?  
A: Agoric provides a safer, simpler way to program smart contracts. We
believe smart contracts enable the future of global economic
cooperation.

Q: Why is it called "Agoric"?  
A: _Agoric_ stems from _agora_, the Greek term for a meeting and
market place. An agoric system is a software system using market
mechanisms. ([Miller and Drexler, 1988][MD88])

[MD88]: https://agoric.com/papers/markets-and-computation-agoric-open-systems/abstract/

Q: Smart contracts? What's that?  
A: If you've used amazon, ebay, or a vending machine,
you've used a smart contract: a contract-like arrangement expressed in
software, where the behavior of the software enforces the terms of the
contract.

At W3C, a big part of my job was developing the W3C standards process
and figuring out how much of it could and should automate; looking
back, I think of it as smart contract design.

Q: Are these smart contracts for blockchains and cryptocurrencies like Bitcoin and Ethereum?  
A: Yes, Agoric plans to build on the high-integrity shared compute
infrastructure provided by blockchains, though the architecture
scales down to private clusters and single machines as well. ([Miller, 2019][])

[Miller, 2019]: https://www.youtube.com/watch?v=iyuo0ymTt4g&list=PLhuBigpl7lqth_Ow_eQWZs7NFxmeDw9W8

Agoric is not building on Bitcoin or Ethereum directly, but we are
building on the mature Cosmos SDK. In order to bridge to Ethereum and
Bitcoin, Agoric is a leading contributor to
[IBC](https://cosmos.network/ibc), the Inter-Blockchain Communication
protocol.

Q: How are smart contracts safer using Agoric's technology?  
A: At least three ways:

  1. Agoric provides **offer safety**: when you place an
     offer, either you'll get what you wanted or you get a refund,
     regardless of the (mis)behavior of the underlying smart contract.
     This API (Zoe) is built using a couple of more fundamental mechanisms:
  2. Agoric supports patterns of cooperation without vulnerability using
     **object capabilities** (OCaps).
  3. Agoric avoids reentrancy hazards (such as the $50M DAO bug) using
     asynchronous **eventual-sends**.

Q: Do developers have to learn a new programming language to get all this?  
A: No; Agoric smart contracts are written in a [secure subset of
JavaScript](https://github.com/Agoric/Jessie#subsetting-ecmascript)
that mostly involves sticking to established best practices.

Q: Object capabilities? What's that?  
A: Capability-based security is like the way we control access to our
cars: I use a key to drive my car. I can delegate driving the car
to you by handing you the key. But keys are impractical to forge,
so effectively, unauthorized people can't drive it.

In contrast, the traditional way to control access to computing
resources is with access control lists (ACLs): each file or database
table has a list of who can read and write it. If cars worked this
way, the car would let me drive it only if I present the right
driver's license; perhaps my wife would be on the list too. But if I
wanted to delegate to you, I'd have to update the list of drivers in
the car. And what if my son got hurt and I wasn't around to update the
list of drivers so his friend could get him to the doctor? ([Stiegler,
2004][])

[Stiegler, 2004]: http://erights.org/talks/efun/SecurityPictureBook.pdf

Valet parking would be pretty tedious. And the trunk would have to
have a separate access control list to do what valet keys do.

Worse: what we normally do when we run programs on our computers is
like giving my driver's license to you or the valet to let you drive
the car. I have to run the risk that you'll do other things with the
driver's license like open a bank account in my name. Maybe I trust
you not to do that, but every program on my computer can do anything I
can do, including mess up all my files and demand a ransom to get them
back. And with our computers connected to millions of other computers
via the Internet, we're vulnerable to more than just our friends.
With capabilities, making things like valet keys is easy so that each
program, and each part of a program, gets access to only what it needs
in order to do its job; capabilities support the **principle of least
authority** much better than access control lists. ([Close, 2009][])

[Close, 2009]: https://www.hpl.hp.com/techreports/2009/HPL-2009-20.html

I have been excited about capability-based security since 2001 when I
discovered OCaps and composable smart contracts([Miller, Morningstar,
Frantz, 2000][]). Since 2010 I have been responsible for the security
of a million or so health records in a clinical data research
warehouse at KU Med Center. Being constrained to use ACL-based
filesystems, databases, and web applictions drives me crazy!  The
chance to work on smart contracts with OCaps as a day job is a dream
come true.

[Miller, Morningstar, Frantz, 2000]: http://erights.org/elib/capability/ode/index.html

Q: And Berners-Lee's Inrupt? What do they do?  
A: Inrupt "aims to reset the balance of power on the web" by giving
users control of their data in "pods," personal online data
stores. "Each person could control his or her own data — websites
visited, credit card purchases, workout routines, music streamed — in
an individual data safe, typically a sliver of server space" ([NY
Times Jan 10][NYT]). It uses SOLID, a set of open technologies.

Q: What do you think of Inrupt and SOLID?  
A: I certainly agree when Tim says that "too much power and too much
personal data reside with the tech giants like Google and
Facebook". But

  1. SOLID Web Access Control
     ([WAC](https://github.com/solid/web-access-control-spec/))
     uses ACLs, not capabilities.
  2. I don't see an integrated economic model in SOLID.

To free users from Google, we have to provide the same sub-second
search for all of their email, and I don't see how to do that without
bringing the application code to where the data is.  We're going to
want mash-ups of multiple applications.  We need the kind of
cooperation without vulnerability that only capability-based security
brings. I wonder what would happen if we mixed the Agoric platform's
ability to scale down to clusters and single machines with the notion
of a SOLID pod.

In 2005, I learned that Internet pioneer Dave Clark took a year off to
study economics. Since then it has been pretty clear to me that
whatever comes next in the architecture of the Internet and the Web,
economics needs to be an integral part of the protocols. Bitcoin came
along in 2008 and Ethereum in 2014. Mixing in economics increases the
motivation for fraud, which has made me hesitant to commit to the
cryptocurrency industry as a career. But the Agoric platform provides
an increasing level of safety and most of the team has been working on
smart contracts with capability security as long as I've been working
on the Web, so I just can't pass up the opportunity to join them as
they scale it up to global economic cooperation.
