#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa.
(Database name, mysqluser name and password is passed to the script).
"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         database=sys.argv[3])
    cur = db.cursor()
    query = """
            SELECT cities.id, cities.name, states.name
            FROM cities
            INNER JOIN states ON cities.state_id = states.id
            ORDER BY cities.id
    """
    cur.execute(query)
    row = cur.fetchone()
    while row is not None:
        print(row)
        row = cur.fetchone()
