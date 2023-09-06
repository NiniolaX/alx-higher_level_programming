#!/usr/bin/python3

"""
This module defines a function add_integer for adding two integer or floats.

Attributes:
    None

Functions:
    add_integer: Adds two numbers.
"""


def add_integer(a, b=98):
    """Addition function

    Function adds two numbers.

    Args:
        a (int or float): The first integer.
        b (int or float): The second integer.

    Returns:
        int or float: The sum of a and b

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if type(a) not in (int, float) or a != a or a == float('inf') or \
            a == -float('inf'):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float) or b != b or b == float('inf') or \
            b == -float('inf'):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
