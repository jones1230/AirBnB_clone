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

    def do_EOF(self, line):
        """ Exit the CLI on EOF command. """
        return True

    def do_quit(self, line):
        """ Exit the CLI on quit command. """
        return self.do_EOF(line)


if __name__ == '__main__':
    """ Start the CLI. """
    HBNBCommand().cmdloop()
