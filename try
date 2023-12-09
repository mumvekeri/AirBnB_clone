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
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            cls_name = arg  # Get the class name directly
            cls = globals()[cls_name]
            obj = cls()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """Show command to print the string representation of an instance"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
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
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
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
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** dictionary missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            key = class_name + "." + instance_id
            objects = storage.all()
            if key not in objects:
                print("** no instance found **")
            else:
                obj = objects[key]
                try:
                    attr_dict = json.loads(' '.join(args[2:]))
                except:
                    print("** invalid dictionary format **")
                    return

                if not isinstance(attr_dict, dict):
                    print("** invalid dictionary format **")
                    return

                for key, value in attr_dict.items():
                    setattr(obj, key, value)

                obj.save()

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
            class_name = arg
            objects = storage.all(class_name)
            result = []
            for obj in objects.values():
                result.append(str(obj))
            print(result)

    def default(self, line):
        """Called on an input line when the command prefix is not recognized."""
        args = shlex.split(line)
        if len(args) >= 2 and args[0] in HBNBCommand.classes:
            command = args[1] if args[1] in ["all", "show", "destroy", "update"] else ""
            if command:
                getattr(self, "do_" + command)(args[0] + " " + ' '.join(args[2:]))
            else:
                print("** command not recognized **")
        else:
            print("** command not recognized **")

    def do_count(self, arg):
        """Count command to print the number of instances of a class"""
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            class_name = arg
            count = storage.count(class_name)
            print("There are {} instances of {}".format(count, class_name))

if __name__ == '__main__':
    HBNBCommand().cmdloop()

