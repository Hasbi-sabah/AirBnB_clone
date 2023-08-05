#!/usr/bin/env python3
"""
The data storage module
"""
import json
from models.base_model import BaseModel


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        save_obj = {}
        for key, value in self.__objects.items():
            save_obj[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as fd:
            json.dump(save_obj, fd)

    def reload(self):
        try:
            with open(self.__file_path, encoding="utf-8") as fd:
                json_fvar = json.load(fd)

            for key, value in json_fvar.items():
                self.new(eval(key.split('.')[0])(**value))
        except FileNotFoundError:
            pass
