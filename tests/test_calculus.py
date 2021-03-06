import unittest

from sympy import *
from sympy.abc import *
from sympymod.calculus import *


class TestCalculus(unittest.TestCase):

    def test_partial_deriv_xy(self):

        d_xy = PartialDerivative(x, y)
        self.assertEqual(r"\partial_{xy}", str(d_xy))
        self.assertEqual(4*x*y , d_xy(x**2*y**2))

    def test_partial_integrate_with_normal_boundaries(self):

        integ = Integral(x*exp(-x), (x, a, b))
        actual = integrate_by_parts(integ, x, exp(-x))
        expected =  a*exp(-a) - b*exp(-b) + Integral(exp(-x), (x, a, b))
        self.assertEqual(expected, actual)

    def test_partial_integrate_gaussian_unevaluated_expr(self):
        Ii = Integral(t * exp(-t ** 2) / UnevaluatedExpr(t), (t, 0, oo))
        # raised and exception before fixing the issue:
        Ii.by_parts(1/t, t*exp(-t**2))

