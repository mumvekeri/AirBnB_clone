#!/usr/bin/python3
"""Trying out"""

import uuid
from datetime import datetime
from .engine import file_storage
import storage

class BaseModel:
    """
    Base class for all other models.
    """

    storage = file_storage.storage

    def __init__(self, *args, **kwargs):
        if kwargs:
            self.id = kwargs.pop("id", str(uuid.uuid4()))
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.storage.new(self)

    def __str__(self):
        return f"[<{self.__class__.__name__}>] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        self.storage.save()

    def to_dict(self):
        dict_repr = self.__dict__.copy()
        dict_repr["__class__"] = self.__class__.__name__
        dict_repr["created_at"] = self.created_at.isoformat()
        dict_repr["updated_at"] = self.updated_at.isoformat()
        return dict_repr

storage.reload()

