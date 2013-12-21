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

lte_symmetric: (x: Nat) -> (LTE x x)
lte_symmetric Z = lteZero
lte_symmetric (S k) = lteSucc $ lte_symmetric k

lt_entails_lte: (x: Nat) -> (y: Nat) -> (LTE (S x) y) -> (LTE x y)
lt_entails_lte Z (S right) (lteSucc lteZero) = lteZero
lt_entails_lte (S left) (S right) (lteSucc hyp) =
  lteSucc $ lt_entails_lte left right hyp

intersection: (x -> Type) -> (x -> Type) -> (x -> Type)
intersection s t x = (s x, t x)

in_int: (s: x -> Type) -> (t: x -> Type)
        -> (s a) -> (t a)
        -> (intersection s t a)
in_int s t sa ta = (sa, ta)


total
find_min: (NS: Nat -> Type) -> (n: Nat) -> (NS n)
          -> (m ** (Minimal LT NS m))
find_min NS n ns_n = find_min' n ns_n n hyp1 where
  find_min': (found: Nat) -> (NS found) -> (pred: Nat)
             -> (Minimal LT (intersection NS (LTE pred)) found)
             -> (m ** (Minimal LT NS m))
  find_min' found NSfound (S pred) hyp = ?step
  find_min' found NSfound Z hyp = ?base_case
  hyp1: Minimal LT (intersection NS (LTE n)) n
  hyp1 = defn_minimal LT (intersection NS (LTE n)) n n_in_both noless
         where
           n_in_both = in_int NS (LTE n) ns_n (lte_symmetric n)
           noless = ?noless_pf


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
 