import unittest

from sympy.abc import *
from sympy import *
from sympymod import *


class TestPicker(unittest.TestCase):

    def test_pick_denominator(self):
        eq = Eq((x + I * y + 2 + 3 * I) / (2 * x + 2 * I * y - 3), I + 2)
        actual = select_by_pattern(eq.lhs, a__ / b__, b__)
        expected = (2 * x + 2 * I * y - 3)
        self.assertEqual(expected, actual)

    def test_select_atoms(self):
        expr = 3*x + 5*Integral(x**2, x) / 2
        actual = select_atoms(expr, Integral)[0]
        self.assertEqual(Integral(x**2, x), actual)


if __name__ == '__main__':
    unittest.main()
