#!/usr/bin/python3
"""Module for defining class of sqlalchemy
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ class for state to define base
    """
    __tablename__ = "states"
    id = Column(Integer,
                unique=True,
                nullable=False,
                autoincrement=True,
                primary_key=True)
    name = Column(String(128), nullable=False)
