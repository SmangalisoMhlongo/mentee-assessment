# tests/test_list_utils.py
import unittest
from src.list_utils import filter_even, filter_positive

class TestListUtils(unittest.TestCase):
    def test_filter_even(self):
        self.assertEqual(filter_even([1, 2, 3, 4, 5, 6]), [2, 4, 6])

    def test_filter_positive(self):
        self.assertEqual(filter_positive([-2, -1, 0, 1, 2]), [1, 2])
