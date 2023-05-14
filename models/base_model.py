#!/usr/bin/python3
"""The Base Model Class"""


import uuid
from datetime import datetime
import models


class BaseModel:
    """Base class for other classes to inherit from"""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)
            self.id = str(uuid.uuid4())
            time = datetime.now()
            self.created_at = self.updated_at = time
        else:
            self.id = str(uuid.uuid4())
            time = datetime.now()
            self.created_at = self.updated_at = time
            models.storage.new(self)

    def __str__(self):
        """Return string representation of BaseModel"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update BaseModel with the current time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return dictionary representation of BaseModel"""
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        if "_sa_instance_state" in my_dict:
            del my_dict["_sa_instance_state"]
        return my_dict

    @classmethod
    def dict_to_instance(cls, dictionary):
        """Creates an instance of the class from a dictionary"""
        instance = cls()
        for key, value in dictionary.items():
            if key != '__class__':
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(instance, key, value)
        return instance
