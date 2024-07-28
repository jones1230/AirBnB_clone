#!/usr/bin/python3
"""
This module defines the User class.
The User class inherits from BaseModel and includes additional attributes.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel.

    Attributes:
        email (str): Email of the user. Default is an empty string.
        password (str): Password of the user. Default is an empty string.
        first_name (str): First name of the user. Default is an empty string.
        last_name (str): Last name of the user. Default is an empty string.
    """
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
