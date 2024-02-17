#!/usr/bin/python3
"""This script takes in an argument and displays rows in the states table
where name matches the argument.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    argument = sys.argv[4]

    # Establish connection to database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         database=sys.argv[3])
    cur = db.cursor()

    # Execute query
    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY states.id"
    cur.execute(query, (argument,))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Clean up
    cur.close()
    db.close()
