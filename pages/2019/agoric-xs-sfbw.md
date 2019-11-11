title: "Toward secure distributed computing with Agoric at SFBW '19"
date: 2019-11-03
published: true
tags: [smart-contracts, embedded, javascript, capabilities, travel, SFO]
summary: "I have been looking for someone to reproduce my work porting
         Agoric's SwingSet secure distributed computing platform to
         the Moddable xs JavaScript engine. On my recent trip to San
         Francisco, that someone turned out to be me."

After months of indecision, I decided to go to [San Francisco
Blockchain Week][sfbw] in hopes of syncing up with the [Agoric][]
team. I'm glad I did!

<a href="https://twitter.com/agoric/status/1188952857002696704">
<img src="https://pbs.twimg.com/media/EIACUZfU4AAeYxA?format=jpg&name=small"
     alt="#Agoric Team at #CESC Day 1." />
</a>

[Agoric]: https://agoric.com/
[sfbw]: https://sfblockchainweek.io/

I have been working remotely for a few months on [SwingSet on
xs][126]:

> A key to Agoric's smart contract platform is compatibility between
> widespread understanding of best practices in JavaScript development
> with object capabilities and fail-stop deterministic
> execution. Initial development of cosmic-swingset is based on the
> popular and feature-rich node.js platform, but node.js represents an
> uncomfortably large amount of code to include in a trusted computing
> base as well as a substantial risk to deterministic execution. The
> xs engine in the Moddable SDK is designed for constrained
> microcontroller environments. It has some limitations, but the
> supported feature set seems to be an excellent match for the Agoric
> platform.

[126]: https://github.com/Agoric/SwingSet/issues/126

SwingSet has about 500 tests across 15 files. Once I got about 200 in
3 files, I started looking for someone to reproduce my work.
Switching from my linux desktop to a macbook for this trip meant I
could be that someone. In the Agoric office on Wednesday, I found out
that some of the kludges I had put in place weren't portable between
linux and macOS, so only about 170 tests are working cross-platform.
It was great to be able to chat in person with Brian and Michael about
this stuff.


## Zoe and Offer Safety

Agoric leveled up their platform this week with [Zoe][], which provides
**offer safety**: when you place an offer, either you'll get what you
wanted or you get a refund, regardless of the (mis)behavior of the
underlying smart contract.

For example, [autoswap](https://github.com/Agoric/autoswap-frontend)
is a cool service, but conventional interfaces provide little
assurance as to what is going to happen when you send it some tokens
in a transaction. In contrast, a [wallet working with
Zoe](https://github.com/Agoric/wallet-frontend) presents offers in an
intelligible form and guarantees that the offer is either executed as
stated or you get a refund.

There are some rough edges in getting these demos running, but I had
done the [testnet demo][16] the previous week so it only took me a
little chatting with JF and co to get them running.

And the Agoric folks are not alone in smoothing out the UI: Dan Finlay
built a [MetaMask Agoric
Plugin](https://github.com/danfinlay/metamask-agoric-plugin) at the
DeFi hackathon.

I think it would be fun to formally verify the offer safety property.
Mark Miller and I chatted about this with Eric McCarthy, who works on
the [ACL2
Ethereum](https://www.kestrel.edu/home/projects/ethereum/index.html)
project. I have some history with ACL2, and in some sense the untyped
style of ACL2 goes well with JavaScript, but I wonder if that's a
false economy. I'm more facile with ML style propositions-as-types
systems (idris, ocaml) lately.


[Zoe]: https://agoric.com/zoe-vs-status-quo/
[16]: https://agoric.com/testnet-pixel-demo/


## CESC: Ouroboros, Kara from Oasis Labs, ...

At CESC (crypto economics security conference) Monday and Tuesday,
some talks were too full of greek letters for me to follow and others
were more like TV commercials than academic contributions. Two that
stood were:

 - Vassilis Zikas on _The Evolution of Ouroboros: From Proof of Work
   to Proof of Stake_. He started with an introduction to bitcoin that
   seemed a little remedial for this venue but he built on the
   structure of that intro to make a clear presentation of the rest.

 - [Kara](https://kara.cloud/#/) from [Oasis
   Labs](https://www.oasislabs.com): privacy-preserving health data
   analytics. "AI for healthcare is limited by the fact, that the most
   valuable data is locked in data silos. Kara breaks up these silos
   and allow researchers to train their models on data that is
   otherwise hidden from science - extracting value from it, while
   never exposing the data itself." The talk was a little on the TV
   commercial side, but the [Ekiden](https://arxiv.org/abs/1804.05141)
   on how they mix private compute nodes with the blockchain is pretty
   convincing. The evaluation includes some machine learning stuff for
   medical diagnostics.

## Epicenter: CasperLabs, Chainlink

I went to the [CasperLabs workshop by Michael][clw] with Joshy, a
[fellow rchain expat][rex].

[clw]: https://twitter.com/meetCasperLabs/status/1190015712208666624
[rex]: https://joshyorndorff.com/blog/keeping-the-rchain-community-together

The Chainlink marketplace for connecting smart contracts to real world
data sources (oracles) and payment systems looked interesting. I'm a
little bummed I missed the [chainlink
workshop](https://docs.google.com/document/d/e/2PACX-1vTfuGrmqJO_il0PzZY5iU5_HtmiEExu5t7XHzrj6rRVKZnOdvy3fUJzlIlTgd-FMrUl2A-9T9ndP7Nj/pub),
but I think I made the right call hanging out with the Agoric team
instead.
