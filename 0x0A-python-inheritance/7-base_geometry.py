#!/usr/bin/python3

"""
This module defines an empty class 'BaseGeometry'.

Attributes:
    None

Classes:
    BaseGeometry: A representation of a geomtery object.
"""


class BaseGeometry:
    """A representation of a geometrical object with methof to calculate it's
    area.

    Attributes:
        None

    Methods:
        area: Calculates the area of the object.
        integer_validator: Validates that the argument 'vaue' is an integer.

    Raises:
        TypeError: If 'value' is not an integer'.
        ValueError: If 'value' is less than or equal to 0.
    """
    def __init__(self, name="", value=None):
        self.name = name
        self.value = value

    def area(self):
        """Calculates the area of the object"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that 'value' is an integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
