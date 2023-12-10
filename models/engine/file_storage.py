#!/usr/bin/python3
"""This is a module that creates a file storage class"""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """
    Represents an abstraction for persistent data storage.

    Attributes:
        _file_path (str): The name of the file to store objects.
        _objects (dict): A dictionary of instantiated objects.
    """

    _file_path = "file.json"
    _objects = {}

    def all(self):
        """
        Returns the dictionary containing all stored objects.
        """
        return self._objects

    def new(self, obj):
        """
        Adds a new object to the storage dictionary.

        Args:
            obj: The object to be stored.
        """
        object_class_name = obj.__class__.__name__
        key = f"{object_class_name}.{obj.id}"
        self._objects[key] = obj

    def save(self):
        """
        Serializes the stored objects to a JSON file.
        """
        object_dict = {obj: self._objects[obj].to_dict() for obj in self._objects.keys()}
        with open(self._file_path, "w") as f:
            json.dump(object_dict, f)

    def reload(self):
        """
        Loads objects from a JSON file if it exists.

        Raises:
            FileNotFoundError: If the file does not exist.
        """
        try:
            with open(self._file_path) as f:
                object_dict = json.load(f)
                for data in object_dict.values():
                    class_name = data["__class__"]
                    del data["__class__"]
                    self.new(eval(class_name)(**data))
        except FileNotFoundError:
            pass
