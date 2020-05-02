---
title: "Rosetta Stone: Taking propositions-as-types to the next level"
date: 2020-05-02
tags: ["logic", "fp", "programming", "idris", "rchain"]
published: true
---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">I read CS papers by turning notation into (<a href="https://twitter.com/idrislang?ref_src=twsrc%5Etfw">@idrislang</a>) code. Slow going, but the only way I really grok. e.g. <a href="https://t.co/8Y34KMgiXd">https://t.co/8Y34KMgiXd</a> more: <a href="https://t.co/AecWRmyFJG">https://t.co/AecWRmyFJG</a></p>&mdash; Dan Connolly (@dckc) <a href="https://twitter.com/dckc/status/1230157668888780800?ref_src=twsrc%5Etfw">February 19, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

The [Rosetta Stone](https://arxiv.org/abs/0903.0340) paper by Baez and
Stay has been on my to-read list since a conversation with Stay on a
bus a few years ago. The scope is a bit intimidating:

<table>
<tr>
  <th>Category Theory</th> <th>Physics</th> <th>Topology</th> <th>Logic</th> <th>Computation</th>
</tr>
<tr>
  <td>object</td> <td>system</td> <td>manifold</td> <td>proposition</td> <td>data type</td>
<tr>
 <td>morphism</td> <td>process</td> <td>cobordism</td> <td>proof</td> <td>program</td>
</tr>
<caption>Table 1: The Rosetta Stone (pocket version)</caption>
</table>

But in [Fun with
Categories](https://blog.statebox.org/fun-with-categories-70c64649b8e0),
the Statebox folks laid the groundwork for grokking category theory
with idris in their [idris-ct][]
library.

[idris-ct]: https://github.com/statebox/idris-ct

And the RChain community includes a
[#computational-calculi](https://discordapp.com/channels/257555930173014017/548583847235682304)
channel where people get together to study such things... I get to
fill in gaps from skipping grad school without all the tuition and
tests :). Jake and several other people there immediately agreed when
I suggested we read this paper together.  Jake dug up [Mike Stay's
slides](http://math.ucr.edu/~mike/rosettaslides.pdf) and
[notes](http://math.ucr.edu/~mike/rosetta%20slides.txt) and it took
just a little work to get the details into [the calendar][rccal].
Jake connected us to the statebox folks via a [Category
Theory](https://categorytheory.zulipchat.com/) chat group started by
Christian W.

[rccal]: https://calendar.google.com/calendar/embed?src=2cj152c9nidh6glpr1d5g4eq28%40group.calendar.google.com


## Quantum Physics Gap

Of the five domains in the Rosetta Stone, Quantum Physics is
definitely the most indimidating, to me.  [The Quantum Physics
Sequence](https://www.lesswrong.com/posts/hc9Eg6erp6hk9bWhn/the-quantum-physics-sequence)
by Yudkowsky in 2008 is the closest thing I have found so far to
something my speed, but I think I made it only 1/3rd of the way thru.

I had to look up [Hilbert
space](https://en.wikipedia.org/wiki/Hilbert_space); fortunately my
linear algebra and topology is fresh enough that "a real or complex
inner product space that is also a complete metric space with respect
to the distance function induced by the inner product" only took a few
minutes to grok.

I just watched [a lecture by Edward Witten about knots and
QM](https://youtu.be/cuJY14BYac4), a recommended Tomaslov passed along
from Greg. Quantifier noted _A Quantum Mechanics Primer_ by
D.T.Gillespie as highly regarded.  Jake sai Baez has a [good list of
recommend resources](http://math.ucr.edu/home/baez/books.html).

Fab from Statebox recommended [Picturing Quantum
Processes](https://www.amazon.com/Picturing-Quantum-Processes-Diagrammatic-Reasoning-ebook/dp/B06XB1K71P). Here's hoping...


## Intro to Idris

I gave an intro to idris this week:

> [Idris][] is a programming language designed to encourage _Type-Driven Development_.

> In type-driven development, types are tools for constructing
> programs. We treat the type as the plan for a program, and use the
> compiler and type checker as our assistant, guiding us to a complete
> program that satisfies the type. The more expressive the type is
> that we give up front, the more confidence we can have that the
> resulting program will be correct.

> In Idris, types are first-class constructs in the langauge. This
> means types can be passed as arguments to functions, and returned
> from functions just like any other value ...

[Idris]: https://www.idris-lang.org/

We have a [recording](https://youtu.be/IXqTq839pIo), though it was a
pretty informal session.


### Installing Idris

Idris docs recommend `cabal install idris` but that's a pain;
[nix support for idris](https://nixos.org/nixpkgs/manual/#idris)
reduces installation (and use!) to just[^1]:

```bash
$ nix-shell -p 'idrisPackages.with-packages (with idrisPackages; [ contrib pruviloj ])'
```

I like to combine it with [direnv](https://direnv.net/) support for nix
so that when I `cd` into an idris project directory, it all Just Works.

[^1]: if you get `idris-modules/build-builtin-package.nix:23 is marked
    as broken, refusing to evaluate`, your nix installation may be out
    of date; `nix update-nix` worked for me.

There seems to be good [vs-code support for
idris](https://github.com/zjhmale/vscode-idris), but I don't know how
to get it to look at the `contrib` package, so for today, I tried
emacs, though even that showed some rough edges.


### Formalizing Knowledge with Idris

LaTeX is fine for _typesetting_ knowledge, but my goal is to
_formalize_ knowledge such that the machine can help exploit it.

The example I gave in my [Feb 29
tweet](https://twitter.com/dckc/status/1230157668888780800?ref_src=twsrc%5Etfw)
was a [2016 paper on capabilities and confused deputy
attacks](https://www-sop.inria.fr/lemme/Tamara.Rezk/publication/csf16Capabilities.pdf).

The first definitions I captured were:

> We assume two countable sets, $Loc$ of mutable references and $Prin$ of
> principals. ...
> Values consist of integers ($n$), booleans ($tt$, $ff$) and pointers or
> mutable references $R_r$ and $W_r$.

In idris, this takes the somewhat familiar of a haskell / ML data type:

```idris
data Loc = MkLoc Nat
data Prin = MkPrin Nat

data Value =
    IntVal ZZ
  | True
  | False
  | Read Loc
  | Write Loc
```

This allows the idris compiler to, for example, let me know when I neglected to
handle all kinds of `Value` later in my transcription to code.


## Extending idris-ct for the Rosetta Stone

On page 5 of the Rosetta Stone paper we find this nice diagram
relating definitions in category theory:

<img src="/static/img/rosetta-fig-p5.svg" />

[idris-ct][] already formalizes monoidal categories and symmetric
monoidal categories but not closed categories and cartesian
categories. Jake started laying the ground work for
[CartesianCategory.idr](https://gitlab.com/jake.gillberg/programmingcats/-/blob/master/src/ProgrammingCats/MonoidalCategory/CartesianCategory.idr)
and such.

In discussion of cup and cap, Fabrizio answered a question by way of a
figure from some of his [work on petri
nets](https://arxiv.org/abs/1805.05988). He also mentioned
Samson Abramsky's work; 
[Computational interpretations of linear logic][SA93] has been on
my list since Greg said it "changed the direction of his career."
Here's hoping for time to study that one closely too.

[SA93]: https://www.sciencedirect.com/science/article/pii/030439759390181R
