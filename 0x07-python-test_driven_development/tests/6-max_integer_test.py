#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def basictest(self):
        maxi = max_integer([1, 2, 3])
        self.assertEqual(maxi, 3)

    def test_mixed_list(self):
        with self.assertRaises(TypeError):
            max_integer([1, 3, "j"])

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)
if __name__ == '__main__':
    unittest.main()
