#!/usr/bin/python3

"""Importing storage variable"""

from os import getenv
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
# from models.engine.db_storage import DBStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import sqlalchemy



cdict = {
    'BaseModel': BaseModel,
    'User': User,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Place': Place,
    'Review': Review}

if getenv('HBNB_TYPE_STORAGE') == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()

else:
    storage = FileStorage()
    storage.reload()
