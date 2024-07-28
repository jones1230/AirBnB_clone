#!/usr/bin/python3

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        """Set up test environment."""
        self.storage = FileStorage()
        self.base_model = BaseModel()
        self.test_file_path = 'test_filestoragedb.json'
        self.storage._FileStorage__file_path = self.test_file_path

    def tearDown(self):
        """Clean up after each test."""
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_all(self):
        """Test the all method."""
        self.assertEqual(type(self.storage.all()), dict)

    def test_new(self):
        """Test the new method."""
        self.storage.new(self.base_model)
        key = f'{self.base_model.__class__.__name__}.{self.base_model.id}'
        self.assertIn(key, self.storage.all())

    def test_save_reload(self):
        """Test the save and reload methods."""
        self.storage.new(self.base_model)
        self.storage.save()
        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.test_file_path
        new_storage.reload()
        key = f'{self.base_model.__class__.__name__}.{self.base_model.id}'
        self.assertIn(key, new_storage.all())

    def test_attributes(self):
        """Test the attributes method."""
        attributes = self.storage.attributes()
        self.assertIn("BaseModel", attributes)
        self.assertIn("User", attributes)
        self.assertIn("State", attributes)
        self.assertIn("City", attributes)
        self.assertIn("Amenity", attributes)
        self.assertIn("Place", attributes)
        self.assertIn("Review", attributes)

    def test_classes(self):
        """Test the classes method."""
        classes = self.storage.classes()
        self.assertIn("BaseModel", classes)
        self.assertIn("User", classes)
        self.assertIn("State", classes)
        self.assertIn("City", classes)
        self.assertIn("Amenity", classes)
        self.assertIn("Place", classes)
        self.assertIn("Review", classes)


if __name__ == '__main__':
    unittest.main()
