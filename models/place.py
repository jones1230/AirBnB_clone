#!/usr/bin/python3
"""
This module defines the Place class.
The Place class inherits from BaseModel and includes additional attributes.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class that inherits from BaseModel.

    Attributes:
        city_id (str): The city id. Default is an empty string.
        user_id (str): The user id. Default is an empty string.
        name (str): Name of the place. Default is an empty string.
        description (str): Description of the place. Default is an
        empty string.
        number_rooms (int): Number of rooms. Default is 0.
        number_bathrooms (int): Number of bathrooms. Default is 0.
        max_guest (int): Maximum number of guests. Default is 0.
        price_by_night (int): Price per night. Default is 0.
        latitude (float): Latitude of the place. Default is 0.0.
        longitude (float): Longitude of the place. Default is 0.0.
        amenity_ids (list): List of amenity ids. Default is an empty list.
    """
    city_id: str = ""
    user_id: str = ""
    name: str = ""
    description: str = ""
    number_rooms: int = 0
    number_bathrooms: int = 0
    max_gue: int = 0
    price_by_night = 0
    latitude: float = 0.0
    longitude: float = 0.0
    amenity_ids: list = []
