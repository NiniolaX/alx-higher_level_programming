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
				width (int): Value to set for width
		"""
		return self.__width

	@width.setter
	def width(self, width):
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
		"""
		return self.__height

	@height.setter
	def height(self, height):
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
		"""
		return self.__x

	@x.setter
	def x(self, x):
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
		"""
		return self.__y

	@y.setter
	def y(self, y):
		self.__y = y