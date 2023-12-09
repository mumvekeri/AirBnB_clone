#!/usr/bin/python3
"""Creates a console class"""

import cmd
import shlex
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

    prompt = "(hbnb) "  # a custom prompt
    classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def do_quit(self, arg):
        """Quit command to exit the prompt"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Create command to create a new instance of a class"""
        args = shlex.split(arg)

        if not args:
            print("** class name missing **")
        elif len(args) > 1:
            print("** too many arguments **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            cls_name = args[0]
            cls = globals()[cls_name]
            obj = cls()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """Show command to print the string representation of an instance"""
        args = shlex.split(arg)

        if not args:
            print("** class name missing **")
        elif len(args) != 2:
            print("** invalid arguments **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            class_name, instance_id = args
            key = class_name + "." + instance_id
            objects = storage.all()
            if key not in objects:
                print("** no instance found **")
            else:
                print(objects[key])

    def do_destroy(self, arg):
        """Destroy command to delete an instance based on the class name and id"""
        args = shlex.split(arg)

        if not args:
            print("** class name missing **")
        elif len(args) != 2:
            print("** invalid arguments **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            class_name, instance_id = args
            key = class_name + "." + instance_id
            objects = storage.all()
            if key not in objects:
                print("** no instance found **")
            else:
                del objects[key]
                storage.save()

    def do_update(self, arg):
        """Update command to update an instance based on the class name and id"""
        args = shlex.split(arg)

        if not args:
            print("** class name missing **")
        elif len(args) < 4 or len(args) > 5:
            print("** invalid arguments **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            class_name, instance_id, attribute_name, value = args[:4]
            key = class_name + "." + instance_id
            objects = storage.all()

            if key not in objects:
                print("** no instance found **")
            else:
                obj = objects[key]
                try:
                    # Check for valid attribute name
                    if not hasattr(obj, attribute_name):
                        print("** no attribute found **")
                        return

                    # Cast value to attribute type
                    value = type(getattr(obj, attribute_name))(value)
                    setattr(obj, attribute_name, value)
                    obj.save()
                except ValueError:
                    print("** invalid value **")
                    return

    def do_all(self, arg):
        """All command to print all string representation of all instances"""
        args = shlex.split(arg)

        if not args:
            pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

