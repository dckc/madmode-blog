module Main

thm1 : {thing: Type} -> {Man, Mortal: thing -> Type}
        -> ((x: thing) -> (Man x -> Mortal x))
        -> (socrates: thing) -> (Man socrates)
        -> (Mortal socrates)
thm1 all_men_mortal socrates socrates_a_man =
  all_men_mortal socrates socrates_a_man
