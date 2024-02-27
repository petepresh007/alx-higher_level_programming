#!/usr/bin/python3
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """ City Table inherits model"""
    __tablename__ = "cities"
    id = Column(Integer, nullable=False, unique=False,
                autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
