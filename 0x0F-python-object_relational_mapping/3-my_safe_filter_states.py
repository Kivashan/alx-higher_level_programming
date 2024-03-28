#!/usr/bin/python3
"""write a script that takes in arguments and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections.
"""

from sys import argv
import MySQLdb as m

if __name__ == '__main__':
    db = m.connect(host='localhost', user=argv[1], passwd=argv[2], db=argv[3],\
                   port=argv[4])

    cur = db.cursor()

    db_query = 'SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id'\
               .format(argv[4])

    a = cur.execute(db_query)
    for i in range(a):
        print(cur.fetchone())

    cur.close()
    db.close()
