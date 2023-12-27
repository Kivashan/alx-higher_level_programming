#!/usr/bin/python3
"""A Script that prints all city objects from a given database"""


from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    """Create connection to db"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]))

    """Create session"""
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State.name, City.id, City.name).\
        join(City).order_by(City.id).all()
    for i in query:
        print("{}: ({}) {}".format(i[0], i[1], i[2]))
