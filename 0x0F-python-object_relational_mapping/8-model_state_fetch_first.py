#!/usr/bin/python3
"""A script that prints the first State object from a given db"""


from sys import argv, exit
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    if (len(argv) < 4):
        exit("Incorrect number of arguments passed")

    """Create connection to db"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]))

    """Create session"""
    Session = sessionmaker(bind=engine)
    session = Session()

    first = session.query(State).first()
    if (first):
        print("{:d}: {}".format(first.id, first.name))

    """End session: releases resources used in session"""
    session.close()
