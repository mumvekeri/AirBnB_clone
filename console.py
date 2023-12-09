#!/usr/bin/python3
"""Creates a console class"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Class to handle the command interpreter.
    """

    intro = "Welcome to the HBNB command interpreter!"
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit the command interpreter."""
        print("Quitting...")
        exit()

    def do_EOF(self, args):
        """Quit using EOF."""
        print("Quitting...")
        exit()

    def do_help(self, args):
        """Show help for available commands."""
        print(cmd.Cmd.do_help(self, args))

    def emptyline(self):
        """Do nothing when the user enters an empty line."""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it and prints the id."""
        args = parse_args(args)
        try:
            if not args.class_name:
                raise Exception("class name missing")
            if not hasattr(storage.all(), args.class_name):
                raise Exception("class doesn't exist")
            new_instance = eval(args.class_name)()
            new_instance.save()
            print(new_instance.id)
        except Exception as e:
            print(e)

    def do_show(self, args):
        """Prints the string representation of an instance."""
        args = parse_args(args)
        try:
            if not args.class_name:
                raise Exception("class name missing")
            if not hasattr(storage.all(), args.class_name):
                raise Exception("class doesn't exist")
            if not args.id:
                raise Exception("instance id missing")
            instance = storage.get(args.class_name, args.id)
            if not instance:
                raise Exception("no instance found")
            print(instance)
        except Exception as e:
            print(e)

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id."""
        args = parse_args(args)
        try:
            if not args.class_name:
                raise Exception("class name missing")
            if not hasattr(storage.all(), args.class_name):
                raise Exception("class doesn't exist")
            if not args.id:
                raise Exception("instance id missing")
            instance = storage.get(args.class_name, args.id)
            if not instance:
                raise Exception("no instance found")
            storage.delete(instance)
            storage.save()
            print("Deleted")
        except Exception as e:
            print(e)

    def do_all(self, args):
        """Prints all string representation of all instances."""
        args = parse_args(args)
        results = []
        try:
            if args.class_name and not hasattr(storage.all(), args.class_name):
                raise Exception("class doesn't exist")
            for key, value in storage.all().items():
                if not args.class_name or key == args.class_name:
                    results.append

if __name__ == '__main__':
    HBNBCommand().cmdloop()

