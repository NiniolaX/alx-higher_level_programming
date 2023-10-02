#!/usr/bin/python3
"""
This module defines a function that adds a new attribute to an object if
possible.

Functions:
    add_attribute - Adds a new attribute to an object if possible

Attribute:
    None
"""


def add_attribute(obj, attr_name, attr_value):
    """Add attribute function

    Adds a new attribute to an object if possible.

    Args:
        attr_name (int): Name of attribute to be added
        attr_value: Value of attribute to be added

    Raises:
        TypeError: if new attribute can't be added
    """
    if isinstance(obj, (float, str)):
        raise TypeError("can't add new attribute")
    if not hasattr(obj, attr_name):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
