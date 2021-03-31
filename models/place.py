#!/usr/bin/python3
""" Place Module for HBNB project """

import models
from models.base_model import BaseModel
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from os import getenv

class Place(BaseModel):

    """ A place to stay """
    __tablename__ = 'places'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), nullable=False, ForeignKey('cities.id'))
        user_id = Column(String(60), nullable=False, ForeignKey('users.id'))
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        city_id = Column(String(60), nullable=False, ForeignKey('cities.id'))
        city_id = Column(String(60), nullable=False, ForeignKey('cities.id'))
        city_id = Column(String(60), nullable=False, ForeignKey('cities.id'))
        city_id = Column(String(60), nullable=False, ForeignKey('cities.id'))
        city_id = Column(String(60), nullable=False, ForeignKey('cities.id'))
        city_id = Column(String(60), nullable=False, ForeignKey('cities.id'))

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
