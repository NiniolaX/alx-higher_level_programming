#!/usr/bin/python3
"""
This module defines a function that writes an object to a text file using a
JSON representation.

Attributes:
    None

Functions:
    save_to_json_file - Writes an object to a text file using a JSON
    representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using a JSON representation.

    Args:
        my_obj (object): Object to be written to file.
        filename (file object): Text file to be written to.

    Returns:
        None.
    """
    with open(filename, 'w') as myFile:
        json.dump(my_obj, myFile)