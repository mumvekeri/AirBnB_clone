#!/usr/bin/python3
"""Creates a console class"""

import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """A command interpreter for the HBNB project"""

    prompt = "(hbnb) "  # a custom prompt
    classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def do_EOF(self, arg):
        """Exit the program"""
        print()
        return True

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_help(self, arg):
        """Show help for the available commands"""
        print("Available commands:")
        print("\tcreate <class_name>: Create a new instance of a class")
        print("\tshow <class_name> <id>: Show the string representation of an instance")
        print("\tdestroy <class_name> <id>: Delete an instance")
        print("\tupdate <class_name> <id> <attribute_name> <value>: Update an attribute of an instance")
        print("\tall [<class_name>]: Print all string representations of instances")
        print("\tcount <class_name>: Count the number of instances of a class")
        print("\tquit: Exit the program")
        print("\thelp: Show this help message")

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()

