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
        self.assertEqual(rect.id, 15)

    def test_width_getter(self):
        """Tests width getter"""
        rect = Rectangle(3, 8, x=1, y=2)
        self.assertEqual(rect.width, 3)

    def test_width_type_error(self):
        """Test validity of width type"""
        rect = Rectangle(3, 8, x=1, y=2)
        with self.assertRaises(TypeError):
            rect.width = 'a'
        with self.assertRaises(TypeError):
            rect.width = True
        with self.assertRaises(TypeError):
            rect.width = [1,2,3]
        with self.assertRaises(TypeError):
            rect.width = (1,2,3)
        with self.assertRaises(TypeError):
            rect.width = {1: 'a', 2: 'b'}

    def test_width_value_error(self):
        """Test validity of width value"""
        rect = Rectangle(5, 4, x=1, y=2)
        with self.assertRaises(ValueError):
            rect.width = -1
        with self.assertRaises(ValueError):
            rect.width = 0

    def test_height_getter(self):
        """Tests height getter"""
        rect = Rectangle(3, 8, x=1, y=2)
        self.assertEqual(rect.height, 8)

    def test_height_type_error(self):
        """Test validity of width type"""
        rect = Rectangle(3, 8, x=1, y=2)
        with self.assertRaises(TypeError):
            rect.height = 'b'
        with self.assertRaises(TypeError):
            rect.width = False
        with self.assertRaises(TypeError):
            rect.height = [1,2,3]
        with self.assertRaises(TypeError):
            rect.height = (1,2,3)
        with self.assertRaises(TypeError):
            rect.height = {1: 'a', 2: 'b'}

    def test_height_value_error(self):
        """Test validity of width value"""
        rect = Rectangle(5, 4, x=1, y=2)
        with self.assertRaises(ValueError):
            rect.height = -100
        with self.assertRaises(ValueError):
            rect.height = 0

    def test_x_getter(self):
        """Tests x getter"""
        rect = Rectangle(3, 8, x=1, y=2)
        self.assertEqual(rect.x, 1)

    def test_x_type_error(self):
        """Test validity of x type"""
        rect = Rectangle(3, 8, x=1, y=2)
        with self.assertRaises(TypeError):
            rect.x = 'b'
        with self.assertRaises(TypeError):
            rect.x = False
        with self.assertRaises(TypeError):
            rect.x = [1,2,3]

    def test_x_value_error(self):
        """Test validity of x value"""
        rect = Rectangle(5, 4, x=1, y=2)
        with self.assertRaises(ValueError):
            rect.x = -1000

    def test_y_getter(self):
        """Tests y getter"""
        rect = Rectangle(3, 8, x=1, y=2)
        self.assertEqual(rect.y, 2)

    def test_y_type_error(self):
        """Test validity of y type"""
        rect = Rectangle(3, 8, x=1, y=2)
        with self.assertRaises(TypeError):
            rect.y = 'b'
        with self.assertRaises(TypeError):
            rect.y = True
        with self.assertRaises(TypeError):
            rect.y = {1,2,3}

    def test_y_value_error(self):
        """Test validity of y value"""
        rect = Rectangle(5, 4, x=1, y=2)
        with self.assertRaises(ValueError):
            rect.y = -10000

if __name__ == "__main__":
    unittest.main()