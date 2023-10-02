#!/usr/bin/python3

"""
Unittest for the Rectangle class.
"""
import unittest
from models.rectangle import Rectangle

class TestRectangleClass(unittest.TestCase):
    """Tests the Base class.

    Args:
        unittest (class): unittest
    """

    def test_constructor(self):
        """Tests constructor of the Rectangle class"""
        rect = Rectangle(5, 7)
        rect1 = Rectangle(2, 4)
        self.assertIsInstance(rect, Rectangle)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 7)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect1.id, 2)

    def test_constructor_with_id(self):
        """Tests constructor of Rectangle class with id"""
        rect = Rectangle(5, 7, id=15)
        self.assertEqual(rect.id, 12)

if __name__ == "__main__":
    unittest.main()