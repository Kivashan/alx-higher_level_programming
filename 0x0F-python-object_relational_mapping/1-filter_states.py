#!/usr/bin/python3
"""a script that lists all states with a name starting with N (upper N)"""

from sys import argv
import MySQLdb as m

if __name__ == '__main__':
    db = m.connect(host='localhost', user=argv[1], passwd=argv[2], db=argv[3],
                   port=3306)

    cur = db.cursor()

    db_query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id"
    a = cur.execute(db_query)
    for i in range(a):
        print(cur.fetchone())

    # clean up
    cur.close()
    db.close()
