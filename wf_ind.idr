-- Well-founded induction

data Minimal: (x -> x -> Type) -> (x -> Type) -> x -> Type where
  defn_minimal: (R: x -> x -> Type) -> (Sub: x -> Type) -> (m: x)
                -> (Sub m)
                -> ((s: x) -> (Sub s) -> Not (R s m))
                -> Minimal R Sub m
  
{- This helped me find the structure of the proof below. -}
total
calc_min: (NS: Nat -> Bool) -> Nat -> Nat
calc_min NS n = calc_min' n n where
  calc_min': Nat -> Nat -> Nat
  calc_min' found Z = found
  calc_min' found (S pred) =
    if NS pred then calc_min' pred pred else calc_min' found pred

lt_entails_lte: (x: Nat) -> (y: Nat) -> (LTE (S x) y) -> (LTE x y)
lt_entails_lte Z (S right) (lteSucc lteZero) = lteZero
lt_entails_lte (S left) (S right) (lteSucc hyp) =
  lteSucc $ lt_entails_lte left right hyp

-- TODO: finish other cases
find_min: (NS: Nat -> Type) -> (n: Nat) -> (NS n)
          -> (m ** (Minimal LT NS m))
find_min NS n ns_n = find_min' n ns_n n hyp0 where
  find_min': (found: Nat) -> (NS found)
             -> (pred: Nat) -> ((s: Nat) -> (LTE (S pred) s)
                                -> (NS s) -> (LTE found s))
             -> (m ** (Minimal LT NS m))
  find_min' found NSfound Z hyp =
    (found ** defn_minimal LT NS found NSfound ?pf_lt_entails_lte)
  hyp0: (s: Nat) -> (LTE (S n) s) -> (NS s) -> (LTE n s)
  hyp0 s lteSns NSs = lt_entails_lte n s lteSns
    
{-
-- not_lt_s_z: Not (LT s Z)
total
not_lt_s_z: Not (LT s Z)
not_lt_s_z lteZero impossible
not_lt_s_z (lteSucc lr) impossible

-- @@ find_min_below NS ((S n) ** NS) Z lte_a_n =
--  (Z ** defn_minimal LT NS Z ns_Z none_lt_z)
  
find_min NS ((S n) ** ns_sn) acc =
  (Z ** defn_minimal LT NS Z ns_Z none_lt_z)
  where
    none_lt_z: (s: Nat) -> (NS s) -> Not (LT s Z)
    none_lt_z s ns_s = not_lt_s_z

  -- (Z ** defn_minimal Z LT NS ns_z (not_lt_s_z Z))
-}

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
                   -> (m ** (Minimal R Sub m)) )
               -- Then R is well-founded on x
               -> WellFounded x R




{- @@
wf_lt_nat: WellFounded Nat LT
wf_lt_nat = defn_wf Nat LT show_min where
  show_min: (Sub: Nat -> Type) -> (Exists Nat Sub) -> (m ** (Minimal LT Sub m))
  show_min Sub (Z ** z_in_Sub) =
    (Z ** defn_minimal Z LT Sub z_in_Sub no_less_z)
    where
      no_less_z: (s: Nat) -> Sub s -> Not (LT s Z)
      no_less_z Z ss = not_lt_s_z
  show_min Sub ((S n) ** sn_in_Sub) =
    (m ** defn_minimal m LT Sub m_in_Sub no_less_m)
    where
      no_less_m: (s: Nat) -> Sub s -> Not (LT s m)
-}


{-
wf_ind: (P: Nat -> Type)
        -> ((LT y x -> P y) -> P x)
        -> ((x: Nat) -> P x)
wf_ind P hyp = ?pf
-}
 