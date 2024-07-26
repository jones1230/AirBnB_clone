#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime, timezone


class BaseModel():
    def __init__(self, *args, **kwargs):
        if kwargs is not None and kwargs != {}:
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
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        return f'[{self.__class__.__name__}]({self.id}){self.__dict__}'

    def save(self):
        self.updated_at = datetime.now()

        def to_dict(self):
            new_dict = self.__dict__.copy()
            new_dict["__class__"] = type(self).__name__
            new_dict["created_at"] = new_dict["created_at"].isoformat()
            new_dict["updated_at"] = new_dict["updated_at"].isoformat()
            return new_dict
