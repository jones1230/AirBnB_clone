#!/usr/bin/python3

"""
This module defines the BaseModel class for the AirBnB clone project.

The BaseModel class provides a base structure for other models,
including methods for initialization, string representation,
saving, and converting instances to a dictionary format.

Imports:
    - uuid: For generating unique identifiers.
    - datetime: For handling date and time information.
    - storage: For interacting with the storage system (e.g., saving and retrieving instances).
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    A base class for all models in the AirBnB clone project.

    Attributes:
        id (str): A unique identifier for the instance.
        created_at (datetime): The date and time when the instance was created.
        updated_at (datetime): The date and time when the instance was last
        updated.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance.

        Args:
            *args: Variable length argument list (not used in this method).
            **kwargs: Keyword arguments used to initialize the instance.
                Can include 'id', 'created_at', and 'updated_at' to set their
                values.

        If `kwargs` is provided and contains 'created_at' or 'updated_at',
        those values are parsed and assigned to the instance. Otherwise, a
        new id is generated, and `created_at` and `updated_at` are set to
        the current date and time.
        """
        if kwargs:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: A string representation of the instance in the format:
                "[ClassName] (id) {'attribute': value, ...}"
        """
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Updates the `updated_at` attribute with the current date and time and
        saves the instance to the storage.

        This method is used to persist changes made to the instance.
        """
        self.updated_at = datetime.now()
        storage.save(self)

    def to_dict(self):
        """
        Converts the instance to a dictionary format.

        Returns:
            dict: A dictionary representation of the instance with the
            following keys:
                - '__class__': The name of the class.
                - 'id': The unique identifier.
                - 'created_at': The creation date and time (in ISO format).
                - 'updated_at': The last update date and time (in ISO format).
                - All other instance attributes.
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
