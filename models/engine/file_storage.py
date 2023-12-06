#!/usr/bin/python3
"""This is a module that is going to create a file storage class"""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """A class that serializes and deserializes instances to and from a JSON file"""

    __file_path = "file.json" # the path to the JSON file
    __objects = {} # a dictionary to store all objects by <class name>.id
    classes = {"BaseModel": BaseModel, "User": User, "Place": Place, "State": State, "City": City, "Amenity": Amenity, "Review": Review}

    def all(self, cls=None):
        """Returns the dictionary __objects"""

        if cls is None: # if no class is specified, return all objects
            return FileStorage.__objects
        elif isinstance(cls, str): # if cls is a class name
            if cls in FileStorage.classes: # if the class name is valid
                cls = FileStorage.classes[cls] # get the class object
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
            result[key] = obj.to_dict() # convert the obj to a dictionary and store it
        with open(FileStorage.__file_path, "w") as f:
            json.dump(result, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists)"""
        try:
            with open(FileStorage.__file_path, "r") as f: # open the file in read mode
                result = json.load(f)
            for key, value in result.items():
                if value["_class_"] in FileStorage.classes:
                    cls = FileStorage.classes[value["_class_"]]
                    obj = cls(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
