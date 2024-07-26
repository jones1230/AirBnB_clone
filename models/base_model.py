#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime, timezone


class BaseModel():
    def __init__(self) -> None:
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at

    def __str__(self):
        return f'[{self.__class__.__name__}]({self.id}){BaseModel().__dict__}'

    def save(self):
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        self.__dict__.update(__class__=__class__.__name__)
        self.__dict__.update(updated_at=self.updated_at.isoformat())
        self.__dict__.update(created_at=self.created_at.isoformat())
        sorted_items = sorted(self.__dict__.items())
        return dict(sorted_items)
