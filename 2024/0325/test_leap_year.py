import unittest
from leap_year import is_leap_year


class TestLeapYear(unittest.TestCase):
    def test_2020(self):
        r = is_leap_year(2020)
        self.assertEqual(r, True)

    def test_2077(self):
        r = is_leap_year(2077)
        self.assertEqual(r, False)

    def test_2000(self):
        r = is_leap_year(2000)
        self.assertEqual(r, True)

    def test_1900(self):
        r = is_leap_year(1900)
        self.assertEqual(r, False)
