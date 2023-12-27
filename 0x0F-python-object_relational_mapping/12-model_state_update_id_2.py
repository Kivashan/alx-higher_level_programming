#!/usr/bin/python3
"""A Script that changes the name of a State"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    """Create a connection to db"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]))

    """Create a session"""
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        query, = session.query(State).filter(State.id == 2).all()
    except TypeError as err:
        raise err
    else:
        query.name = 'New Mexico'
        session.commit()
    finally:
        session.close()
