#!/usr/bin/python3
import json
from models.base_model import BaseModel
class FileStorage:
    def __init__(self):
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        obj_key = '{}.{}'.format(type(obj).__name__, obj.id)
        self.__objects[obj_key] = obj

    def save(self):
        d_objs = {}
        for key, value in self.__objects.items():
            d_objs[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(d_objs, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                s_objs = json.load(f)
            for value in s_objs.values():
                cls = value['__class__']
                self.new(eval(cls)(**value))
        except FileNotFoundError:
            pass
