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

    This class is a representation of a square. It instantiates it with an
    optional size and validating that size is an integer and not less than 0
    before instantiation.

    Attributes:
        size (int): The size of the square as a positive integer.

    Methods:
        None.
    """

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
