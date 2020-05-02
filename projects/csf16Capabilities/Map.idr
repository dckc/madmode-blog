module Map

import Data.List

%default total
%access public export

Map: Type -> Type -> Type
Map k v = List (k, v)

lookup: DecEq k => (key: k) -> (m: Map k v) -> Maybe v
lookup key [] = Nothing
lookup key ((k0, v0) :: m') with (decEq key k0)
 | Yes _ = Just v0
 | No _ = lookup key m'
 
