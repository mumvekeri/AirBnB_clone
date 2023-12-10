#!/usr/bin/python3
"""
creates a file class storage
"""
import json
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    class FileStorage class
    private class attributes:
        __file_path(str): path to the JSON file
        __objects(dict): will store all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}
    classes = {
        "BaseModel": BaseModel,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
        "User": User,
    }

    def all(self, cls=None):
        """
        returns the dictionary containing all objects.
        """
        if cls is None:
            return self.__objects
        elif cls.__name__ in self.classes:
            return {
                k: v for k, v in self.__objects.items() if isinstance(v, cls)
            }
        else:
            return {}

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{str(obj.id)}"
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file.
        """
        with open(self.__file_path, "w", encoding="UTF-8") as f:
            json.dump(self.__objects, f, indent=4)

    def reload(self):
        """
        deserializes the JSON file to __objects.
        """
        try:
            with open(self.__file_path, "r") as f:
                new_dict = json.load(f)
            for key, value in new_dict.items():
                base = self.classes[value["__class__"]](**value)
                self.__objects[key] = base
        except FileNotFoundError:
            pass

    def count(self, cls=None):
        """
        Returns the number of objects of a specific class or
        the total number of objects if cls is None.
        """
        if cls is not None and cls.__name__ in self.classes:
            return sum(
                1 for obj in self.__objects.values() if isinstance(obj, cls)
            )
        else:
            return len(self.__objects)

