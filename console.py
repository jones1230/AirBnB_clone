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


class HBNBCommand(cmd.Cmd):
    """
    CLI for the AirBnB Clone Console.

    Attributes:
        prompt (str): CLI prompt displayed to the user.
    """
    prompt = "(hbnb) "

    @staticmethod
    def do_EOF(line):
        """ Exit the CLI on EOF command. """
        return True

    @staticmethod
    def do_quit(line):
        """ Exit the CLI on quit command. """
        return True

    def emptyline(line):
        return False

    def do_create(self, line):
        valid_classes = storage.classes()
        if line in valid_classes:
            temp = valid_classes[line]()
            temp.save()
            print(temp.id)
        elif line == "":
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        if line == "" or line is None:
            print("** class name missing")
        else:
            words = line.split()
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        if line == "" or line is None:
            print("** class name missing")
        else:
            words = line.split()
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        if line != "":
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                nl = [str(obj) for key, obj in storage.all().items()
                      if type(obj).__name__ == words[0]]
                print(nl)
        else:
            new_list = [str(obj) for key, obj in storage.all().items()]
            print(new_list)

    def do_update(self, line):
        if not line:
            print("** class name missing **")
            return

        args = line.split()
        if len(args) < 1:
            print("** class name missing **")
            return

        classname = args[0]
        if classname not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        uid = args[1]
        key = "{}.{}".format(classname, uid)
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        value = " ".join(args[3:])
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
        else:
            try:
                value = float(value) if '.' in value else int(value)
            except ValueError:
                pass

        instance = storage.all()[key]
        if hasattr(instance, attribute):
            attr_type = type(getattr(instance, attribute))
            value = attr_type(value)

        setattr(instance, attribute, value)
        instance.save()


if __name__ == '__main__':
    """ Start the CLI. """
    try:
        HBNBCommand().cmdloop()
    except KeyboardInterrupt:
        print('Session Ended!')
