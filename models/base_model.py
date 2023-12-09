#!/usr/bin/python3
"""Trying out"""

import uuid
from datetime import datetime
from .engine import file_storage


class BaseModel:
    """
    Base class for all other models.
    """

    def __init__(self, *args, **kwargs):
        if kwargs:
            self.id = kwargs.pop("id", str(uuid.uuid4()))
            self.created_at = datetime.fromisoformat(kwargs.pop("created_at"))
            self.updated_at = datetime.fromisoformat(kwargs.pop("updated_at"))
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        return f"[<{self.__class__.__name__}>] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        dict_repr = self.__dict__.copy()
        dict_repr.update({
            "__class__": self.__class__.__name__,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        })
        return dict_repr

