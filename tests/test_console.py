#!/usr/bin/python3

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User


class TestConsole(unittest.TestCase):
    """Unittests for the HBNBCommand console."""

    def setUp(self):
        """Set up the test environment."""
        self.cli = HBNBCommand()

    def tearDown(self):
        """Clean up the test environment."""
        storage.all().clear()

    def test_EOF(self):
        """Test the EOF command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("EOF")
            self.assertEqual(f.getvalue().strip(), "")

    def test_quit(self):
        """Test the quit command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("quit")
            self.assertEqual(f.getvalue().strip(), "")

    def test_emptyline(self):
        """Test empty line input."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("")
            self.assertEqual(f.getvalue().strip(), "")

    def test_create(self):
        """Test the create command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            new_instance = f.getvalue().strip()
            self.assertTrue(len(new_instance) > 0)
            self.assertIn(new_instance, storage.all())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create NonExistentClass")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_show(self):
        """Test the show command."""
        instance = BaseModel()
        instance.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd(f"show BaseModel {instance.id}")
            self.assertIn(str(instance), f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("show BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("show NonExistentClass 1234")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("show BaseModel 1234")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_destroy(self):
        """Test the destroy command."""
        instance = BaseModel()
        instance.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd(f"destroy BaseModel {instance.id}")
            self.assertNotIn(instance.id, storage.all())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("destroy BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("destroy NonExistentClass 1234")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("destroy BaseModel 1234")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_all(self):
        """Test the all command."""
        instance1 = BaseModel()
        instance2 = User()
        instance1.save()
        instance2.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("all")
            self.assertIn(str(instance1), f.getvalue().strip())
            self.assertIn(str(instance2), f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("all BaseModel")
            self.assertIn(str(instance1), f.getvalue().strip())
            self.assertNotIn(str(instance2), f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("all NonExistentClass")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_update(self):
        """Test the update command."""
        instance = BaseModel()
        instance.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd(f"update BaseModel {instance.id} name 'test'")
            self.assertEqual(f.getvalue().strip(), "")
            self.assertEqual(storage.all()[f"BaseModel.{instance.id}"].name,
                             'test')

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("update BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("update NonExistentClass 1234")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("update BaseModel 1234")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd(f"update BaseModel {instance.id}")
            self.assertEqual(f.getvalue().strip(),
                             "** attribute name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd(f"update BaseModel {instance.id} name")
            self.assertEqual(f.getvalue().strip(), "** value missing **")

    def test_custom_commands(self):
        """Test custom commands."""
        instance = BaseModel()
        instance.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd(f"BaseModel.all()")
            self.assertIn(str(instance), f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd(f"BaseModel.count()")
            self.assertEqual(f.getvalue().strip(), "1")

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd(f"BaseModel.show({instance.id})")
            self.assertIn(str(instance), f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd(f"BaseModel.destroy({instance.id})")
            self.assertEqual(f.getvalue().strip(), "")
            self.assertNotIn(instance.id, storage.all())

        instance = BaseModel()
        instance.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd(f'BaseModel.update({instance.id}, "name", "test")')
            self.assertEqual(f.getvalue().strip(), "")
            self.assertEqual(storage.all()[f"BaseModel.{instance.id}"].name,
                             'test')

        instance = BaseModel()
        instance.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd(
                f'BaseModel.update({instance.id}, {{"name": "test"}})')
            self.assertEqual(f.getvalue().strip(), "")
            self.assertEqual(storage.all()[f"BaseModel.{instance.id}"].name,
                             'test')


if __name__ == "__main__":
    unittest.main()
