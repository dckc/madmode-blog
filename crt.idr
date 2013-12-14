{- Algebraic Structures I "A study of groups, rings, and fields" -}
{- Dan Connolly's notes from Fall 1987 -}

{- e.g. Chinese remainder theorem -}

-- module m373k

infixl 10 |

data (|) : Nat -> Nat -> Type where
  defn_divides : {a, k: Nat} -> (a | (a * k))


data GCF : Nat -> Nat -> Nat -> Type where
  defn_gcf : {a, b, d: Nat}
           -> GT d 0 -> d | a -> d | b ->
              ((c: Nat) -> c | a -> c | b -> c | d) -> GCF d a b

data Equiv : Type -> Type -> Type where
  Equiv_intro: {p, q: Type} -> (p -> q) -> (q -> p) -> Equiv p q


total
divmod: (a: Nat) -> (b: Nat)
         -> (b = a * (b `divNat` a) + (b `modNat` a))
-- TBD
-- divmod a Z = ?x_1
-- divmod a (S k) = ?x_2

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

relPrime : Nat -> Nat -> Type
relPrime a b = GCF 1 a b

lemma1: {a, b: Nat} -> GCF 1 a b -> a | (b * c) -> a | c

lemma1a: {a, b, c: Nat} -> a | b -> a | c -> a | (b + c)

lemma1b: {a, b: Nat} -> a | b -> ((x: Nat) -> a | (b * x))

data Prime: Nat -> Type where
  defn_prime: {x, p: Nat} -> (x | p -> Either (x = 1) (x = p))
              -> Prime p

thmPrimeDivisors: {a, b, p: Nat} -> Prime p -> p | (a * b)
 -> Either (p|a) (p|b)


data EqvMod : Nat -> Nat -> Nat -> Type where
  defn_eqvMod : (a: Nat) -> (b: Nat) -> (n: Nat)
                -> n | (a - b) -> EqvMod a b n

sigma: (a -> Nat) -> List a -> Nat
sigma f xs = foldr plus Z (map f xs)

expansion: List (Nat, Nat) -> Nat
expansion xes = sigma x_to_e xes
                where
                  x_to_e (x, e) = power x e

data PrimeFactorization : Nat -> List (Nat, Nat) -> Type where
  defn_pf: (xes: List (Nat, Nat)) -> (so $ sorted xes)
           -> ((x: Nat) -> so (elem x (map fst xes)) -> (Prime x))
           -> (PrimeFactorization (expansion xes) xes)

-- Unique  Factorization Theorem
