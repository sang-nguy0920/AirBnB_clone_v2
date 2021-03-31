#!/usr/bin/python3
""" State Module for HBNB project """

import models
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete-orphan")
    else:
        name = ""
        @property
        def cities(self):
            instance_state = []
            for key, obj in models.storage.all().items():
                if obj.__class__.__name__ == 'City':
                    if obj.state_id == self.id:
                        instance_state.append(obj)
            return instance_state
