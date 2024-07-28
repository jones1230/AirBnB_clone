#!/usr/bin/python3
"""
This module defines the Review class.
The Review class inherits from BaseModel and includes additional attributes.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel.

    Attributes:
        place_id (str): The place id. Default is an empty string.
        user_id (str): The user id. Default is an empty string.
        text (str): Review text. Default is an empty string.
    """
    place_id: str = ""
    user_id: str = ""
    text: str = ""
