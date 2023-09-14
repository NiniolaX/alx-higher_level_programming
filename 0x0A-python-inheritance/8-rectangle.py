#!/usr/bin/python3

"""
This module defines an class 'BaseGeometry'.

Attributes:
    None

Classes:
    BaseGeometry: A representation of a geomtery object.
    Rectangle: A representation of a rectangle. Inherits from 'BaseGeometry'.
"""


class BaseGeometry:
    """A representation of a geometrical object with method to calculate it's
    area and validate the value of it's attribute.

    Attributes:
        name: name of the geometrical quantity.
        value: value of the quantity

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

    def integer_validator(self, name="", value=None):
        """Validates that 'value' is an integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value < 1:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A representation of a rectangele.

    Attributes:
        width: width of rectangle
        height: height of an rectangle

    Methods:
        None
    """
    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
