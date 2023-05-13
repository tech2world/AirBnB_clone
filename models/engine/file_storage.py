#!/usr/bin/python3
"""A class that serializes instances to a JSON file and
    deserializes JSON file to instances"""

import json
import os.path
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """This class serializes instances to a JSON file and deserializes JSON
    file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of all objects"""
        if cls is None:
            return self.__objects
        else:
            return {key: obj for key, obj in self.__objects.items()
                    if type(obj) == cls}

    def new(self, obj):
        """Sets __objects with the obj"""
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)
                for key, val in obj_dict.items():
                    cls_name = key.split('.')[0]
                    if cls_name == 'BaseModel':
                        self.__objects[key] = BaseModel(**val)
                    elif cls_name == 'User':
                        self.__objects[key] = User(**val)
                    elif cls_name == 'State':
                        self.__objects[key] = State(**val)
                    elif cls_name == 'City':
                        self.__objects[key] = City(**val)
                    elif cls_name == 'Amenity':
                        self.__objects[key] = Amenity(**val)
                    elif cls_name == 'Place':
                        self.__objects[key] = Place(**val)
                    elif cls_name == 'Review':
                        self.__objects[key] = Review(**val)
