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
