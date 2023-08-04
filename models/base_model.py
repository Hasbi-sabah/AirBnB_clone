#!/usr/bin/env python3
"""
Base Model for AirBnB
"""
import uuid
import datetime


class BaseModel:
    """
    Base class
    """
    def __init__(self):
        """Initialize the class"""
        self.id = str(uuid.uuid4())
        self.created_at = self.current_time()
        self.update_at = self.current_time()

    def current_time(self):
        """ Get the current time"""
        return datetime.datetime.now()

    def save(self):
        """ Updates the time"""
        self.update = self.current_time()

    def to_dict(self):
        """ Return a dictionary of of the class instance"""
        dic_temp = self.__dict__
        dic_temp["__class__"] = self.__class__.__name__
        dic_temp["created_at"] = fmt_time(self.created_at)
        dic_temp["update_at"] = fmt_time(self.update_at)
        return dic_temp

    def fmt_time(self, curr):
        """ Format the time and date"""
        return curr.isoformat(format="%Y-%m-%dT%H:%M:%S.%f")

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
