#!/usr/bin/python3
"""Creates a console class"""

import cmd
import re
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage

class HBNBCommand(cmd.Cmd):
    """A command interpreter for the HBNB project"""

    prompt = "(hbnb) " # a custom prompt
    classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
