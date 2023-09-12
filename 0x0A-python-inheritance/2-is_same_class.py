#!/usr/bin/python3

"""
This module defines a function 'is_same_class' that checks if an object is
exactly an instance of the specified class.

Attributes:
    None

Functions:
    is_same_class - Checks is an object is exactly an instance of a specified
    class.
"""


def is_same_class(obj, a_class):
    """Function checks if an object is exactly an instance of the specified
    class.

    Args:
        obj (object): Object to be examined
        a_class (class): Class to be compared with object

    Return:
        Bool: 'True' if object is exactly an instance of the class; 'False'
        otherwise.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
