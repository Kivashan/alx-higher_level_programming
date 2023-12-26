#!/usr/bin/python3
"""A Script that prints the State object id based on user input"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    """Create connection to db"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]))

    """Create a session"""
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        query, = session.query(State.id).filter(State.name==argv[4]).first()
    except:
        print('Not found')
    else:
        print(query)
    finally:
        """Closing session releases any resources in use for this session"""
        session.close()
