#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests the msx_integer function."""

    def test_normal_case(self):
        """Test with normal cases"""
        self.assertEqual(max_integer([1, 5, 2, 4]), 5)
        self.assertEqual(max_integer([-2, 7, 0, -10]), 7)
        self.assertEqual(max_integer([-5, -0.5, -25, -15]), -0.5)
        self.assertEqual(max_integer([0, -2, -10]), 0)
        self.assertEqual(max_integer([-7]), -7)
        self.assertEqual(max_integer([0]), 0)

    def test_empty_list(self):
        """Tests with empty list"""
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer())

    def test_wrong_type(self):
        """Tests with wrong argument type"""
        self.assertRaises(TypeError, max_integer, 2)
        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(TypeError, max_integer, [1, -5, 'a', 7])
        self.assertRaises(TypeError, max_integer, [1, -5, [6], 7])


if __name__ == "__main__":
    unittest.main()
