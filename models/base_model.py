#!/usr/bin/python3
"""This module creates a base model class"""

from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """A base class for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "_class":
                    continue
                elif key in ("created_at", "updated_at"):
                    # Convert string dates to datetime objects
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """Return a string representation of the instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the updated_at attribute and save object"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance"""
        result = self.__dict__.copy()
        result["_class"] = self.__class__.__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result


