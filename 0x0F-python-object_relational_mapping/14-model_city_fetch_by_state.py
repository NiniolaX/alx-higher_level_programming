#!/usr/bin/python3
"""This script prints all City objects from the database hbtn_0e_14_usa.
Database name is passed as an argument to the script.
"""

from model_city import City
from model_state import State
from sqlalchemy import create_engine, select
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
    query = select(City, State).select_from(City).join(State, onclause=City.state_id == State.id)
    results = session.execute(query).fetchall()

    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")
