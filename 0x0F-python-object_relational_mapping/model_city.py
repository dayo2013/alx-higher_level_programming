#!/usr/bin/python3
"""
Class definition of a City
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State
from sqlalchemy.ext.declarative import declarative_base

class City(Base):
    """
    City class that inherits from Base
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
