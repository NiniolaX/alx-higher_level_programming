#!/usr/bin/python3
"""
This modue defines a function that prints a square.

Class:
    None.

Attributes:
    None.

Functions:
    print_square: Prints a square with the character '#'.
"""


def print_square(size):
    """Prints a square with the character '#'.

   Args:
    size (int): Length of the square.

    Returns:
        None.

    Raises:
        TypeError: If:
            (i) size is not an ineger.
            (ii) size is a float and is less than 0.
        ValueError: If size is less than 0.
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            print('#' * size)
