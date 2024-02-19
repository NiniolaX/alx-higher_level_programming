#!/usr/bin/python3
"""This module contains a class City which links to a MySQL database table
'cities'.

Classes:
    City: Links to the table 'cities' of a MySQL database.

Attributes:
    None

Functions:
    None
"""

from model_state import Base, State
from sqlalchemy import create_engine, Integer, String, Column, ForeignKey


class City(Base):
    """This class links to the table 'cities' of a MySQL database.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('State.id'))
