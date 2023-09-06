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
    # Check for NaN argument
    if a != a:
        return 0
    if b != b:
        return 0

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    # Check for postive and negative infinity arguments
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 0

    return int(a) + int(b)
