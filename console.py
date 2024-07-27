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


if __name__ == '__main__':
    """ Start the CLI. """
    try:
        HBNBCommand().cmdloop()
    except KeyboardInterrupt:
        print('Session Ended!')
