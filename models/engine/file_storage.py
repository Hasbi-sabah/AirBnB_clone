#!/usr/bin/python3
import json
import uuid
from datetime import datetime as dt
class FileStorage:
    def __init__(self):
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        obj_key = '{}.{}'.format(type(obj).__name__, obj.id)
        self.__objects[obj_key] = obj.__dict__
        d_f = '%Y-%m-%dT%H:%M:%S.%f'
        for value in self.__objects.values():
            if type(value['created_at']) is str:
                value['created_at'] = dt.strptime(value['created_at'], d_f)
                value['updated_at'] = dt.strptime(value['updated_at'], d_f)

    def save(self):
        for value in self.__objects.values():
            if type(value['created_at']) is dt:
                value['created_at'] = value['created_at'].isoformat()
                value['updated_at'] = value['updated_at'].isoformat()
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f)
        d_f = '%Y-%m-%dT%H:%M:%S.%f'
        for value in self.__objects.values():
            if type(value['created_at']) is str:
                value['created_at'] = dt.strptime(value['created_at'], d_f)
                value['updated_at'] = dt.strptime(value['updated_at'], d_f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
            d_f = '%Y-%m-%dT%H:%M:%S.%f'
            for value in self.__objects.values():
                if type(value['created_at']) is str:
                    value['created_at'] = dt.strptime(value['created_at'], d_f)
                    value['updated_at'] = dt.strptime(value['updated_at'], d_f)
        except FileNotFoundError:
            pass
