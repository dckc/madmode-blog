---
title: Formal Verification is catching up with cutting-edge Mathematics
date: 2025-01-01
published: true
tags: [proof, logic, collaboration]
---

Formalization has trailed cutting-edge mathematics for some time:
the [four color theorem](https://en.wikipedia.org/wiki/Four_color_theorem) was proved in 1976,
but it wasn't formally verifed until 2005.

This was one of the objections of the [QED manifesto](https://en.wikipedia.org/wiki/QED_manifesto) in 1993:

> **Objection 4.** Mechanically checked formality is impossible.
> There is no evidence that extremely hard proofs can be put into formal form
> in less than some utterly ridiculous amount of work.
>
> **Reply to Objection 4.** Based upon discussions with numerous workers in automated reasoning,
> it is our view that using current proof-checking technology, we can, using a variety of systems and expert users of those systems,
> check mathematics at **within a factor of ten**, often much better, of the time it takes a skilled mathematician to write down a proof
> at the level of an advanced undergraduate textbook. (_emphasis mine_)

Today I got a github notification that prompted me check in on [recent discussion around Metamath](https://groups.google.com/g/metamath),
and I learned that one of the greatest living mathematicians is formally verifying his work as he develops it:

> ... when it comes to formalising mathematics in real time, we now have an even more spectacular data point:
> Terry Tao led a team which formalised the main result in his breakthrough new paper
>  with Gowers, Green and Manners proving Katalin Marton’s polynomial Freiman-Ruzsa conjecture.
>  The 33 page paper was formalised in **_just three weeks_** (before the paper had even been submitted)!
 -- [Lean in 2024 | Xena](https://xenaproject.wordpress.com/2024/01/20/lean-in-2024/)

My [notes](https://www.diigo.com/user/dckc-madmode?query=%23research+%23logic) show I first looked at [Lean](https://lean-lang.org/about/)
back in 2015. I'm trying to remember what I didn't like about it... ah yes... it's written in C++ and the logic is kinda hairy.

The logic does have a [kernel](https://lean-lang.org/doc/reference/latest/Elaboration-and-Compilation/#The-Lean-Language-Reference--Elaboration-and-Compilation--The-Kernel),
which was written up by someone I recognize from the Metamath community:

 - Mario Carneiro, 2019. [The Type Theory of Lean.](https://github.com/digama0/lean-type-theory/releases/download/v1.0/main.pdf)
   - [The Type Theory of Lean - YouTube](https://www.youtube.com/watch?v=3sKrSNhSxik)

In his [mm0](https://github.com/digama0/mm0) work, he calls it a "very strong axiomatic framework".

I tried to read that paper; it's a little over my head. But Lean can export proof objects and there are independent checkers.
[tc.rs](https://github.com/ammkrn/nanoda_lib/blob/master/src/tc.rs) is the core of a rust implementation;
it's over 1000 LOC; over 5000 if you count the modules it imports.
Compare with the 362 line [otter proof checker](https://lists.w3.org/Archives/Public/sw99/2000JanMar/0002.html).
The [Type Checking in Lean 4](https://ammkrn.github.io/type_checking_in_lean4/) docs are just about my speed, though. Thanks!
