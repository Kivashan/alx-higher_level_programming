#!/usr/bin/python3
"""Script that lists all states beginning with 'N'"""

from sys import argv
import MySQLdb

if __name__ == "__main__":

    """Create connection to db"""
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         password=argv[2], db=argv[3])

    """Create cursor object"""
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    rows = cur.fetchall()

    for i in rows:
        print(i)

    cur.close()
