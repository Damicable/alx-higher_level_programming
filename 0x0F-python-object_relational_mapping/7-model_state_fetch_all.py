#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
Your script should take 3 arguments: mysql uname, mysql pswd and db name
You must use the module SQLAlchemy
You must import State and Base - from model_state import Base, State
Script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).order_by(State.id):
        print('{}: {}'.format(instance.id, instance.name))
