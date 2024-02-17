#!/usr/bin/python3
"""This script takes in an argument and returns rows in the states table
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
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY states.id",
                (argument,))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
