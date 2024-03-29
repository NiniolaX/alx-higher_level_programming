#!/usr/bin/python3
"""This script prints the State object with the name passed as an argument
from the hbtn_0e_6_usa database.
(hbtn_0e_6_usa is passed as an argument to the script)
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    state_name = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name == state_name).all()

    if states:
        for state in states:
            print(state.id)
    else:
        print("Not found")
