#!/usr/bin/python3
"""
This module defines a function that formats and prints a text.

Class:
    None.

Attributes:
    None.

Functions:
    text_indentation: Prints a text with two new lines after each of these
    characters: '.', '?' and ':'
"""


def text_indentation(text):
    """Prints a text with 2 new lines after characters '.', '?' and ':'

    Args:
        text (str): Text to print

    Returns: None.

    Raises:
        TypeError: If text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for c in text:
        print(c, end="")
        if c == '.' or c == '?' or c == ':':
            print('\n')
