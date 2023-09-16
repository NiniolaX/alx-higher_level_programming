#!/usr/bin/python3

"""
This module defines a function 'write_file' that appends a string to a text
file and returns the number of characters added.

Attributes:
    None

Functions:
    append_write - Appends a string into a text file and returns the number of
    characters written.

Classes:
    None
"""


def append_write(filename="", text=""):
    """Appends a string to a text file.
    Args:
        filename (str): File to be read
        text (str): String to write into file

    Returns:
        (int): Number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as myFile:
        return myFile.write(text)