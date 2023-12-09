#!/usr/bin/python3
"""This is a file storage class"""

import json
import re
import sys
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """A class that handles file storage"""

    __file_path = "file.json" # the path to the JSON file
    __objects = {}

    models.classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

    def all(self, cls=None):
        """Returns the dictionary __objects"""
        if cls is None:
            return FileStorage.__objects
        elif isinstance(cls, str):
            if cls in FileStorage.classes:
                cls = FileStorage.classes[cls]  # get the class object
            else:
                return {}
            return {key: obj for key, obj in FileStorage.__objects.items() if isinstance(obj, cls)}

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id as it should be"""
        if obj is not None:
            key = obj._class.__name_ + "." + obj.id
            FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        result = {}
        for key, obj in FileStorage.__objects.items():
            result[key] = obj.to_dict()
            with open(FileStorage.__file_path, "w") as f:
                json.dump(result, f)

    def count(self, cls=None):
        """Count the number of objects of a specific class"""
        if cls is not None and cls in FileStorage.classes:
            return sum(1 for obj in FileStorage.__objects.values() if isinstance(obj, FileStorage.classes[cls]))
        else:
            return len(FileStorage.__objects)
          
    def reload(self):
        """Deserializes the JSON file to objects"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                json_dict = json.load(f)
                for key, value in json_dict.items():
                    class_name = value["_class_"]
                    cls = _import("models").__dict_[class_name]
                    obj = cls(**value)
                    FileStorage.__objects[key] = obj
        
        except FileNotFoundError:
            pass
