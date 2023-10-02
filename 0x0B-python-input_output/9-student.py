#!/usr/bin/python3
"""
This module defines a class representing a Student.

Class:
    Student: Representation of a student.

Attributes:
    first_name: First name of student.
    last_name: Last name of student.
    age: Age of student.
"""


class Student:
    """A class that defines a student.

    This class is a basic representation of a student.

    Attributes:
        first_name (str): First name of student.
        last_name (str): Last name of student.
        age (int): Age of student.

    Methods:
        to_json: Retrieves a dictionary representation of an instance of
                the class.
    """
    def __init__(self, first_name="", last_name="", age=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dictionary representation of an instance of the class."""
        return self.__dict__
