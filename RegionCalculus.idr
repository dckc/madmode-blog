||| Figure 1. Region Calculus
|||
||| "Our technical development is based on a region calculus, a simple,
||| formal imperative language with notions of principals (which own a
||| subset of references) and regions (which specify a write integrity
||| policy that we wish to enforce).
||| Our calculus has five syntactic categories — values (v ),
||| expressions (e), commands (c), regions (ρ), and top-level
||| programs or, simply, programs (P )."

module RegionCalculus

import Data.ZZ
import Decidable.Order -- TODO: Lattice
import Map

%default total
%access public export

||| We assume two countable sets, Loc of mutable references and Prin of
||| principals.  Elements of Loc are written r and elements of Prin are
||| written P.
data Loc = MkLoc Nat
data Prin = MkPrin Nat

locInjective : MkLoc n = MkLoc m -> n = m
locInjective Refl = Refl

DecEq Loc where
  decEq (MkLoc x) (MkLoc y) with (decEq x y)
    | Yes p = Yes $ cong p
    | No p = No $ \h => p $ locInjective h



||| Values consist of integers (n), booleans (tt, ff ) and pointers or
||| mutable references R r and W r
||| References R r and W r
||| represent the read and write capabilities for the reference r .
||| Capability R r can only be used to read r , whereas capability
||| W r can only be used to write r .
data Value =
    IntVal ZZ
  | True
  | False
  | Read Loc
  | Write Loc

||| Expressions e are computations that cannot update references. They
||| include values and reference reading (!e).
data Expr =
    Lit Value
  | Deref Expr

||| Commands c are standard conditionals, while loops, assignments,
||| sequencing (c 1 ; c 2 ) and skip.
data Command =
    If Expr Command Command
  | Loop Expr Command
  | Assignment Expr Expr
  | Seq Command Command
  | Skip

||| A region ρ is either a principal P or an endorsed principal, P. In
||| both cases, P represents a ceiling (maximum) authority for
||| executing code. However, in the case of an endorsed region, the
||| principal expresses the explicit willingness to act on another
||| principal’s behalf.
data Region =
    Principal Prin
  | Endorsed Prin

||| A program P is a sequence of commands, executed in possibly different
||| regions. A program has the form ρ 1 {c 1 } ◦ . . . ◦ ρ n {c n } and
||| means that first command c 1 runs in the region ρ 1 , then command c 2
||| runs in region ρ 2 and so on.  When a command runs in a region, the
||| command is subject to the ceiling authority of the region.
data Program =
    RegionCommand Region Command
  | Compose Program Program


||| Regions and write integrity
|||
||| ... we assume that each reference is owned by a principal. This is
||| formalized by an ownership map O, that maps a reference to the
||| principal that owns the reference. Formally, O : Loc →
||| Prin. Principals are assumed to be organized in a lattice L whose
||| order is written ≥ L .
data WriteIntegrity: (owner: Map Loc Prin) -> (gteL: Prin -> Prin -> Type) -> Type where
  HasWriteIntegrity: Poset Prin gteL => WriteIntegrity owner gteL

||| For convenience, we extend the order ≥ L to regions: ρ ≥ L ρ 0
||| when ρ ∈ {P, P}, ρ 0 ∈ {P 0 , P 0 } and P ≥ L P 0 .
extend: (gteL: Prin -> Prin -> Type) -> (Region -> Region -> Type)
extend gteL (Principal p) (Principal p') = gteL p p'
extend gteL (Endorsed p) (Principal p') = gteL p p'
extend gteL (Endorsed p) (Endorsed p') = gteL p p'
extend gteL (Principal p) (Endorsed p') = gteL p p'

-- Local Variables:
-- idris-load-packages: ("contrib")
-- End:
