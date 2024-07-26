#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime, timezone


class BaseModel():
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ('created_at', 'updated_at'):
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def __str__(self):
        return f'[{self.__class__.__name__}]({self.id}){self.__dict__}'

    def save(self):
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        self.__dict__.update(
            {'__class__': __class__.__name__,
            'updated_at': datetime.isoformat(self.updated_at),
            'created_at': datetime.isoformat(self.created_at)
            })
        return self.__dict__
        # sorted_items = sorted(self.__dict__.items())
        # return dict(sorted_items)
