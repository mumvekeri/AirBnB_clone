#!/usr/bin/python3
"""This module creates a base model class"""

from uuid import uuid4
from datetime import datetime
import models
import storage

class BaseModel:
    """A base class for other classes"""

    def _init_(self, *args, **kwargs):
        """Initialize a new instance"""
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "_class":
                    continue
                elif key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
                else:
                    self.id = str(uuid4())
                    self.created_at = datetime.now()
                    self.updated_at = self.created_at
                    storage.new(self)
        self.class = self.__class_

    def _str_(self):
        """Return a string representation of the instance"""
        return "[{}] ({}) {}".format(self.class.__name, self.id, self.__dict_)

    def save(self):
        """Update the updated_at attribute with the current datetime and save it"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance"""
        result = self._dict_.copy()
        result["class"] = self.__class.__name_
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result
