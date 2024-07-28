#!/usr/bin/python3
"""
This module defines the State class.
The State class inherits from BaseModel and includes additional attributes.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State class that inherits from BaseModel.

    Attributes:
        name (str): Name of the state. Default is an empty string.
    """
    name: str = ""
