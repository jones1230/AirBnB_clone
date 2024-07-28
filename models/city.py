#!/usr/bin/python3
"""
This module defines the State class.
The City class inherits from BaseModel and includes additional attributes.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel.

    Attributes:
        name (str): Name of the city. Default is an empty string.
        state_id (str): The State.id. Default is an empty string.
    """
    state_id: str = ""
    name: str = ""
