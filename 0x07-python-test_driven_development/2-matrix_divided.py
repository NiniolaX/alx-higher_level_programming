#!/usr/bin/python3

"""
This module defines a function matrix_divided which divides all the elments of
a matrix by a number.

Attributes:
    None

Functions:
    matrix_divided: Divides a matrix by a number.
"""


def matrix_divided(matrix, div):
    """Function to divide a matrix

    Args:
        matrix (list of lists): Matrix to be divided.
        div (int or float): Divisor.

    Returns:
        list of lists: A new matrix containing the result of the division.

    Raises:
        ZeroDivisionError: If div is equal to 0.
        TypeError: If: (i) matrix is not a list of lists;
            (ii) rows of matrix differ in size;
            (iii) an element of matrix is not an int or float;
            (iv) div is not an integer or float.
    """
    # Check if matrix is empty
    if not matrix:
        return []

    # Check if matrix is a list of lists
    if type(matrix) is not list or not all(type(rw) is list for rw in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

    # Check if length of rows are the same
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if all elements in matrix are int or float
    if not all(isinstance(e, (int, float)) for row in matrix for e in row):
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    # Check if div an int or float
    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    # Check if div is 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division
    new_matrix = []
    for row in matrix:
        new_matrix.append([round(e / div, 2) for e in row])

    return new_matrix
