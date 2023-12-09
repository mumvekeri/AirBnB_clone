#!/usr/bin/python3
"""This is a module that creates a file storage class"""

import json
import re

class FileStorage:
    """
    Class for storing and retrieving objects from a JSON file.
    """

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        self.reload()  # Load objects from JSON file on initialization

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, "w") as file:
            json.dump(self.__objects, file)

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)
        except FileNotFoundError:
            pass  # No need to raise an error if the file doesn't exist

