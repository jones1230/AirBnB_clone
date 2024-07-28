#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def setUp(self):
        """Set up test environment."""
        # Assuming storage.new(self) is
        # not actually needed for testing and is a placeholder
        pass

    def tearDown(self):
        """Clean up after each test."""
        pass

    def test_init_with_kwargs(self):
        """Test initialization with keyword arguments."""
        kwargs = {
            'id': 'test-id',
            'created_at': '2023-01-01T00:00:00.000000',
            'updated_at': '2023-01-01T00:00:00.000000'
        }
        model = BaseModel(**kwargs)
        self.assertEqual(model.id, 'test-id')
        self.assertEqual(model.created_at, datetime(2023, 1, 1))
        self.assertEqual(model.updated_at, datetime(2023, 1, 1))

    def test_init_without_kwargs(self):
        """Test initialization without keyword arguments."""
        model = BaseModel()
        self.assertIsNotNone(model.id)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str_representation(self):
        """Test the string representation of the BaseModel instance."""
        model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(str(model), expected_str)

    def test_save_method(self):
        """Test the save method updates the updated_at attribute."""
        model = BaseModel()
        original_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(original_updated_at, model.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method converts the instance to a dictionary."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['created_at'],
                         model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'],
                         model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
