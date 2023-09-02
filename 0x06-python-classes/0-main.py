#!/usr/bin/python3

"""
This script demonstrates the use of the Square class in module '0-square'
module.
"""

# Import the module
Square = __import__('0-square').Square

# Create an instance of the Square class
my_square = Square()

# Prints the type of the my_square object
print(type(my_square))

# Prints the dictionary representation of 'my_square.
print(my_square.__dict__)
