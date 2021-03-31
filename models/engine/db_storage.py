#!/usr/bin/python3
""" Database storage using MySQLAlchemy """

import sqlalchemy
import os
from os import getenv
import sys
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


class DBStorage():
    """inits session"""
    __engine = None
    __session = None
    # user = os.environ('HBNB_MYSQL_USER')
    # password = os.environ('HBNB_MYSQL_PWD')
    # host = os.environ('HBNB_MYSQL_HOST')
    # database = os.environ('HBNB_MYSQL_DB')
    

    def __init__(self):
        """ creates the engine """

        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format("hbnb_dev", "hbnb_dev_pwd", "hbnb_dev_db"), pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        return (None)

        if (hbnb_test):
            cur = engine.cursor()
            cur.execute("DROP TABLES")

    def all(self, cls=None):
        """ returns a dictionary of databases """
        if not cls:
            for instance in self.__session.query().all():
                return self.__session
        if cls == "State":
            for instance in self.__session.query(State).all():
                return self.__session
        if cls == "City":
            for instance in self.__session.query(City).all():
                return self.__session
        if cls == "User":
            for instance in self.__session.query(User).all():
                return self.__session
        if cls == "Amenity":
            for instance in self.__session.query(Amenity).all():
                return self.__session
        if cls == "Place":
            for instance in self.__session.query(Place).all():
                return self.__session
        if cls == "Review":
            for instance in self.__session.query(Review).all():
                return self.__session

    def new(self, obj):
        """ add the object to the current db session """
        self.__session.all().update()

    def save(self):
        """ commit changes of current database session """
        self.__session.add()
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current db session obj if not none """
        if obj:
            self.__session.delete()

    def reload(self):
        """ create all tables in the database """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        # Base.metadata.create_all(engine)

        self.__session = scoped_session(sessionmaker(bind=engine), expire_on_commit=False)
