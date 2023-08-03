#!/usr/bin/python3

import uuid
from datetime import datetime
from . import storage

class BaseModel:
    def __init__(self, *args, **kwargs):
        for key, item in kwargs.items():
            if key != '__class__':
                if key == 'created_at' or key == 'updated_at':
                    d_format = '%Y-%m-%dT%H:%M:%S.%f'
                    setattr(self, key, datetime.strptime(item, d_format))
                else:
                    setattr(self, key, item)
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        s = "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
        return s

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        dict_cpy = self.__dict__.copy()
        dict_cpy['__class__'] = type(self).__name__
        dict_cpy['created_at'] = dict_cpy['created_at'].isoformat()
        dict_cpy['updated_at'] = dict_cpy['updated_at'].isoformat()
        return dict_cpy
