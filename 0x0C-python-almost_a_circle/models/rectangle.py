#!/usr/bin/python3
"""This module defines a class 'Rectangle'

Attributes:
    None

Functions:
    None
    """
from models.base import Base


class Rectangle(Base):
    """Rectangle class

    Attributes:
        width (int): width of rectangle
        height (int): height of rectangle
        x (int, optional): horizontal position
        y (int, optional): vertical position
        id (int): id of class instance

    Methods:
        area:
            Returns the area of the Rectangle instance.
            Args:
                None
        display:
            Prints the Rectangle instance with the character '#' to stdout.
            Args:
                None
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets and sets the value for the width attribute.

        Getter:
            Returns:
                int: width of the object

        Setter:
            Args:
                width (int): value to set for width
            Raises:
                TypeError: If width is not an integer
                ValueError: If width <= 0

        """
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """Gets and sets the value for the height attribute.

        Getter:
            Returns:
                int: height of the object

        Setter:
            Args:
                height (int): value to set for height
            Raises:
                TypeError: If height is not an integer
                ValueError: If height <= 0
        """
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """Gets and sets the value for the x attribute.

        Getter:
            Returns:
                int: horizontal position of object

        Setter:
            Args:
                x (int): value to set for x
            Raises:
                TypeError: If x is not an integer
                ValueError: If x < 0
        """
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """Gets and sets the value for the y attribute.

        Getter:
            Returns:
                int: vertical position of object

        Setter:
            Args:
                y (int): value to set for y
            Raises:
                TypeError: If y is not an integer
                ValueError: If y < 0
        """
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """Returns the area of the Rectangle instance"""
        return self.width * self.height

    def display(self):
        """Prints the Rectangle instance to stdout with the '#' character"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            for i in range(self.x):
                print(" ", end="")
            print('#' * self.width)

    def __str__(self):
        """Returns the string representation of a Rectangle instance
        Format: [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - \
{self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute of a Rectangle instance"""
        if len(args) > 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.__dict__.update({key: value})
                elif key in ("width", "height", "x", "y"):
                    n_key = "_" + self.__class__.__name__ + "__" + key
                    self.__dict__.update({n_key: value})
