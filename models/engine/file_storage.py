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
        print(obj_dict)
        with open(self.__file_path, 'w') as json_file:
            json.dump(obj_dict, json_file)


   
    # from models.base_model import BaseModel
    # from models.engine.file_storage import FileStorage
    # storage = FileStorage()
    # obj1 = BaseModel()
    # obj2 = BaseModel()

    # storage.new(obj1)
    # storage.new(obj2)

    # storage.save()
