import sympy


class Eq(sympy.Eq):

    @property
    def rhs(self):
        return super().rhs

    @rhs.setter
    def rhs(self, rhs):
        self._args = (self.lhs, rhs)

    @property
    def lhs(self):
        return super().lhs

    @lhs.setter
    def lhs(self, lhs):
        self._args = (lhs, self.rhs)

    def __add__(self, other):
        if isinstance(other, Eq):
            return Eq(self.lhs + other.lhs, self.rhs + other.rhs)
        return Eq(self.lhs + other, self.rhs + other)

    def __radd__(self, other):
        return Eq(self.lhs + other, self.rhs + other)

    def __sub__(self, other):
        if isinstance(other, Eq):
            return Eq(self.lhs - other.lhs, self.rhs - other.rhs)
        return Eq(self.lhs - other, self.rhs - other)

    def __rsub__(self, other):
        return Eq(self.lhs - other, self.rhs - other)

    def __mul__(self, other):
        if isinstance(other, Eq):
            return Eq(self.lhs * other.lhs, self.rhs * other.rhs)
        return Eq(self.lhs * other, self.rhs * other)

    def __rmul__(self, other):
        return Eq(other * self.lhs, other * self.rhs)

    def __truediv__(self, other):
        if isinstance(other, Eq):
            return Eq(self.lhs / other.lhs, self.rhs / other.rhs)
        return Eq(self.lhs / other, self.rhs / other)

    def __rtruediv__(self, other):
        return Eq(other / self.lhs, other / self.rhs)

    def __pow__(self, power, modulo=None):
        return Eq(self.lhs**power, self.rhs**power)

    def apply(self, side, what, *args, **kwargs):
        if side == 'lhs':
            return Eq(what(self.lhs, *args, **kwargs), self.rhs)
        elif side == 'rhs':
            return Eq(self.lhs, what(self.rhs, *args, **kwargs))
        elif side == 'both':
            return Eq(what(self.lhs, *args, **kwargs), what(self.rhs, *args, **kwargs))
        else:
            raise Exception('Unknown key word: %s' % side)

    def doit(self, **kwargs):
        return Eq(self.lhs.doit(**kwargs), self.rhs.doit(**kwargs))
