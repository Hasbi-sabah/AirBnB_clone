#!/usr/bin/env python3
"""
Module for the class FileStorage
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Class to manage serialization and deserialization of objects.

    Attributes:
        __file_path (str): The path to the JSON file.
        __objects (dict): A dictionary containing all serialized objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Retrieve the dictionary of all serialized objects.

        Returns:
            dict: A dictionary containing all serialized objects.

        """
        return self.__objects

    def new(self, obj):
        """
        Add a new serialized object to the dictionary.

        Args:
            obj: An instance of a class to be added.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Save the serialized objects to the JSON file.
        """
        save_obj = {}
        for key, value in self.__objects.items():
            save_obj[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as fd:
            json.dump(save_obj, fd)

    def reload(self):
        """
        Load serialized data from the JSON file and create instances.
        """
        try:
            with open(self.__file_path, encoding="utf-8") as fd:
                json_fvar = json.load(fd)

            for key, value in json_fvar.items():
                self.new(eval(key.split(".")[0])(**value))
        except FileNotFoundError:
            pass
