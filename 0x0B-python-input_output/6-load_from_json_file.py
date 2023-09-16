#!/usr/bin/python3
"""
This module defines a function that creates an object from a 'JSON file'.

Attributes:
    None

Functions:
    load_from_json_file - Creates an object from a 'JSON file'.
"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file.

    Args:
        filename (file object): Text file to be written to.

    Returns:
        None.
    """
    with open(filename, encoding='utf-8') as myFile:
        return json.load(myFile)
