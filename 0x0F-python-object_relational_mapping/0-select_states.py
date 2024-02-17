#!/usr/bin/python3
"""
This script contains a function that lists all states from a database..
Note: database name is passed as argument to the script.
"""


import MySQLdb
import sys


if __name__ == "__main__":
    # Create a connection with the mysql server
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])

    # Create a cursor object
    cur = db.cursor()

    # Fetch states data from database
    cur.execute("SELECT * FROM states ORDER BY states.id")
    result_rows = cur.fetchall()

    # Print all rows in cursor
    for row in result_rows:
        print(row)

    # Close connection to server
    cur.close()
    db.close()
