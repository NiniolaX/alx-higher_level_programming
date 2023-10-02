#!/usr/bin/python3
"""
This module defines a class 'MyInt' that inherits from int

Attributes:
    None

Functions:
    None
"""


class MyInt(int):
    """This class hass == and != operators inverted

    Attributes:
        None

    Methods:
        None
    """
    def __eq__(self, other):
        """Inverts the behaviour of __eq__"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts the behaviour of __ne__"""
        return super().__eq__(other)
