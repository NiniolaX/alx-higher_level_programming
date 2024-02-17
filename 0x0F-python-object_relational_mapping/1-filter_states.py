#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to database
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], database=sys.argv[3])
    cur = db.cursor()

    # Fetch data from database
    cur.execute("SELECT * FROM states WHERE name LIKE 'n%' ORDER BY states.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Severe connection with database
    cur.close()
    db.close()
