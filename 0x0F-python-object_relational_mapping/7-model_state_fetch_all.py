#!/usr/bin/python3
"""This script lists all State objects from a specified database.
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database
    results = session.query(State).all()

    # Display results
    for row in results:
        print(f"{row.id}: {row.name}")
