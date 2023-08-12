#!/usr/bin/python3
"""
Module for the class BaseModel
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    class BaseModel
    """

    def __init__(self, *args, **kwargs):
        """
        Base class for all model classes.

        Args:
            *args: Non-keyword arguments (not used in this implementation).
            **kwargs: Keyword arguments containing attribute key-value pairs.

        Public instance attributes:
            id (str): Unique identifier assigned when an instance is created.
            created_at (datetime): Date and time when the instance is created.
            updated_at (datetime): Date and time when the instance is updated.
        """
        from models import storage
        for key, item in kwargs.items():
            if key != "__class__":
                if key == "created_at" or key == "updated_at":
                    d_format = "%Y-%m-%dT%H:%M:%S.%f"
                    setattr(self, key, datetime.strptime(item, d_format))
                elif key == "id":
                    setattr(self, key, str(item))
                else:
                    setattr(self, key, item)
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Return a string representation of the instance.

        Returns:
            str: A formatted string containing the cls name,
            instance ID, and attributes.
        """
        s = "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
        return s

    def save(self):
        """
        Update the 'updated_at' attribute and save the instance.
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Convert the instance attributes to a dictionary.

        Returns:
            dict: A dictionary containing instance attributes.
        """
        dict_cpy = self.__dict__.copy()
        dict_cpy["__class__"] = type(self).__name__
        dict_cpy["created_at"] = dict_cpy["created_at"].isoformat()
        dict_cpy["updated_at"] = dict_cpy["updated_at"].isoformat()
        return dict_cpy
