#!/usr/bin/python3
from models.base_model import BaseModel

kwargs = {
        "name": "Jane Smith",
        "age": 25,
        "updated_at": "2023-08-05T12:34:56.789012",
}

base_model_with_kwargs = BaseModel(**kwargs)
print(base_model_with_kwargs)
