#!/usr/bin/python3

"""
This module defines a function that returns the list of available attributes
and methods of an object.

Attributes:
    None

Functions:
    lookup - Returns the list of available attributes and methods of an onject.
"""


def lookup(obj=None):
    """Returns list of available attributes and methods of an object

    Args:
        obj (object): Object to lookup
    Returns:
        list: Available attributes and methods of the object
    """
    return dir(obj)
