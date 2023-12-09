#!/usr/bin/python3
"""This is a module that creates a file storage class"""

import json
from models.base_model import BaseModel

class FileStorage:
    """
    File Storage class for BaseModel
    """

    _file_path = "file.json"
    _objects = {}

    def all(self):
        """Returns all objects"""
        return self._objects

    def new(self, obj):
        """Adds a new object to the storage"""
        self._objects[obj.id] = obj

    def save(self):
        """Saves all objects to a JSON file"""
        with open(self._file_path, "w") as f:
            json.dump(self._objects, f)

    def reload(self):
        """Loads all objects from a JSON file"""
        try:
            with open(self._file_path, "r") as f:
                self._objects = json.load(f)
        except FileNotFoundError:
            pass

    def get(self, cls, id):
        """
        Returns an object based on its class and ID
        """
        key = "{}.{}".format(cls.__name__, id)
        return self._objects.get(key)

    def delete(self, obj):
        """
        Deletes an object from the storage
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        del self._objects[key]

