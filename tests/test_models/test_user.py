#!/usr/bin/python3

import unittest
from models.user import User
from datetime import datetime

class TestUser(unittest.TestCase):
    """Test the User class"""

    def setUp(self):
        """Set up the test environment"""
        self.user = User()

    def test_inheritance(self):
        """Test if User is a subclass of BaseModel"""
        self.assertIsInstance(self.user, User)
        self.assertTrue(issubclass(type(self.user), BaseModel))

    def test_attributes(self):
        """Test the attributes of User"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_initialization_with_kwargs(self):
        """Test initialization with kwargs"""
        kwargs = {
            'id': '1234',
            'created_at': '2022-01-01T12:00:00.000000',
            'updated_at': '2022-01-01T12:00:00.000000',
            'email': 'test@example.com',
            'password': 'password123',
            'first_name': 'John',
            'last_name': 'Doe'
        }
        user = User(**kwargs)
        self.assertEqual(user.id, '1234')
        self.assertEqual(user.created_at, datetime(2022, 1, 1, 12, 0, 0))
        self.assertEqual(user.updated_at, datetime(2022, 1, 1, 12, 0, 0))
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.password, 'password123')
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')

    def test_to_dict_method(self):
        """Test the to_dict method of User"""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(type(user_dict['created_at']), str)
        self.assertEqual(type(user_dict['updated_at']), str)
        self.assertTrue('id' in user_dict)
        self.assertTrue('created_at' in user_dict)
        self.assertTrue('updated_at' in user_dict)
        self.assertTrue('email' in user_dict)
        self.assertTrue('password' in user_dict)
        self.assertTrue('first_name' in user_dict)
        self.assertTrue('last_name' in user_dict)

    def test_str_method(self):
        """Test the __str__ method of User"""
        user_str = str(self.user)
        self.assertIn("[User]", user_str)
        self.assertIn("id", user_str)
        self.assertIn("created_at", user_str)
        self.assertIn("updated_at", user_str)
        self.assertIn("email", user_str)
        self.assertIn("password", user_str)
        self.assertIn("first_name", user_str)
        self.assertIn("last_name", user_str)
if __name__ == "__main__":
    unittest.main()
