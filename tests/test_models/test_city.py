#!/usr/bin/python3
"""
Unittests for the City class.
"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test cases for the City class.
    """

    def setUp(self):
        """
        Set up for test methods.
        """
        self.city = City()

    def test_instance(self):
        """
        Test if the city is an instance of City and BaseModel.
        """
        self.assertIsInstance(self.city, City)

    def test_attributes(self):
        """
        Test if the City attributes are correct.
        """
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(self.city.name, "")
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertEqual(self.city.state_id, "")

    def test_to_dict(self):
        """
        Test the to_dict method.
        """
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict["__class__"], "City")
        self.assertTrue("created_at" in city_dict)
        self.assertTrue("updated_at" in city_dict)
        self.assertTrue("id" in city_dict)
        self.assertTrue("name" in city_dict)
        self.assertTrue("state_id" in city_dict)

    def test_str(self):
        """
        Test the string representation of the City class.
        """
        self.city.name = "San Francisco"
        self.city.state_id = "123"
        string_rep = str(self.city)
        self.assertIn("[City]", string_rep)
        self.assertIn("San Francisco", string_rep)
        self.assertIn("123", string_rep)
        self.assertIn(self.city.id, string_rep)

    def test_save(self):
        """
        Test the save method.
        """
        old_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(old_updated_at, self.city.updated_at)


if __name__ == "__main__":
    unittest.main()
