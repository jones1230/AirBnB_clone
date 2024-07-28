import cmd
from models.base_model import BaseModel
from models import storage
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

        # Convert the attribute value to the correct type if possible
        if hasattr(instance, attr_name):
            attr_type = type(getattr(instance, attr_name))
            try:
                attr_value = attr_type(attr_value)
            except ValueError:
                pass  # Keep it as a string if conversion fails

        setattr(instance, attr_name, attr_value)
        instance.save()

    def default(self, line):
        """Handle default case where command is not recognized."""
        command = line.split('.')
        if len(command) == 2:
            if command[1] == "all()":
                self.handle_all(command[0])
            elif command[1] == "count()":
                self.handle_count(command[0])
            elif command[1].startswith("show(") and command[1].endswith(")"):
                self.handle_show(command[0], command[1][5:-1])
            elif command[1].startswith("destroy("
                                       ) and command[1].endswith(")"):
                self.handle_destroy(command[0], command[1][8:-1])
            elif command[1].startswith("update(") and command[1].endswith(")"):
                self.handle_update(command[0], command[1][7:-1])
            else:
                print("** invalid command **")
        else:
            print("** invalid command **")

    def handle_all(self, class_name):
        """Handle all() command for a class."""
        if class_name in storage.classes():
            self.do_all(class_name)
        else:
            print("** class doesn't exist **")

    def handle_count(self, class_name):
        """Handle count() command for a class."""
        if class_name in storage.classes():
            instances = storage.all()
            counts = sum(1 for key in instances
                         if key.startswith(class_name + '.'))
            print(counts)
        else:
            print("** class doesn't exist **")

    def handle_show(self, class_name, instance_id):
        """Handle show() command for a class and instance id."""
        if class_name in storage.classes():
            key = "{}.{}".format(class_name, instance_id)
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def handle_destroy(self, class_name, instance_id):
        """Handle destroy() command for a class and instance id."""
        if class_name in storage.classes():
            key = "{}.{}".format(class_name, instance_id)
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def handle_update(self, class_name, params):
        """Handle update() command for a class and parameters."""
        if class_name in storage.classes():
            if params.startswith('{') and params.endswith('}'):
                self.handle_dict_update(class_name, params)
            else:
                self.handle_single_update(class_name, params.split(', '))
        else:
            print("** class doesn't exist **")

    def handle_dict_update(self, class_name, params):
        """Handle dictionary update for a class."""
        instance_id, attr_dict = params.split(', ', 1)
        instance_id = instance_id.strip('"')
        attr_dict = eval(attr_dict)
        key = "{}.{}".format(class_name, instance_id)
        if key in storage.all():
            instance = storage.all()[key]
            for attr_name, attr_value in attr_dict.items():
                self.update_attribute(instance, attr_name, attr_value)
            instance.save()
        else:
            print("** no instance found **")

    def handle_single_update(self, class_name, params):
        """Handle single attribute update for a class."""
        if len(params) == 3:
            instance_id, attr_name, attr_value = params
            instance_id = instance_id.strip('"')
            attr_name = attr_name.strip('"')
            attr_value = attr_value.strip('"')
            key = "{}.{}".format(class_name, instance_id)
            if key in storage.all():
                instance = storage.all()[key]
                self.update_attribute(instance, attr_name, attr_value)
                instance.save()
            else:
                print("** no instance found **")
        else:
            print("** invalid command **")

    def update_attribute(self, instance, attr_name, attr_value):
        """Update the attribute of an instance."""
        if hasattr(instance, attr_name):
            attr_type = type(getattr(instance, attr_name))
            try:
                attr_value = attr_type(attr_value)
            except ValueError:
                pass  # Keep it as a string if conversion fails
        setattr(instance, attr_name, attr_value)


if __name__ == '__main__':
    """Start the CLI."""
    HBNBCommand().cmdloop()
