#!/usr/bin/python3
"""Write a script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
"""

from sys import argv
import MySQLdb as m

if __name__ == '__main__':
    db = m.connect(host='localhost', user=argv[1], passwd=argv[2], db=argv[3],\
                   port=3306)

    cur = db.cursor()

    db_query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id"\
                .format(argv[4])

    a = cur.execute(db_query)
    for i in range(a):
      print(cur.fetchone())

    # clean up
    cur.close()
    db.close()
