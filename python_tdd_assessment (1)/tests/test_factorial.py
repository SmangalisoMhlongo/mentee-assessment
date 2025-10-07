# tests/test_factorial.py
import unittest
from src.factorial import factorial

class TestFactorial(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(factorial(5), 120)

    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)
