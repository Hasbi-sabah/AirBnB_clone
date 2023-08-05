#!/usr/bin/env python3
"""
The data storage module
"""
import json


class FileStorage():
    __file_path = "../../storage.json"
    __objects = {}

    def all(self):
        return self.__objects

    def _get_id(self, obj):
        return str(obj.id)

    def new(self, obj):
        FileStorage.__objects[obj+"."+_get_id] = obj

    def save(self):
        json_file = json.dumps(cls.__objects)
        with open(cls.__file_path, "w", encoding="utf-8") as fd:
            fd.write(json_file)

    def reload(self):
        try:
            with open(cls.__file_path, "r", encoding="utf-8") as fd:
                json_fvar = json.load(fd)

        FileStorage.__objects = (json_fvar)

        except FileNotFoundError:
            pass
