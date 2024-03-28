#!/usr/bin/python3
"""List city by states"""

from sys import argv
import MySQLdb as m

if __name__ == '__main__':
    db = m.connect(host='localhost', user=argv[1], passwd=argv[2], db=argv[3],
                   port=3306)

    cur = db.cursor()

    db_query = 'SELECT cities.id, cities.name, states.name FROM cities'\
               ' INNER JOIN states ON cities.state_id = states.id'

    a = cur.execute(db_query)
    for i in range(a):
        print(cur.fetchone())

    cur.close()
    db.close()
