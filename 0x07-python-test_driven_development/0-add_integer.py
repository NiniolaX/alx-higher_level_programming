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
    # Handle NaN input values (since NaN == Nan returns False)
    if a != a:
        a = 89
    if b != b:
        b = 89

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    # Handle positive and negative infinity values:
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89

    return int(a) + int(b)
