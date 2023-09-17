#!/usr/bin/python3
"""
This contains the definition of Class City.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State

class City(Base):
    """City class inherits from the Base imported from model_state"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
