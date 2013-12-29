parameters (thing: Type)

data Term where
  k: String -> Term -- uri ref?
  ex: String -> Term -- De Brun (sp) indexes?
  i: Int -> Term
  s: String -> Term
  b: Bool -> Term
  dt: String -> String -> Term

data DataFormula where
  atom: Term -> Term -> Term -> Type
  conj: Formula -> Formula -> Type
  -- existential binding?
  -- universal binding?

t_socrates : Term
t_socrates = k "socrates"

t_men : Term
t_men = k "men"

t_mortal : Term
t_mortal = k "mortal"

ax1 : t_men -> t_mortal
ax1 = 