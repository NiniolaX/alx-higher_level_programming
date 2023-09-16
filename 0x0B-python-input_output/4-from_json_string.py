#!/usr/bin/python3
"""
This module defines a function that returns an object represented by a JSON
string.

Attributes:
    None

Functions:
    from_json_string - Returns an object represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """Returns the an object (Python data structure) represented by a JSON
    string.

    Args:
        my_str (string): JSON string

    Returns:
        str: Object (python data structure).
    """
    return json.loads(my_str)