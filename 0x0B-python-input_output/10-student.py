#!/usr/bin/python3
"""
This module defines a class representing a Student.

Class:
    Student: Representation of a student.

Attributes:
    first_name (str): First name of student.
    last_name (str): Last name of student.
    age (int): Age of student.
"""


class Student:
    """A class that defines a student.

    This class is a basic representation of a student.

    Attributes:
        first_name: First name of student.
        last_name: Last name of student.
        age: Age of student.

    Methods:
        to_json: Retrieves a dictionary representation of an instance of
                the class. If attrs is a list of strings, only attribute
                names contained in this list must be retrieved
                Args:
                    attrs - list of attribute to be retrieved
    """
    def __init__(self, first_name="", last_name="", age=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list) and all(isinstance(item, str) for item
                                           in attrs):
           return {key: self.__dict__[key] for key in attrs if key in self.__dict__}
        return self.__dict__