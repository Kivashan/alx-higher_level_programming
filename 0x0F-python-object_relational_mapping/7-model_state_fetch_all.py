#!/usr/bin/python3
"""A script that lists all states from a given db"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":

    """Create a connection to db"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]))

    """Create a session"""
    Session = sessionmaker(bind=engine)
    session = Session()

    for index, state in session.query(State.id, State.name).order_by(State.id):
        print("{:d}: {}".format(index, state))

    """release any resources still in use by session"""
    session.close()
