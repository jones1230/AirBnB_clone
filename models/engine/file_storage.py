#!/usr/bin/python3

"""
This module defines the FileStorage class, which handles the storage of
objects in a JSON file.

The FileStorage class includes methods to manage object storage, including
adding new objects, saving them to a file, and reloading them from a file.

Imports:
    - json: For serializing and deserializing JSON data.
    - os: For file path operations.
    - datetime: For handling date and time (although not used directly here).
"""

import json
import os
import datetime


class FileStorage:
    """
    A class to manage storage of objects in a JSON file.

    Attributes:
        __file_path (str): The path to the file where objects are stored.
        __objects (dict): A dictionary storing objects, with keys in the
            format '<class name>.<id>' and values as the objects themselves.
    """

    __file_path = 'filestoragedb.json'
    __objects = dict()  # Key: '<class name>.<id>', Value: object

    def all(self):
        """
        Returns a dictionary of all stored objects.

        Returns:
            dict: A dictionary of all objects with keys in the format
            '<class name>.<id>' and values as the objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the storage.

        Args:
            obj: The object to be added. The object's key is generated as
            '<class name>.<id>'.
        """
        self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        """
        Serializes all objects to the JSON file defined by __file_path.

        The objects are converted to dictionaries before being written to
        the file.
        """
        obj_dict = dict()
        for obj_key, obj_value in self.__objects.items():
            obj_dict[obj_key] = obj_value.to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as json_file:
            json.dump(obj_dict, json_file)
    
    def attributes(self):
        """Returns the valid attributes and their types for classname"""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes

    def classes(self):
        """
        Returns a dictionary of class names and their corresponding classes.

        Returns:
            dict: A dictionary where keys are class names (as strings) and
            values are the class objects.
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }
        return classes

    def reload(self):
        """
        Deserializes objects from the JSON file defined by __file_path.

        If the file does not exist, the method returns without doing anything.
        Otherwise, it loads the file, converts the JSON data to objects, and
        updates the __objects dictionary.
        """
        if not os.path.isfile(FileStorage.__file_path):
            return
        if os.path.getsize(self.__file_path) == 0:
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as fhand:
            obj_dict = json.load(fhand)
            obj_dict = {k: self.classes()[v["__class__"]](**v)
                        for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict
