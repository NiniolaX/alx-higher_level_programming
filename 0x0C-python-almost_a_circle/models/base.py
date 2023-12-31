#!/usr/bin/python3
"""
This module defines a class 'Base'.

Attributes:
        None
Functions:
        None
"""


class Base:
    """Base class

    Atributes:
            id (int): id of class instance
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
