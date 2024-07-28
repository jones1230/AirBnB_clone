#!/usr/bin/python3

"""
Unittests for the State class.
"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    Test cases for the State class.
    """

    def setUp(self):
        """
        Set up for test methods.
        """
        self.state = State()

    def test_instance(self):
        """
        Test if the state is an instance of State and BaseModel.
        """
        self.assertIsInstance(self.state, State)

    def test_attributes(self):
        """
        Test if the State attributes are correct.
        """
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "")

    def test_to_dict(self):
        """
        Test the to_dict method.
        """
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict["__class__"], "State")
        self.assertTrue("created_at" in state_dict)
        self.assertTrue("updated_at" in state_dict)
        self.assertTrue("id" in state_dict)
        self.assertTrue("name" in state_dict)

    def test_str(self):
        """
        Test the string representation of the State class.
        """
        self.state.name = "California"
        string_rep = str(self.state)
        self.assertIn("[State]", string_rep)
        self.assertIn("California", string_rep)
        self.assertIn(self.state.id, string_rep)

    def test_save(self):
        """
        Test the save method.
        """
        old_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(old_updated_at, self.state.updated_at)


if __name__ == "__main__":
    unittest.main()
