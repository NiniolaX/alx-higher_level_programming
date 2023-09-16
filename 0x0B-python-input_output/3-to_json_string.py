#!/usr/bin/python3
"""
This module defines a function that returns the JSON representation of an
object.

Attributes:
    None

Functions:
    to_json_string - Returns the JSON representation of an object.
"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an onject

    Args:
        my_obj (object): Object whos JSON representation is to be returned.

    Returns:
        str: JSON representation of object.
    """
    return json.dumps(my_obj)