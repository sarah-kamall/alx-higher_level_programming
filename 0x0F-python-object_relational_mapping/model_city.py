#!/usr/bin/python3
"""class definition of a City and an instance Base"""
from sqlalchemy import Column, Integer, String, MetaData, ForeignKey
from model_state import Base
from sqlalchemy.orm import relationship


class City(Base):
    """
    Class with id and name attributes of each City
    """
    __tablename__ = "cities"
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
