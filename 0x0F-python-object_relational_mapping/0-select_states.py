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


if __name__ == "__main__":
    # Create a connection with the mysql server
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])

    # Create a cursor object
    cur = db.cursor()

    # Fetch data fron database into cursor object
    cur.execute("SELECT * FROM states ORDER BY states.id")

    # Print all rows in cursor
    result_rows = cur.fetchall()
    for row in result_rows:
        print(row)

    # Close connection to server
    cur.close()
    db.close()
