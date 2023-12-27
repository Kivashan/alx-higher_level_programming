#!/usr/bin/python3
"""Script that deletes all State objects that contain the letter a"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    """Create connection to the db"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]))

    """Create session"""
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(State.name.like('%a%')).all()

    if query:
        for i in query:
            session.delete(i)
        session.commit()
    session.close()
