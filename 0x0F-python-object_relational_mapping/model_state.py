#!/usr/bin/python3
"""This file contains the class definition of a State which links to the MySQL
database table states.

Classes:
    Base: An instance of SQLAlchemy declarative base from which other classes
          inherit
    State: Class which inherits from Base and links to the 'states' table of a
          MySQL database

Functions:
    None

Attributes:
    None
"""

from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Links to the states table of a MySQL database.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
