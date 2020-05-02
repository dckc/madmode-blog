||| Figure 2. Access control (A) and Capability (C) semantics
module Semantics

import Data.ZZ
import Map
import RegionCalculus
import Control.Algebra.Lattice

%default total
%access public export


||| As usual, a heap H is a map from Loc to values and
||| determines the value stored in each reference.
||| TODO: Here, values are integers and booleans.
data IsData: Value -> Type where
  IntIsData: IsData (IntVal i)
  TrueIsData: IsData True
  FalseIsData: IsData False

Heap: Type
Heap = Map Loc (v: Value ** IsData v)


data X = A | C

data ReduceExpr: X -> Region -> (Heap, Expr) -> Value -> Type where
  A_Val: (h: Heap) -> (v: Value) -> (rho: Region) -> ReduceExpr A rho (h, Lit v) v
  A_Deref: (ReduceExpr A rho (h, e) (Read r))
    -> (Just (v ** _)) = (Map.lookup r h)
    -> ReduceExpr A rho (h, Deref e) v

  C_Val: {owner: Map Loc Prin}
    -> { gteL: Prin -> Prin -> Type } -- TODO: lattice constraint?
    -> ({ defined: (Map.lookup r owner) = (Just o_r) } -> v = Write r -> (extend gteL) rho (Principal o_r))
    -> (ReduceExpr C rho (h, Lit v) (Write r))

  C_Deref: {owner: Map Loc Prin}
    -> { gteL: Prin -> Prin -> Type }
    -> (ReduceExpr C rho (h, e) (Read r))
    -> (Just (v ** _)) = (Map.lookup r h)
    -> ({ defined: (lookup r' owner) = (Just o_r') } -> (v = Write r') -> (extend gteL) rho (Principal o_r'))
    -> (ReduceExpr C rho (h, Deref e) v)


update: (Map k v) -> k -> v -> (Map k v)
update m k v = (k, v) :: m

data StepCmd: X -> Region -> (Heap, Command) -> (Heap, Command) -> Type where
  X_if: (ReduceExpr x rho (h, e) v)
    -> v = True
    -> StepCmd x rho (h, If e c1 c2) (h, c1)
  X_else: (ReduceExpr x rho (h, e) v)
    -> v = False
    -> StepCmd x rho (h, If e c1 c2) (h, c2)
  X_while_1: (ReduceExpr x rho (h, e) v)
    -> v = True
    -> StepCmd x rho (h, While e c) (h, Seq c (While e c))
  X_while_2: (ReduceExpr x rho (h, e) v)
    -> v = False
    -> StepCmd x rho (h, While e c) (h, Skip)
  A_Assign: ReduceExpr A rho (h, e1) (Write r)
    -> (Just pr) = (lookup r owner)
    -> (extend gteL) rho (Principal pr)
    -> ReduceExpr A rho (h, e2) v
    -> {isData: IsData v}
    -> StepCmd A rho (h, Assign e1 e2) (update h r (v ** isData), Skip)
  C_Assign: ReduceExpr C rho (h, e1) (Write r)
    -> ReduceExpr C rho (h, e2) v
    -> {isData: IsData v}
    -> StepCmd C rho (h, Assign e1 e2) (update h r (v ** isData), Skip)

{- TODO: Seq, Program -}

-- Local Variables:
-- idris-load-packages: ("contrib")
-- End:
