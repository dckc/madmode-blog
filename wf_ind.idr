-- Well-founded induction

data Minimal: (m: x) -> (x -> x -> Type) -> (x -> Type) -> Type where
  defn_minimal: (m: x) -> (R: x -> x -> Type) -> (Sub: x -> Type)
                -> Sub m -> ((s: x) -> Sub s -> Not (R s m))
                -> Minimal m R Sub
  
-- cribbed from https://en.wikipedia.org/wiki/Well-founded_relation
data WellFounded : (x: Type) -> (x -> x -> Type) -> Type where
     defn_wf : (x: Type)
               -- R is a relation on x
               -> (R: x -> x -> Type)
               -- If for every Sub, a (characteristic function of) a subset of x
               -> ((Sub: x -> Type)
                   -- if S is not empty
                   -> (notEmpty: Exists x Sub)
                   -- then it has an element that is minimal w.r.t. R
                   -> (m ** (Minimal m R Sub)) )
               -- Then R is well-founded on x
               -> WellFounded x R


-- not_lt_s_z: Not (LT s Z)
total
not_lt_s_z: (LTE (S s) Z) -> _|_
not_lt_s_z lteZero impossible
not_lt_s_z (lteSucc lr) impossible


wf_lt_nat: WellFounded Nat LT
wf_lt_nat = defn_wf Nat LT show_min where
  show_min: (Sub: Nat -> Type) -> (Exists Nat Sub) -> (m ** (Minimal m LT Sub))
  show_min Sub (Z ** z_in_Sub) = (Z ** defn_minimal Z LT Sub z_in_Sub no_less_z)
    where
      no_less_z: (s: Nat) -> Sub s -> Not (LT s Z)
      no_less_z Z ss = not_lt_s_z

{-
wf_ind: (P: Nat -> Type)
        -> ((LT y x -> P y) -> P x)
        -> ((x: Nat) -> P x)
wf_ind P hyp = ?pf
-}
