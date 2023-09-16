#!/usr/bin/python3

"""
This module defines a function 'read_file' which reads a text file (UTF8)
and prints it to stdout.

Attributes:
    None

Functions:
    read_file - Reads a text file and prints it to stdout

Classes:
    None
"""



def read_file(filename=""):
    """Reads a text file and prints it to stdout.
    Args:
        filename (str): File to be read
    Returns:
        Nothing
    """
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read())
