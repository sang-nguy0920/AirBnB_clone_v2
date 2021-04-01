#!/usr/bin/python3
""" Database storage using MySQLAlchemy """

import sqlalchemy
import os
from os import getenv
import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, scoped_session
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

cdict = {
    'BaseModel': BaseModel,
    'User': User,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Place': Place,
    'Review': Review}


class DBStorage():

    """inits session"""
    __engine = None
    __session = None

    user = getenv('HBNB_MYSQL_USER')
    password = getenv('HBNB_MYSQL_PWD')
    host = getenv('HBNB_MYSQL_HOST')
    database = getenv('HBNB_MYSQL_DB')

    def __init__(self):
        """ creates the engine """

        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                                      .format("hbnb_dev",
                                              "hbnb_dev_pwd",
                                              "hbnb_dev_db"),
                                      pool_pre_ping=True)
        Session = sessionmaker(bind=self.__engine)
        session = Session()
        return (None)

        if (hbnb_test):
            cur = self.__engine.cursor()
            cur.execute("DROP TABLES")

    def all(self, cls=None):
        """ returns a dictionary of databases """
        db_dict = {}
        if cls is not None:
            for instance in self.__session.query(cdict[cls]).all():
                db_dict[cdict[cls].__name__ + "." + cdict[cls].id] = instance
            return db_dict
        else:
            for i in cdict:
                find = self.__session.query(cdict[i]).all()
                for y in find:
                    db_dict[
                        instance.__class__.__name__ +
                        "." +
                        instance.id] = instance
            return db_dict

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
        self.__session.add(obj)

    def save(self):
        """ commit changes of current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current db session obj if not none """
        if obj:
            self.__session.delete()

    def reload(self):
        """ create all tables in the database """
        from models.base_model import BaseModel, Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        Base.metadata.create_all(self.__engine)

<<<<<<< HEAD
        self.__session = scoped_session(sessionmaker(bind=self.__engine))
=======
        sesh = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(sesh)
>>>>>>> bb6e05f50880146279a8da6f08fca76c58bb2ac6
