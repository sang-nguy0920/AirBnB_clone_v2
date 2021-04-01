#!/usr/bin/python3
""" State Module for HBNB project """

import models
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, DateTime, Table, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):

    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="delete", backref='State')
