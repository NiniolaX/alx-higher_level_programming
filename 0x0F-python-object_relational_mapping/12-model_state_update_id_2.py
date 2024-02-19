#!/usr/bin/python3
"""This script changes the name of a State object from the database
hbtn_0e_6_usa.
Database name is passed as an argument to the script.
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

    # Query to get specific state object to modify
    state_to_modify = session.query(State).filter(State.id == 2).first()

    # Check if state exists and modify it it does
    if state_to_modify:
        state_to_modify.name = "New Mexico"

        # Commit changes to the database
        session.commit()
