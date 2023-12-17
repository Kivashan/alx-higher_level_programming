#!/usr/bin/python3
"""Script that returns a list of states based on user input"""

from sys import argv
import MySQLdb
from validator import validator

if __name__ == "__main__":

    local_data = []

    """Create connection to db"""
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         password=argv[2], db=argv[3])

    """Create cursor object"""
    cur = db.cursor()

    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()

    """Call Validator function"""
    local_data = validator(rows, argv[4])

    if local_data != []:
        for i in local_data:
            print(i)

    cur.close()
    db.close()
