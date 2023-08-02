#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        s = "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
        return s

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict_cpy = self.__dict__.copy()
        dict_cpy['__class__'] = type(self).__name__
        dict_cpy['created_at'] = dict_cpy['created_at'].isoformat()
        dict_cpy['updated_at'] = dict_cpy['updated_at'].isoformat()
        return dict_cpy

if __name__ == "__main__":
    mod = BaseModel()
    print(mod.updated_at)
