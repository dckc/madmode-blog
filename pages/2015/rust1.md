title: studying Knuth's Mastermind Solver with rust
date: 2015-05-20
tags: ['rust', 'programming', 'games', 'performance']
published: true

To celebrate rust turning 1.0, here's what I learned with [mmind5][],
a study of [Knuth's five guess algorithm for mastermind][wp5].

[wp5]: http://en.wikipedia.org/wiki/Mastermind_%28board_game%29#Five-guess_algorithm
[mmind5]: https://github.com/dckc/mmind5

While I had my share of frustration with the borrow-checker, the rust
type system is expressive enough that code is typically correct once it
compiles. I had only one bug fix in the whole project.

My first commit was *codemaker chooses a random Pattern of CodePegs*:

        #[derive_Rand]
        #[derive(Debug)]
        enum CodePeg {
          Red, Orange, Yellow,
          Green, Blue, White
        }
        
        #[derive(Debug)]
        struct Pattern {
          pegs: [CodePeg; 4]
        }
        
        impl Rand for Pattern {
            fn rand<R: Rng>(rng: &mut R) -> Self {
                Pattern {
                    pegs: [CodePeg::rand(rng),
                           CodePeg::rand(rng),
                           CodePeg::rand(rng),
                           CodePeg::rand(rng)]
                }
            }
        }

But as soon as I started working on scoring a guess vs. the code and
wanted to iterate over the pegs, my next commit was *abandon fixed
sized array in favor of vec*.

Then we get nice functional code for scoring blacks:

        let rightColorAndPlace = (0..Pattern::size()).map(|pos| {
            if g[pos] == s[pos] { Some(KeyPeg::Black) }
            else { None }
        }).collect();

White scoring is more involved; I worked it out using sloppy `println!()`
debugging. More on testing below.

As I started to study the algorithm, I changed the representation of
`Pattern` to a single `u32` representing the (lexicographic) index of
the pattern, converting to a vector of pegs as needed for scoring.
And I punted on deriving `Rand`.

The rust `std::collections::BitSet` was a good match for *... the set
S of 1296 possible codes, 1111,1112,.., 6666.*

I got the first five steps of the algorithm working on the first
night; or so I thought. On the second night, I got the final minmax
step coded up and fixed that bug in step 5 (`remove_mismatches`) and
tada!  It works.

Once I got it working, I have found any number of ways to clarify the
code by refactoring. Each time, it was a matter of making one isolated
change and letting the compiler guide me through the rest of the places
in the code that needed fixing.

For example, I had conversion from patterns to indexes and back mixed
in with scoring logic:

        let mut guesses_with_score = HashMap::new();
        for guess_ix in 0..Pattern::cardinality() {
            if !self.guessed.contains(&Pattern::ith(guess_ix)) {
                let score = guess_score(guess_ix);
                let guess = Pattern::ith(guess_ix);
                guesses_with_score.entry(score).or_insert(vec![]).push(guess)
            }
        }

I was able to factor out `PatternSet`, hiding the `BitSet` of indexes, so
the solver logic looks like:

        let mut guesses_with_score = HashMap::new();
        for guess in Pattern::range() {
            if !self.guessed.contains(&guess) {
                let score = guess_score(guess);
                guesses_with_score.entry(score).or_insert(vec![]).push(guess)
            }
        }

Implementing `Iterator` for `Solver` worked nicely, but doing `IntoIterator` for
`PatternSet` stumped me.  It's frustrating: all I wanted to do was
factor out the expression `Pattern::range().filter(|p| self.s.contains(p))`
as `into_iter` on `s`, but its type is a monster to write out and I never
did get the associated types and lifetimes figured out.

It seems to make two or three guesses per second, which seems pretty
speedy, considering it seems to be O(N^2) where N = 1296. Now that
I think about it, those were debug builds. A release build takes
a small part of a second to solve the whole thing:

    mmind$ time target/release/mmind 
    codemaker: 4112
    turn 1:    1122  BBW
    turn 2:    1223  WW
    turn 3:    4115  BBB
    turn 4:    4112  BBBB
    
    real	0m0.026s
    user	0m0.026s
    sys	0m0.000s

This is what I would see during development:

    mmind$ time target/debug/mmind
    codemaker: 1553
    turn 1:    1122  B
    turn 2:    1344  BW
    turn 3:    4524  B
    turn 4:    1336  BW
    turn 5:    1553  BBBB
    
    real	0m3.804s
    user	0m3.793s
    sys	0m0.004s

Another thing that felt slow was example documentation tests. Having
support for them is great; python doctest got me addicted to this
style. But testing them seems to rely on having the crate built;
i.e. `cargo test` isn't enough; I had to do `cargo build; cargo
test`. And to see the documentation, it becomes `cargo build; cargo
test; cargo doc`.

I'm also addicted to emacs and flycheck-mode. flycheck-rust works pretty
well but helping it find the crate root is a little fidgety.
