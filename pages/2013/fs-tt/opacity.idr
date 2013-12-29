{-
  (believes LoisLane '(capable Superman fly) )

and,

  (identical Superman ClarkKent)

we *can't* infer,

  (believes LoisLane '(capable ClarkKent fly) )

http://lists.w3.org/Archives/Public/www-rdf-logic/2001Apr/0074.html
-}


{-
 -- owl:Thing a rdfs:Class
 -- lois a owl:Thing. clark ...
 -- CanFly a rdfs:Class
 -- believes a rdf:Property
-}
props : {thing: Type}
        -> { CanFly: thing -> Type }
        -> { clark, superman: thing }
        -> (clark = superman)
        -> (CanFly superman)
        -> (CanFly clark)

quot : {thing: Type}
        -> { CanFly: thing -> Type }
        -> { believes: thing -> Type -> Type }
        -> { lois, clark, superman: thing }
        -> (believes lois (CanFly superman))
        -> (CanFly superman)


quot2 : {thing: Type}
        -> { CanFly: thing -> Type }
        -> { believes: thing -> Type -> Type }
        -> { lois, clark, superman: thing }
        -> { prop: Type } -> (believes lois prop)
        -> prop


class rdfs_Class thing where
  contains: thing -> Type

class rdf_Property domain range where
  
{-
thm2 : {thing: Type}
        -> { CanFly: thing -> Type }
        -> { believes: thing -> Type -> Type }
        -> (thing lois) -> (thing clark) -> (thing superman)
        -> (clark = superman)
        -> ((arg: ((believes lois (CanFly superman))
                   -> (believes lois (CanFly clark))))
            -> (arg: _|_))
-}
