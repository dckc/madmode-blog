from flip.logic import nd
from flip.logic.formula import (
    InfixRelation, InfixLogical, Variable, VariablePlaceholder)
from flip.logic.prop_common import And, Not, Impl, m1, m2
from flip.logic.fol import Equal, A, E, t1, t2, v1, v2, P1


def axiom(name, abbr, fmla):
    _rule_names = {abbr: name}
    _rules = {abbr: [fmla]}
    nd.add_rule_names(_rule_names)
    nd.add_rules(_rules)
    return abbr


def infer_bidir(name, abbr, p, q):
    intro = abbr + 'I'
    elim = abbr + 'E'
    _rule_names = {
        intro: name + ' (intro)',
        elim: name + ' (elim)'
    }
    _rules = {
        elim: [p, q],
        intro: [q, p]
    }
    nd.add_rule_names(_rule_names)
    nd.add_rules(_rules)
    return intro, elim


class Iff(InfixLogical):
    """
    Impl(a,b) means a <=>
    """
    def __init__(self, *args):
        InfixLogical.__init__(self, *args)
        self.symbol = '<=>'


iffI, iffE = infer_bidir('Iff', 'iff',
                         Iff(m1, m2),
                         And(Impl(m1, m2), Impl(m2, m1)))


class elt(InfixRelation):
    def __init__(self, *args):
        InfixRelation.__init__(self, *args)
        self.symbol = '.in.'


phi = Variable('phi')

emptySet = axiom('Empty Set', 'emptySet', Not(elt(t1, phi)))
# alternatively: E(x, A(y, Not(elt(y, x))))

ext = infer_bidir('Extensionality', 'ext',
                  # need a side-condition that t1 and t2 are sets?
                  Equal(t1, t2),
                  A(v1, Iff(elt(v1, t1), elt(v1, t2))))

abst = axiom('Abstraction', 'abst',
             E(v1, A(v2, Iff(elt(v2, v1), And(elt(v2, t1), P1(v2))))))
