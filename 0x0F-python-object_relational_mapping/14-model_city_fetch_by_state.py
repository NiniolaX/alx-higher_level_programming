#!/usr/bin/python3
"""This script prints all City objects from the database hbtn_0e_14_usa.
Database name is passed as an argument to the script.
"""

from model_city import City
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    # Create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database
    results = session.query(City, State).join(State).all()

    for row in results:
        print(f"{state.name}: ({city.id}) {city.name}")
