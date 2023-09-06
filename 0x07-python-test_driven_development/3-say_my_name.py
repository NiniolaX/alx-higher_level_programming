#!/usr/bin/python3
"""
This module defines a function that prints a person's name.

Class:
    None.

Attributes:
    None.

Functions:
    say_my_name: Prints a person's name.
"""


def say_my_name(first_name="", last_name=""):
    """Prints a persons name in format: My name is <first_name> <last_name>

    Args:
        first_name (str): First name of person.
        last_name (str): Last name of person.

    Returns:
        None.

    Raises:
        TypeError: If first_name or last_name are not strings.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print('My name is {} {}'.format(first_name, last_name))
