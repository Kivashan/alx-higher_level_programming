#!/usr/bin/python3
"""Module that lists all cities from a database"""

from sys import argv
import MySQLdb

if __name__ == "__main__":

    """Create connect to db"""
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         password=argv[2], db=argv[3])

    """Create cursor object"""
    cur = db.cursor()

    cur.execute('SELECT cities.id, cities.name, states.name FROM states '
                'INNER JOIN cities ON states.id = cities.state_id')

    rows = cur.fetchall()

    for i in rows:
        print(i)
