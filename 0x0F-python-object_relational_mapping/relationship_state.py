#!/usr/bin/python3
"""State class"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """A class that inherits from declarative_base in order to map our class
    to our states table in our db"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
            cascade='all, delete, delete-orphan')
