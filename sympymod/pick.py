from sympy import Wild


def select_by_pattern(expr, pattern, which):
    matches = expr.match(pattern)
    if matches:
        return matches[which]
    return None


def select_atoms(expr, atom_type):
    return list(expr.atoms(atom_type))

a__ = Wild('a')
b__ = Wild('b')
c__ = Wild('c')
d__ = Wild('d')
e__ = Wild('e')
f__ = Wild('f')
g__ = Wild('g')
h__ = Wild('h')
i__ = Wild('i')
j__ = Wild('j')

