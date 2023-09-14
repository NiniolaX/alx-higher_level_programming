#!/usr/bin/python3

"""
This module defines an class 'BaseGeometry'.

Attributes:
    None

Classes:
    BaseGeometry: A representation of a geomtery object.
    Rectangle: A representation of a rectangle. Inherits from 'BaseGeometry'.
    Square: A representation of a square. Inherits from 'Rectangle'.
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
        else:
            return value


class Rectangle(BaseGeometry):
    """A representation of a rectangle.

    Attributes:
        width: width of rectangle
        height: height of an rectangle

    Methods
        Methods:
        area():
            Calculates the area of the rectangle
            Args:
                None
            Returns:
                (int): area of the rectangle
        __str__():
            Returns a string representation of an instance of the class
            Args:
                None
            Returns:
                (str): string representation of an instance of the class
    """
    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def area(self):
        """Calculates the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """A representation of a square.

    Attributes:
        None.

    Methods:
        None
    """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(size, size)
