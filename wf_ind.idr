-- Well-founded induction

{- Adapted from Coq's Init/Wf.v. LGPL -}
data Acc: (A: Type) -> (R: A -> A -> Type) -> A -> Type where
  Acc_intro : (A: Type) -> (R: A -> A -> Type) -> (x: A)
              -> ((y: A) -> R y x -> Acc A R y) -> Acc A R x

WellFounded: (A: Type) -> (R: A -> A -> Type) -> Type
WellFounded A R = (x: A) -> Acc A R x

Acc_inv: (A: Type) -> (R: A -> A -> Type)
         -> (x:A) -> (Acc A R x) -> ((y:A) -> (R y x) -> Acc A R y)
Acc_inv A R x (Acc_intro A R x ally) = ally

well_founded_induction_type : (A: Type) -> (R: A -> A -> Type) -> (P:A -> Type)
                              -> ((x:A) -> ((y:A) -> R y x -> P y) -> P x)
                              -> ((a:A) -> P a)
well_founded_induction_type A R P f a = ?well_founded_induction_type_rhs
