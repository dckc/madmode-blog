{- Algebraic Structures I "A study of groups, rings, and fields" -}
{- Dan Connolly's notes from Spring 1988 -}

{- goal: prove Chinese remainder theorem -}
{- TODO: migrate from Nat to ZZ.
   I started this with Version 0.9.10.1 of Idris, which has
   a bug in importing modules, so I restricted myself to Nat,
   which is in the Prelude. -}
{- ack: Library Coq.ZArith.Znumtheory
http://coq.inria.fr/library/Coq.ZArith.Znumtheory.html#Zis_gcd
 -}
module m373k

import Data.Vect


infixl 7 |  -- lower than *, +

  {- TODO: consider "using a: Nat, b: Nat" -}
{- how do typeclasses work here? i.e. does it matter
   whether I write * or mult? -}
data (|) : Nat -> Nat -> Type where
  defn_divides : {a, k: Nat} -> (a | a * k)

{- Coq has lots of other useful-looking stuff; e.g. divides is decideable. -}

{- this is written (a, b) in my notes, but that's taken, so... -}
data GCF : Nat -> Nat -> Nat -> Type where
  defn_gcf : {a, b, d: Nat}
           -> GT d 0  -- The Coq library doesn't include d > 0. hmm.
             -> d | a -> d | b ->
              ((c: Nat) -> c | a -> c | b -> c | d) -> GCF a b d

{- This is an unnamed Thm: in my notes,
   (half way) proved using well-ordering of N (Nat)
   but the Coq approach seems more useful. -}
data Euclid : (a: Nat) -> (b: Nat)
     -> (u: Nat) -> (v: Nat)
     -> (d: Nat) -> Type where
  Euclid_intro : {a, b, u, v, d: Nat} -> GCF a b d -> Euclid a b u v d

rel_prime: Nat -> Nat -> Type
rel_prime a b = GCF a b 1

{- This is an unnamed Lemma in my notes -}
Guass: {a, b, c: Nat} -> (a | b * c) -> rel_prime a b -> (a | c)

lemma1a: {a, b, c: Nat} -> a | b -> a | c -> a | b + c

lemma1b: {a, b: Nat} -> a | b -> ((x: Nat) -> a | b * x)

data Prime: Nat -> Type where
  {- This is prime_divisors in Coq. -}
  {- It doesn't seem to exclude 1. That can't be on purpose, can it? -} 
  defn_prime: {x, p: Nat} -> (x | p -> Either (x = 1) (x = p))
              -> Prime p

prime_mult: {a, b, p: Nat} -> Prime p -> p | a * b
 -> Either (p|a) (p|b)

{-
gcd_divides_b : (a: Nat) -> (b: Nat) -> (gcd a b) | b
gcd_divides_b Z Z = defn_divides {a=Z} {k=Z}
-- rest TBD

gcd_divides_a : (a: Nat) -> (b: Nat) -> (gcd a b) | a
gcd_divides_a Z Z = defn_divides {a=Z} {k=Z}
-- rest TBD

gcd_greatest : (a: Nat) -> (b: Nat)
               -> ((c: Nat) -> (c | a) -> (c | b) -> (c | (gcd a b)))
-- TBD

gcf_gcd : (a: Nat) -> (b: Nat) -> (GT (gcd a b) 0) -> (GCF (gcd a b) a b)
gcf_gcd  a b gt = (defn_gcf gt (gcd_divides_a a b) (gcd_divides_b a b)
                   (gcd_greatest a b))


data Equiv : Type -> Type -> Type where
  Equiv_intro: {p, q: Type} -> (p -> q) -> (q -> p) -> Equiv p q


data EqvMod : Nat -> Nat -> Nat -> Type where
  defn_eqvMod : (a: Nat) -> (b: Nat) -> (n: Nat)
                -> n | a - b -> EqvMod a b n

expansion: Vect n (Nat, Nat) -> Nat
expansion xes = sum $ map x_to_e xes
                where
                  x_to_e (x, e) = power x e

data PrimeFactorization : Nat -> Vect n (Nat, Nat) -> Type where
  defn_pf: (xes: Vect n (Nat, Nat)) -> (so $ sorted $ toList xes)
           -> (All Prime (map fst xes))
           -> (PrimeFactorization (expansion xes) xes)
-- Unique  Factorization Theorem

-}

