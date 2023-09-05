#!/usr/bin/python3
"""
This module defines a class 'Rectangle' with attibutes- width
and height, and methods for calculating its area and perimeter, and
returning a printable string representation of the rectangle.

Class:
    Rectangle: A basic representation of a rectangle.

Attributes:
    None.

Functions:
    None.
"""


class Rectangle:
    """An class that defines a rectangle.

    This class is a basic representation of a rectangle. It serves as a
    starting point for building more complex Rectangle-related classes.

    Attributes:
        width (int): Width of rectangle
        height (int): Height of rectangle

    Methods:
        __int__():
            Initializes an instance of Rectangle.
            Args:
                width (int): Value for width of instance.
                height (int): Value for height of instance.
        area():
            Calculates and returns the area of the rectangle.
            Args:
                None.
            Returns:
                int: Area of the rectangle.
        perimeter():
            Calculates and returns the perimeter of the rectangle.
            Args:
                None.
            Returns:
                int: Perimeter of the rectangle or 0 if its width or height
                is 0.
        __str__():
            Returns a human readable string representation of object.
        __repr__():
            Returns a string representation of the object which can be used to
            recreateit.
        __del__():
            Prints a feedback text when an object is deleted.

    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets and sets the value of the width of the object.

        Getter:
            Returns:
                int: The width of the object.

        Setter:
            Args:
                value (int): The value to set for width.
            Raises:
                TypeError: If the provided value is not an integer.
                ValueError: If thw provided value is less than 0.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Gets and sets the value of the height of the object.

        Getter:
            Returns:
                int: The height of the object.

        Setter:
            Args:
                value (int): The value to set for the height.
            Raises:
                TypeError: If the provided value is not an integer.
                ValueError: If the provided value is less than 0.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """Returns the string representation of the rectangle using '#'."""
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = ""
        for i in range(self.height):
            if type(self.print_symbol) is not str:
                rectangle_str += str(self.print_symbol) * self.width + '\n'
            else:
                rectangle_str += self.print_symbol * self.width + '\n'
        return rectangle_str[:-1]  # Slicing excludes trailing '\n'

    def __repr__(self):
        """Returns a string representation that can be used to recreate
        the object."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Deletes an instance of the Rectangle class."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on their areas."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        else:
            if rect_1.area() > rect_2.area():
                return rect_1
            else:
                return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance width width == height == size"""
        return cls(size, size)
