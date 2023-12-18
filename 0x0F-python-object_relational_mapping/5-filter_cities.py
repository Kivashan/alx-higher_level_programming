#!/usr/bin/python3
""" Module that lists cities by state"""

from sys import argv
import MySQLdb

if __name__ == "__main__":

    """Create db connection"""
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         password=argv[2], db=argv[3])

    """Create cursor object"""
    cur = db.cursor()

    user_state_input = (argv[4],)
    sql_query = "SELECT cities.name, states.name  FROM cities "\
                "INNER JOIN states "\
                "ON states.id = cities.state_id WHERE states.name = %s"

    cur.execute(sql_query, user_state_input)
    rows = cur.fetchall()

    for i in rows:
        if i[0] != rows[0][0]:
            print(", ", end='')
        print(i[0], end='')
    print()
