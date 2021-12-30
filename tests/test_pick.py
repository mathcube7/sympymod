import unittest

from sympy import *
from sympy.abc import *
from sympymod import *


class TestPicker(unittest.TestCase):

    def test_pick_denominator(self):
        eq = Eq((x + I * y + 2 + 3 * I) / (2 * x + 2 * I * y - 3), I + 2)
        actual = pick(eq.lhs, a__/b__, b__)
        expected = (2 * x + 2 * I * y - 3)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
