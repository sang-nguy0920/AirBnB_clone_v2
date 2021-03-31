#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from models.engine import file_storage
from sqlalchemy import Column, String, Integer, DateTime, Table, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""


#        if (len(kwargs) == 0):
 #           self.id = Column(String(60), (uuid.uuid4()), nullable=False, primary_key=True)
  #          self.created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
   #         self.updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    #    else:
        try:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                 '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                 '%Y-%m-%dT%H:%M:%S.%f')
        except KeyError:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now() 
            self.updated_at = datetime.now()

        for key, value in kwargs.items():
            if "__class__" not in key:
                setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        cdict = __self.__dict__
        if '_sa_instance_state' in cdict:
            del cdict['_sa_instance_state']

        cdict['__class__'] = self.__class__.__name__
        cdict['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        cdict['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
          
        return cdict

    def delete(self):
        """ Delete an instance """
        models.storage.delete(self)
