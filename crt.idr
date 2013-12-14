{- Algebraic Structures I "A study of groups, rings, and fields" -}
{- Dan Connolly's notes from Fall 1987 -}

{- e.g. Chinese remainder theorem -}

-- module m373k

infixl 10 |

data (|) : Nat -> Nat -> Type where
  divides_k : {a, b, k: Nat} -> b = k * a -> a | b
