#!/usr/bin/python3
"""
This module defines a Square class for representing squares.

This module provides a basic representation of a square and its size.

Class:
    Square: A basic representation of a square.

Attributes:
    None.

Functions:
    None.
"""


class Square:
    """A class that defines a square.

    This class is a representation of a square and provides methods for
    calculating its area.

    Attributes:
        size (int): The size of the square as a positive integer. Defaults
        to 0.

    Methods:
        area():
            Calculates and returns the area of an instance of the Square.
            Args:
                None.
            Returns:
                int: The area of the square.
        my_print():
            Prints the square with the '#' character
            Args:
                None.
            Returns:
                None.

    Raises:
        TypeError: If 'size' is not an integer.
        ValueError: If 'size' is less than 0.
    """

    def __init__(self, size=0):
        """Initializes a square with an optional size."""
        self.size = size

    @property
    def size(self):
        """Getter method for the 'size' attribute"""
        return self.__size

    @size.setter
    def size(self, size):
        """Setter method for the 'size' attribute"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print('#' * self.__size)
