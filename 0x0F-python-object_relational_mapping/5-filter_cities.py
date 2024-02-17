#!/usr/bin/python3
"""
Script takes in the name of a state as an argument and lists all the cities
of that state, using the hbtn_0c_4_usa database.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    state_name = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         database=sys.argv[3])
    cur = db.cursor()
    query = """
            SELECT name
            FROM cities
            WHERE state_id = (SELECT id FROM states WHERE name = %s)
            ORDER BY cities.id
    """
    cur.execute(query, (state_name,))
    rows = cur.fetchall()
    print(", ".join(row[0] for row in rows))

    cur.close()
    db.close()
