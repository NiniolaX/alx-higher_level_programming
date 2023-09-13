#!/usr/bin/python3

"""
This module contains a function which checks whether an object is an
instance of a class that inherits (directly or indirectly) from the specified
class.

Attributes:
    None

Functions:
    inherits_from - Checks if an object is an instance of a class that inherits
    from the specified class.
"""


def inherits_from(obj, a_class):
    """Function checks if an object is an instance of a class that inherits
    from the specified class.

    Args:
        obj (object): Object to be examined
        a_class (class): Class to compare with object

    Returns:
        bool: True if object is an instance of a class that inherits from the
        specified class; otherwise, False.
    """
    return issubclass(type(obj), a_class)
