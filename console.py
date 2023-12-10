#!/usr/bin/python3
"""
module console class
contains the entry point to the command interpreter
"""

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage

class HBNBCommand(cmd.Cmd):
    """Shell for the HBNB project."""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exit the command interpreter."""
        return True

    def do_quit(self, line):
        """Exit the command interpreter."""
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it and prints the id."""
        args = line.split()

        if not args:
            print("** class name missing **")
            return

        if args[0] not in storage.all():
            print("** class doesn't exist **")
            return

        new_obj = eval(args[0])()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id."""
        args = line.split()

        if not args:
            print("** class name missing **")
            return

        if args[0] not in storage.all():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]

        try:
            obj = storage.get(args[0], obj_id)
        except Exception:
            obj = None

        if not obj:
            print("** no instance found **")
            return

        print(obj)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id."""
        args = line.split()

        if not args:
            print("** class name missing **")
            return

        if args[0] not in storage.all():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]

        try:
            obj = storage.get(args[0], obj_id)
        except Exception:
            obj = None

        if not obj:
            print("** no instance found **")
            return

        storage.delete(obj)
        storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name."""
        args = line.split()

        if args and args[0] not in storage.all():
            print("** class doesn't exist **")
            return

        obj_list = storage.all() if not args else storage.all(args[0])

        for obj in obj_list:
            print(obj)

    def do_update(self, line):
        """Updates an instance based on the class name and id."""
        args = line.split()

        if not args:
            print("** class name missing **")
            return

        if args[0] not in storage.all():
            print("** class doesn't exist **")
            return

        if len(args) < 4:
            if len(args) == 2:
                print("** instance id missing **")
            elif len(args) == 3:
                print("** attribute name missing **")
            else:
                print("** value missing **")
            return

        obj_id = args[1]
        attr_name = args[2]
        attr_value = eval(args[3])

        if attr_name in ("id", "created_at", "updated_at"):
            print("** can't update this attribute **")
            return

        try:
            obj = storage.get(args[0], obj_id)
        except Exception:
            obj = None

        if not obj:
            print("** no instance found **")
            return

        setattr(obj, attr_name, attr_value)
        obj.save()
        storage.save()

    def emptyline(self):
        """Pass on empty lines."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
