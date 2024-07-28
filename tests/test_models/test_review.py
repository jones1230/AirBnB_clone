#!/usr/bin/python3
"""
Unittests for the Review class.
"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test cases for the Review class.
    """

    def setUp(self):
        """
        Set up for test methods.
        """
        self.review = Review()

    def test_instance(self):
        """
        Test if the review is an instance of Review and BaseModel.
        """
        self.assertIsInstance(self.review, Review)

    def test_attributes(self):
        """
        Test if the Review attributes are correct.
        """
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertEqual(self.review.place_id, "")
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertEqual(self.review.user_id, "")
        self.assertTrue(hasattr(self.review, "text"))
        self.assertEqual(self.review.text, "")

    def test_to_dict(self):
        """
        Test the to_dict method.
        """
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict["__class__"], "Review")
        self.assertTrue("created_at" in review_dict)
        self.assertTrue("updated_at" in review_dict)
        self.assertTrue("id" in review_dict)
        self.assertTrue("place_id" in review_dict)
        self.assertTrue("user_id" in review_dict)
        self.assertTrue("text" in review_dict)

    def test_str(self):
        """
        Test the string representation of the Review class.
        """
        self.review.text = "Great place!"
        self.review.place_id = "123"
        self.review.user_id = "456"
        string_rep = str(self.review)
        self.assertIn("[Review]", string_rep)
        self.assertIn("Great place!", string_rep)
        self.assertIn("123", string_rep)
        self.assertIn("456", string_rep)
        self.assertIn(self.review.id, string_rep)

    def test_save(self):
        """
        Test the save method.
        """
        old_updated_at = self.review.updated_at
        self.review.save()
        self.assertNotEqual(old_updated_at, self.review.updated_at)


if __name__ == "__main__":
    unittest.main()
