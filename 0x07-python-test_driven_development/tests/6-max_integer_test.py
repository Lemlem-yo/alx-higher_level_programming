#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Tests for max_integer()"""
    _max = max_integer

    def test_integers(self):
        """Tests with integers"""
        _max = max_integer
        self.assertEqual(_max([1, 2, 4, 5, 13]), 13)
        self.assertEqual(_max([-1, -2, 0, -7]), 0)
        self.assertEqual(_max([1, 1, 1, 1]), 1)
        self.assertEqual(_max([-10, -12, -150]), -10)

    def test_empty_list(self):
        """Test for empty list as arg"""
        _max = max_integer
        self.assertEqual(_max([]), None)

    def test_one_element(self):
        """Tests for a list of one element"""
        _max = max_integer
        self.assertEqual(_max([4]), 4)

if __name__ == "__main__":
    unittest.main()
