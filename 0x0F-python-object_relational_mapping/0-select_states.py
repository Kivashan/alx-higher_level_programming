#!/usr/bin/python3
"""A script that select all states from a database"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    """Create connection with database"""
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         password=argv[2], db=argv[3])

    """Create cursor object"""
    cur = db.cursor()

    """Select all states in database"""
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()

    for i in rows:
        print("{}".format(i))
