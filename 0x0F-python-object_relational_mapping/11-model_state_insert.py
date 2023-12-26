#!/usr/bin/python3
"""A Script that adds a State object to a given db"""


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

    sta = 'Louisiana'
    session.add(State(name=sta))
    session.commit()
    try:
        index, = session.query(State.id).filter(State.name == sta).first()
    except TypeError as err:
        raise err
    else:
        print(index)
    finally:
        session.close()
