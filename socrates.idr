module Main

           main : IO ()
main = putStrLn "Hello world!"

thm1 : {thing: Type} -> {Man, Mortal: thing -> Type}
        -> ((x: thing) -> (Man x -> Mortal x))
        -> (socrates: thing) -> (Man socrates)
        -> (Mortal socrates)
thm1 assume_all_men_mortal assume_socrates_exists assume_socrates_man =
  assume_all_men_mortal assume_socrates_exists assume_socrates_man

