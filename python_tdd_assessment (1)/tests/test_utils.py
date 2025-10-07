import unittest
from utils import get_max
from utils import count_vowels

class Test(unittest.TestCase):
    def testing_max(self):
        results = get_max([9,8,6])
        self.assertEqual(results, 9)
    def testing_vowels(self):
        results = count_vowels("smanga")
        self.assertEqual(results, 2)