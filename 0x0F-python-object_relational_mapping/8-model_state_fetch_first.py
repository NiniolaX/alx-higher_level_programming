#!/usr/bin/python3
"""This script prints the first State object in the database hbtn_0e_6_usa.
(hbtn_0e_6_usa is passed to the script from the cmd line)
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
    first_obj = session.query(State).first()

    if first_obj:
        print(f"{first_obj.id}: {first_obj.name}")
    else:
        print("Nothing")
