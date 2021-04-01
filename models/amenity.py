#!/usr/bin/python3
""" State Module for HBNB project """


import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.place import place_amenity
from os import getenv


class Amenity(BaseModel):

    """ A place to stay """
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)
