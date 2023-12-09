#!/usr/bin/python3
"""This module creates a base model class"""

from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """A base class for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance"""

        if kwargs is not None:  # Use 'is not None' to check if kwargs is not empty
            for key, value in kwargs.items():
                if key == "_class":
                    continue
                elif key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
                else:
                    self.id = str(uuid.uuid4())
                    self.created_at = datetime.now()
                    self.updated_at = self.created_at
                    storage.new(self)

    def __str__(self):
        """Return a string representation of the instance"""
        return "[{}] ({}) {}".format(self._class.__name, self.id, self.__dict__)

    def save(self):
        """Update the updated_at attribute with the current datetime and save it"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance"""
        result = self.__dict__.copy()
        result["_class"] = self.__class__.__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result

