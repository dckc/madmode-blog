-- Well-founded induction

data Minimal: (m: x) -> (x -> x -> Type) -> (x -> Type) -> Type where
  defn_minimal: (m: x) -> (R: x -> x -> Type) -> (S: x -> Type)
                -> S m -> ((s: x) -> S s -> Not $ R s m)
                -> Minimal m R S
  
-- cribbed from https://en.wikipedia.org/wiki/Well-founded_relation
data WellFounded : (x: Type) -> (x -> x -> Type) -> Type where
     defn_wf : (x: Type)
               -- R is a relation on x
               -> (R: x -> x -> Type)
               -- If for every S, a (characteristic function of) a subset of x
               -> ((S: x -> Type)
                   -- if S is not empty
                   -> (notEmpty: Exists x S)
                   -- then it has an element that is minimal w.r.t. R
                   -> (m ** (Minimal m R S)))
               -- Then R is well-founded on x
               -> WellFounded x R

wf_lt_nat: WellFounded Nat LT

{-
wf_ind: (P: Nat -> Type)
        -> ((LT y x -> P y) -> P x)
        -> ((x: Nat) -> P x)
wf_ind P hyp = ?pf
-}
