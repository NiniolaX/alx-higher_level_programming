#!/usr/bin/python3
"""
Inserts a line of text to a file, after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """ Inserts a string to a file after a specific string
    Args:
        search_string (str): String after which new string is to be inserted
        new_string (str): String to insert
    Return:
        None
    """
    new_file = ""
    with open(filename, "r") as f:
        for line in f:
            new_file += line
            if search_string in line:
                new_file += new_string

    with open(filename, "w") as f:
        f.write(new_file)
