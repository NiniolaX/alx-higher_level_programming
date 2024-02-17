#!/usr/bin/python3
"""
This script contains a function that lists all states from a database..
Note: database name is passed as argument to the script.

Functions:
    list_states: Lists all states from a specified database

Attributes:
    None
"""


import MySQLdb
import sys


def list_states(username, password, database_name):
    """Lists all states of a specified database

    Args:
        username(str): MySQL username
        password(str): MySQL password
        database_name: MySQL database to use

    Returns:
        None
    """
    db = MySQLdb.connect(host="localhost", user=username, passwd=password,
                         db=database_name, port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")

    # Print all rows in the cursor
    row = cur.fetchone()
    while (row is not None):
        print(row)
        row = cur.fetchone()


if __name__ == "__main__":
    args = sys.argv[1:]  # First argument is name of script
    if len(args) == 3:
        list_states(args[0], args[1], args[2])
