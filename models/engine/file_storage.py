#!/usr/bin/python3
import json


class FileStorage():
    __file_path = 'filestoragedb.json'
    __objects = dict()  # __class__.__name__ + <object> + .id: <class name>.id

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        obj_dict = dict()
        for obj_key, obj_value in self.__objects.items():
            obj_dict[obj_key] = obj_value.to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as json_file:
            json.dump(obj_dict, json_file)

    def reload(self):
        try:
           with open(self.__file_path, 'r') as fhand:
                json_dict = json.loads(fhand.read())
                for value in json_dict.values():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
        except Exception:
            pass
