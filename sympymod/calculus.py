from IPython.display import Math, display
from sympy import diff


class PartialDerivative:

    def __init__(self, *wrt):
        self.wrt = wrt

    def __call__(self, f):
        return diff(f, *self.wrt)

    def __str__(self):
        return '\partial_{' + ''.join([str(x) for x in self.wrt]) + '}'

    def __repr__(self):
        return self.__str__()

    def _repr_latex_(self):
        return Math(str(self))

    def _ipython_display_(self, **kwargs):
        display(Math(str(self)))