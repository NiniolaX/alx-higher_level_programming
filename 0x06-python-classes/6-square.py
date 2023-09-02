#!/usr/bin/python3
"""
This module defines a Square class for representing squares.

This module provides a basic representation of a square.

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
    calculating its area and printing it.

    Attributes:
        size (int): The size of the square as a positive integer. Defaults
        to 0.
        position (tuple): The position of the square with respect to stdout.

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
        TypeError: If 'size' is not an integer or position is not a tuple of
        2 positive integers.
        ValueError: If 'size' is less than 0.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square with an optional size."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method for the 'size' attribute."""
        return self.__size

    @property
    def position(self):
        """Getter method for 'position' attribute."""
        return self.__position

    @size.setter
    def size(self, size):
        """Setter method for the 'size' attribute of square."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @position.setter
    def position(self, value):
        """Setter method for 'position' attribute of square."""
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif all(type(elem) is not int or elem < 0 for elem in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the area of the square."""
        return self.size ** 2

    def my_print(self):
        """Prints the square."""
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                print(' ' * (self.position)[0] + '#' * self.size)
