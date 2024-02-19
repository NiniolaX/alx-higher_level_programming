#!/usr/bin/python3
"""This script lists all State objects that contain the letter 'a' from the
database hbtn_0e_6_usa (will be passed via the cmd line).
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

    results = session.query(State).filter(State.name.like('%a%')).all()
    for row in results:
        print(f"{row.id}: {row.name}")
