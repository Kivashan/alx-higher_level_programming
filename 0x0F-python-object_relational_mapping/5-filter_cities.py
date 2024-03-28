#!/usr/bin/python3
"""Write a script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""

from sys import argv
import MySQLdb as m

if __name__ == '__main__':
    db = m.connect(host='localhost', user=argv[1], passwd=argv[2], db=argv[3],
                   port=3306)

    cur = db.cursor()

    db_query = "SELECT cities.name FROM cities INNER JOIN states ON "\
               "states.id = cities.state_id "\
               "WHERE states.name LIKE BINARY %s ORDER BY cities.id"

    a = cur.execute(db_query, (argv[4],))
    for i in range(a):
        if i > 0:
            print(', ', end='')
        print(cur.fetchone()[0], end='')
    print()
