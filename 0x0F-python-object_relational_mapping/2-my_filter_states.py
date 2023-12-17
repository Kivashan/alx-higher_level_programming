#!/usr/bin/python3
"""Script that matches a name in a db and prints result of match"""

from sys import argv
import MySQLdb

if __name__ == "__main__":

    """Create connection"""
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         password=argv[2], db=argv[3])

    """Create cursor object"""
    cur = db.cursor()

    userinput = "SELECT * FROM states WHERE name = '{}'".format(argv[4])

    cur.execute(userinput)
    rows = cur.fetchall()

    for i in rows:
        print(i)
