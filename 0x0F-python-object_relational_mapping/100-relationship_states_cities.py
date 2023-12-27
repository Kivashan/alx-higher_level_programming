#!/usr/bin/python3
"""A script that creates a given state and city from a given db"""


from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    """Create a connection to the db"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]))

    """Create tables"""
    Base.metadata.create_all(engine)

    """Create session"""
    Session = sessionmaker(bind=engine)
    session = Session()

    """Create new State and City objects"""
    city = City(name='San Francisco')
    city.state = State(name='California')

    """Add state object to session, no need to add city object as they are
    both linked because of relationship and backref, see state class for
    use"""
    session.add(city)
    session.commit()
    session.close()
