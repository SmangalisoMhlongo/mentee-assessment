# tests/test_string_utils.py
import unittest
from src.string_utils import format_name, title_case

class TestStringUtils(unittest.TestCase):
    def test_format_name(self):
        self.assertEqual(format_name("John", "Doe"), "Doe, John")

    def test_title_case(self):
        self.assertEqual(title_case("hello world"), "Hello World")
