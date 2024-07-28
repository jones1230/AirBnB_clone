#!/usr/bin/python3
"""
Unittests for the Amenity class.
"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class.
    """

    def setUp(self):
        """
        Set up for test methods.
        """
        self.amenity = Amenity()

    def test_instance(self):
        """
        Test if the amenity is an instance of Amenity and BaseModel.
        """
        self.assertIsInstance(self.amenity, Amenity)

    def test_attributes(self):
        """
        Test if the Amenity attributes are correct.
        """
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, "")

    def test_to_dict(self):
        """
        Test the to_dict method.
        """
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertTrue("created_at" in amenity_dict)
        self.assertTrue("updated_at" in amenity_dict)
        self.assertTrue("id" in amenity_dict)
        self.assertTrue("name" in amenity_dict)

    def test_str(self):
        """
        Test the string representation of the Amenity class.
        """
        self.amenity.name = "Wi-Fi"
        string_rep = str(self.amenity)
        self.assertIn("[Amenity]", string_rep)
        self.assertIn("Wi-Fi", string_rep)
        self.assertIn(self.amenity.id, string_rep)

    def test_save(self):
        """
        Test the save method.
        """
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(old_updated_at, self.amenity.updated_at)


if __name__ == "__main__":
    unittest.main()
