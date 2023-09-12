#!/usr/bin/python3

"""
This module defines a class 'MyList' that inherits from 'list', with method
for printing the list, but sorted.

Class:
    MyList: A child class of list.

Attributes:
    None

Functions:
    None
"""

class MyList(list):
    """A child class of the 'list' class.
    
    Attributes:
        None

    Methods:
        print_sorted:
            Prints an instance of 'MyList', but sorted in ascending order.
            Args:
                None

            Returns:
                None
    """
    def __init__(self):
        self.my_list = []
        pass

    def print_sorted(self):
        "Prints the list sorted in ascending order."
        sorted_list = sorted(self.my_list)
        print(sorted_list)