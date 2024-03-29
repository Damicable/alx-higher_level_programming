#!/usr/bin/python3
"""
This contains the definition of a State class and an instance
City relationship
"""

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """This class State inherits from Base Tips
    This class attributes represents a relationship with the class City.
   """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
