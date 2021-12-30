import unittest
from sympy import *
from sympymod.utils import *


class TestUtils(unittest.TestCase):

    def test_norm_of_vector(self):
        v = Matrix([3, 4])
        actual = norm(v)
        expected = 5
        self.assertEqual(expected, actual)

