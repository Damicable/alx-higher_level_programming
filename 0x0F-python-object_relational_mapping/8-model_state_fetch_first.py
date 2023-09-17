#!/usr/bin/python3
"""
Script that prints the first state object from database hbtn_0e_6_usa
using the module SQLAlchemy
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State).order_by(State.id).first()
    if instance is None:
        print('Nothing')
    else:
        print('{}: {}'.format(instance.id, instance.name))
