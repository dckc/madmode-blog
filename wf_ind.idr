-- Well-founded induction

{- Adapted from Coq's Init/Wf.v. LGPL -}
using (A: Type, R: A -> A -> Type)
  data Acc: {A: Type} -> (R: A -> A -> Type) -> A -> Type where
    Acc_intro : {A: Type} -> ((y: A) -> R y x -> Acc R y) -> Acc R x
  WellFounded: {A: Type} -> (R: A -> A -> Type) -> Type
  WellFounded {A=A} R = (x: A) -> Acc R x

  Acc_inv: {A: Type}
           -> (R: A -> A -> Type) -> (x:A)
           -> (Acc R x) -> ((y:A) -> (R y x) -> Acc R y)
  Acc_inv R x accx = ?Acc_inv_rhs
  
  well_founded_induction_type : {A: Type} -> {R: A -> A -> Type}
                                -> (P:A -> Type)
                                -> ((x:A) -> ((y:A) -> R y x -> P y) -> P x)
                                -> ((a:A) -> P a)
  well_founded_induction_type P f a = ?well_founded_induction_type_rhs
