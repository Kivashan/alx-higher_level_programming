#!/usr/bin/python3
"""A Script that lists all state objects and corresponding city objects"""


from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    """Create connection to db"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]))

    """Create tables in db if not exists"""
    Base.metadata.create_all(engine)

    """Create session"""
    Session = sessionmaker(bind=engine)
    session = Session()

    state_objects = session.query(State).order_by(State.id).all()

    for state in state_objects:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

    session.close()
