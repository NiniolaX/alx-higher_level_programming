#!/usr/bin/python3
"""This script deletes all state objects with name containing the letter 'a'
from the database hbtn_0e_6_usa.
Database name is passed to script.
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_del = session.query(State).filter(State.name.like('%a%')).all()

    if states_to_del:
        for state in states_to_del:
            session.delete(state)
        session.commit()
