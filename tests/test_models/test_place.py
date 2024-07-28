#!/usr/bin/python3
"""
Unittests for the Place class.
"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Test cases for the Place class.
    """

    def setUp(self):
        """
        Set up for test methods.
        """
        self.place = Place()

    def test_instance(self):
        """
        Test if the place is an instance of Place and BaseModel.
        """
        self.assertIsInstance(self.place, Place)

    def test_attributes(self):
        """
        Test if the Place attributes are correct.
        """
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertEqual(self.place.city_id, "")
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertEqual(self.place.user_id, "")
        self.assertTrue(hasattr(self.place, "name"))
        self.assertEqual(self.place.name, "")
        self.assertTrue(hasattr(self.place, "description"))
        self.assertEqual(self.place.description, "")
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertEqual(self.place.number_rooms, 0)
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertEqual(self.place.max_guest, 0)
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertEqual(self.place.price_by_night, 0)
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertEqual(self.place.latitude, 0.0)
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertEqual(self.place.longitude, 0.0)
        self.assertTrue(hasattr(self.place, "amenity_ids"))
        self.assertEqual(self.place.amenity_ids, [])

    def test_to_dict(self):
        """
        Test the to_dict method.
        """
        place_dict = self.place.to_dict()
        self.assertEqual(place_dict["__class__"], "Place")
        self.assertTrue("created_at" in place_dict)
        self.assertTrue("updated_at" in place_dict)
        self.assertTrue("id" in place_dict)
        self.assertTrue("city_id" in place_dict)
        self.assertTrue("user_id" in place_dict)
        self.assertTrue("name" in place_dict)
        self.assertTrue("description" in place_dict)
        self.assertTrue("number_rooms" in place_dict)
        self.assertTrue("number_bathrooms" in place_dict)
        self.assertTrue("max_guest" in place_dict)
        self.assertTrue("price_by_night" in place_dict)
        self.assertTrue("latitude" in place_dict)
        self.assertTrue("longitude" in place_dict)
        self.assertTrue("amenity_ids" in place_dict)

    def test_str(self):
        """
        Test the string representation of the Place class.
        """
        self.place.name = "Beach House"
        self.place.city_id = "123"
        self.place.user_id = "456"
        string_rep = str(self.place)
        self.assertIn("[Place]", string_rep)
        self.assertIn("Beach House", string_rep)
        self.assertIn("123", string_rep)
        self.assertIn("456", string_rep)
        self.assertIn(self.place.id, string_rep)

    def test_save(self):
        """
        Test the save method.
        """
        old_updated_at = self.place.updated_at
        self.place.save()
        self.assertNotEqual(old_updated_at, self.place.updated_at)


if __name__ == "__main__":
    unittest.main()
