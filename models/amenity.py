#!/usr/bin/python3
"""
This module defines the Amenity class.
The Amenity class inherits from BaseModel and includes additional attributes.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel.

    Attributes:
        name (str): Name of the amenity. Default is an empty string.
    """
    name: str = ""
