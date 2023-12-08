#!/usr/bin/python3
"""Creates a console class"""

import cmd
import re
import json
import sys
import models
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

    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        print()
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def help_quit(self):
        """Show the help message for quit command"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Show the help message for EOF command"""
        print("EOF command to exit the program")

    def do_create(self, arg):
        """Create command to create a new instance of a class"""
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            cls = eval(arg)
            obj = cls()
            obj.save()
            print(obj.id)
    def help_create(self):
        """Show the help message for create command"""
        print("Create command to create a new instance of a class")
        print("Usage: create <class name>")

    def do_show(self, arg):
        """Show command to print the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            objects = storage.all()
            if key not in objects:
                print("** no instance found **")
            else:
                print(objects[key])

    def help_show(self):
        """Show the help message for show command"""
        print("Show command to print the string representation of an instance")
        print("Usage: show <class name> <id>")

    def do_destroy(self, arg):
        """Destroy command to delete an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            objects = storage.all()
            if key not in objects:
                print("** no instance found **")
            else:
                del objects[key]
                storage.save()

    def help_destroy(self):
        """Show the help message for destroy command"""
        print("Destroy command to delete an instance based on the class name and id")
        print("Usage: destroy <class name> <id>")

    def do_all(self, arg):
        """All command to print all string representation of all instances"""
        if not arg:
            objects = storage.all()
            result = []
            for obj in objects.values():
                result.append(str(obj))
            print(result)
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            objects = storage.all(arg)
            result = []
            for obj in objects.values():
                result.append(str(obj))
            print(result)

    def help_all(self):
        """Show the help message for all command"""
        print("All command to print all string representation of all instances")
        print("Usage: all <class name> (optional)")

    def do_update(self, arg):
        """Update command to update an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            objects = storage.all()
            if key not in objects:
                print("** no instance found **")
            else:
                obj = objects[key]
                attr = args[2]
                value = args[3]
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                try:
                    value = eval(value)
                except:
                    pass
                if attr not in ["id", "created_at", "updated_at"]:
                    setattr(obj, attr, value)
                obj.save()

    def help_update(self):
        """Show the help message for update command"""
        print("Update command to update an instance based on the class name and id")
        print("Usage: update <class name> <id> <attribute name> \"<attribute value>\"")

    def do_BaseModel(self, arg):
        """BaseModel command to retrieve all instances of BaseModel or
        the number of instances or an instance based on its ID"""
        if arg == "all":
            objects = storage.all("BaseModel")
            for obj in objects.values():
                print(obj)
        elif arg == "count":
            objects = storage.all("BaseModel")
            print(len(objects))
        elif arg.startswith("show"):
            id = arg[5:-1]
            obj = storage.show("BaseModel", id)
            if obj is None:
                print("** no instance found **")
            else:
                print(obj)
        else:
            print("Invalid argument")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
