#!/usr/bin/python3
"""A city class"""


from model_state import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy import ForeignKey

class City(Base):
    """A city class"""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))

    def __repr__(self):
        return "<City(name = '%s', state_id = '%s')>" % (self.name, self.state_id)
