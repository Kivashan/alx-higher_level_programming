#!/usr/bin/python3
"""a script that lists all states from the database hbtn_0e_0_usa"""

from sys import argv
import MySQLdb as m

if __name__ == '__main__':
    # Create a connection to db
    db = m.connect(host='localhost', user=argv[1], passwd=argv[2], db=argv[3],\
                   port=3306)

    # Create a cursor object
    cur = db.cursor()

    # Select states in db
    a = cur.execute("SELECT * FROM states ORDER BY states.id")
    for i in range(a):
        print(cur.fetchone())

    # Clean up
    cur.close()
    db.close()
