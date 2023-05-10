#!/usr/bin/python3
"""The Base Model Class"""


import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """All other classes inherit from the here"""

    def __init__(self, *args, **kwargs):
        """Initialization of instance attributes

        Args:
            args - list of arguments
            **kwargs - dict of key/value pair arguments
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:S.%f")
                else:
                    self.id = str(uuid.uuid4())
                    self.created_at = datetime.now()
                    self.updated_at = datetime.now()
                    storage.new(self)

    def __str__(self):
        """Returns string representation"""
        return "[{}] ({}) ({})"\
            .format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
