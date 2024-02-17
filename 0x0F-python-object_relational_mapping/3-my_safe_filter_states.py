#!/usr/bin/python3
"""This script takes in an argument and displays all values in the states table
where name matches the argument, safe from MySQL injections.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    state_name_searched = sys.argv[4]

    # Establish connection to database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         database=sys.argv[3])
    cur = db.cursor()

    # Execute query
    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY states.id"
    cur.execute(query, (state_name_searched,))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Clean up
    cur.close()
    db.close()
