#!/usr/bin/python3

"""
This module defines a function that checks if an object is an instance of
a specified class, or of an instance of a class that inherited from the
specified class.

Attributes:
    None

Functions:
    is_kind_of_class: Checks if an object is an instance of, or an instance of
    a class inherited from the specified class.
"""


def is_kind_of_class(obj, a_class):
    """Function checks if an object is an instance of a class or an instance
    of a class that inherited from the specified class.

    Args:
        obj (object): Object to be examined
        a_class (class): Class to be compared with object

    Return:
        bool: True if object is an instance of the specified class, or the
        class's ancestor; otherwise False
    """
    return isinstance(obj, a_class)