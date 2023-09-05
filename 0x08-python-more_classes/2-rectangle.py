#!/usr/bin/python3
"""
This module defines a class 'Rectangle' with attibutes- width
    and height, and methods for calculating its area and perimeter.

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
    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

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
