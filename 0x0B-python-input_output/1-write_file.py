#!/usr/bin/python3

"""
This module defines a function 'write_file' that writes a string to a text
file and returns the number of characters written.

Attributes:
    None

Functions:
    write_file - Writes a string into a text file and returns the number of
    characters written.

Classes:
    None
"""


def write_file(filename="", text=""):
    """Writes a string to a text file.
    Args:
        filename (str): File to be read
        text (str): String to write into file

    Returns:
        (int): Number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as myFile:
        return myFile.write(text)
