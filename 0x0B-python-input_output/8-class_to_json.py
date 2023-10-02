#!/usr/bin/python3
"""
This module defines a function that returns the dictionary description with
simple data structure (list, dictionary, string, integer and boolean) for JSON
serialization of an object.

Attributes:
    None

Function:
    class_to_json: Returns the dictionary description of an object with simple
    data structure that can be used for JSON serialization of the object.
"""


def class_to_json(obj):
    """Returns the ditionary description of an object with simple data
    structures (list, dictionary, string, integer and boolean), that can be
    used for JSON serialization of the object.

    Args:
        obj - An instance of a class
    """
    return obj.__dict__
