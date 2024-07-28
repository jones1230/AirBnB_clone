#!/usr/bin/python3

import unittest
import json
import os
from unittest.mock import patch, mock_open
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""

    def setUp(self):
        """Set up the test environment"""
        self.storage = FileStorage()
        self.model = BaseModel()
        self.model.id = "1234"
        self.model.created_at = datetime(2022, 1, 1, 12, 0, 0)
        self.model.updated_at = datetime(2022, 1, 1, 12, 0, 0)
        self.model_dict = self.model.to_dict()

    def tearDown(self):
        """Clean up after the test"""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all(self):
        """Test the all method"""
        self.storage.new(self.model)
        all_objects = self.storage.all()
        self.assertIn('BaseModel.1234', all_objects)
        self.assertEqual(all_objects['BaseModel.1234'], self.model)

    def test_new(self):
        """Test the new method"""
        self.storage.new(self.model)
        self.assertIn('BaseModel.1234', self.storage._FileStorage__objects)
        self.assertEqual(self.storage._FileStorage__objects['BaseModel.1234'],
                         self.model)

    @patch("builtins.open", new_callable=mock_open)
    @patch("models.engine.file_storage.FileStorage._FileStorage__file_path",
           "test.json")
    def test_save(self, mock_file):
        """Test the save method"""
        self.storage.new(self.model)
        self.storage.save()
        mock_file.assert_called_once_with("test.json", "w", encoding="utf-8")
        handle = mock_file()
        handle.write.assert_called_once()
        handle.write(json.dumps({'BaseModel.1234': self.model_dict}))

    @patch("builtins.open", new_callable=mock_open,
           read_data=json.dumps({'BaseModel.1234': {
            '__class__': 'BaseModel', 'id': '1234',
            'created_at': '2022-01-01T12:00:00.000000',
            'updated_at': '2022-01-01T12:00:00.000000'}}))
    @patch("models.engine.file_storage.FileStorage._FileStorage__file_path",
           "test.json")
    def test_reload(self, mock_file):
        """Test the reload method"""
        self.storage.new(self.model)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        self.assertIn('BaseModel.1234', self.storage._FileStorage__objects)
        self.assertEqual(
            self.storage._FileStorage__objects['BaseModel.1234'].id, '1234')

    def test_classes(self):
        """Test the classes method"""
        classes = self.storage.classes()
        self.assertIn("BaseModel", classes)
        self.assertIn("User", classes)
        self.assertIn("State", classes)
        self.assertIn("City", classes)
        self.assertIn("Amenity", classes)
        self.assertIn("Place", classes)
        self.assertIn("Review", classes)

    def test_attributes(self):
        """Test the attributes method"""
        attributes = self.storage.attributes()
        self.assertIn("BaseModel", attributes)
        self.assertIn("id", attributes["BaseModel"])
        self.assertIn("created_at", attributes["BaseModel"])
        self.assertIn("updated_at", attributes["BaseModel"])
        self.assertIn("User", attributes)
        self.assertIn("email", attributes["User"])
        self.assertIn("password", attributes["User"])
        self.assertIn("first_name", attributes["User"])
        self.assertIn("last_name", attributes["User"])


if __name__ == "__main__":
    unittest.main()
