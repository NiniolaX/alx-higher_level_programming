#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa
(database name is passed as argument to the script).
"""


import MySQLdb
import sys

# Extract script arguments
args = sys.argv[1:]

username = args[0]
password = args[1]
database_name = args[2]

# Connect to database and load all rows in state table into the cursor object
db = MySQLdb.connect(host="localhost", user=username, passwd=password,
                     db=database_name, port=3306)
cur = db.cursor()
cur.execute("SELECT * FROM states")

# Print all rows in the cursor
row = cur.fetchone()
while (row is not None):
    print(row)
    row = cur.fetchone()
