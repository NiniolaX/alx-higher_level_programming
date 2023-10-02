#!/usr/bin/python3
"""
This module defines a function 'pascal_triangle' that returns a list of
lists of integers representing the Pascal's triangle of a number, n.

Functions:
    pascal_triangle: Returns a list of integers representing the Pascal's
    triangle of a number, n.

Attributes:
    None
"""


def pascal_triangle(n=None):
    """This function returns a list of list of integers representing the
    Pascal's triangle of n.

    Args:
        n (int): Number

    Returns:
        (list of lists): Integers representing the Pascal's triangle of n.
    """

    res = []
    if n <= 0:
        return res
    for i in range(1, n + 1):
        new_row = []
        num = 1
        for j in range(1, i + 1):
            new_row.append(num)
            num = num * (i - j) // j
        res.append(new_row)
    return res