#!/usr/bin/python3
"""
This module defines a simple command-line interface (CLI) for the AirBnB
Clone Console project.

The `HBNBCommand` class is a subclass of `cmd.Cmd` that provides a basic
interactive prompt for user input. It supports basic commands such as
`EOF` (End Of File) and `quit` to exit the CLI.

Imports:
    - cmd: The standard library module for creating command-line
        interfaces.
"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    CLI for the AirBnB Clone Console.

    Attributes:
        prompt (str): CLI prompt displayed to the user.
    """
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exit the CLI on EOF command."""
        print()
        return True

    def do_quit(self, line):
        """Exit the CLI on quit command."""
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_create(self, line):
        """Create a new instance of BaseModel and print its id."""
        if not line:
            print("** class name missing **")
            return
        try:
            new_instance = eval(line)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Show the string representation of an instance."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, line):
        """Delete an instance based on class name and id."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, line):
        """Print all string representations of all instances."""
        args = line.split()
        if args and args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        objects = storage.all()
        obj_list = []
        if args:
            for key, obj in objects.items():
                if key.startswith(args[0] + '.'):
                    obj_list.append(str(obj))
        else:
            for obj in objects.values():
                obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, line):
        """Update an instance based on class name and id."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        instance = storage.all()[key]
        attr_name = args[2]
        attr_value = args[3]
        try:
            attr_type = type(getattr(instance, attr_name))
            attr_value = attr_type(attr_value)
        except AttributeError:
            pass
        setattr(instance, attr_name, attr_value)
        instance.save()

    def default(self, line):
        command = line.split('.')
        if len(command) == 2 and command[1] == "all()":
            if command[0] in storage.classes() and command[1] == "all()":
                self.do_all(command[0])
            else:
                print("** class doesn't exist **")
        else:
            print("** invalid command **")


if __name__ == '__main__':
    """Start the CLI."""
    HBNBCommand().cmdloop()
