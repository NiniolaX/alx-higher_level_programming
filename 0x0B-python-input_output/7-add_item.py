#!/usr/bin/python3
"""
This script adds all arguments to a Python list, and then saves them to a
file.

Attributes:
    None.

Functions:
    None
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv[1:]
filename = 'add_item.json'

try:
    with open(filename):
        pass
except FileNotFoundError:
    # Create an empty lis if file does not exist
    myList = []
else:
    # Get previous list from json file
    myList = load_from_json_file(filename)

myList.extend(args)

save_to_json_file(myList, filename)