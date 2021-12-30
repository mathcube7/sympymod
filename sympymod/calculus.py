from IPython.display import Math, display
from sympy import diff, limit, Mul
import sympy


class Integral(sympy.Integral):

    def by_parts(self, u, vp):
        return integrate_by_parts(self, u, vp)


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


def integrate_by_parts(integral, u, vp):
    """ Makes SymPy integrate by parts

        integral: A SymPy Integral object
        u: u(x)
        vp: derivative of v(x)
    """
    integrand, (x_, a_, b_) = integral.args
    assert integrand == u * vp
    v = Integral(vp, x_).doit()

    # If the new integrand contains a leading minus sign,
    # put it in front of the integral.
    integrand = diff(u, x_) * v
    sign = -1
    if isinstance(integrand, Mul) and integrand.args[0] == -1:
        integrand *= -1
        sign = 1

    # The limits take into account cases like oo*exp(-oo)
    return (
            limit(u * v, x_, b_) - limit(u * v, x_, a_)
            + sign * Integral(integrand, (x_, a_, b_))
    )