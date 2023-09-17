#!/usr/bin/python3
"""script that lists all State objects that contain the letter a from
the database hbtn_0e_6_usa using SQLAlchemy module
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine, text)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(
            text("name LIKE '%a%'")).order_by(State.id)
    for state in query.all():
        print('{}: {}'.format(state.id, state.name))