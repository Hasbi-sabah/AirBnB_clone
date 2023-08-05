#!/usr/bin/env python3
"""
Base Model for AirBnB
"""
import uuid
import datetime
import models


class BaseModel:
    """
    Base class
    """
    def __init__(self, *args, **kwargs):
        """Initialize the class"""
        if kwargs is not None and kwargs:
            for key, value in kwargs.items():
                if key in ("created_at", "update_at"):
                    setattr(self, key, self.str_to_iso(value))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.current_time()
            self.update_at = self.current_time()
            models.storage.new(self)

    def str_to_iso(self, date_str):
        """ Convert string to isoformat"""
        fmt = "%Y-%m-%dT%H:%M:%S.%f"
        return datetime.datetime.strptime(date_str, fmt)

    def current_time(self):
        """ Get the current time"""
        return datetime.datetime.now()

    def save(self):
        """ Updates the time"""
        self.update_at = self.current_time()
        models.storage.save()

    def to_dict(self):
        """ Return a dictionary of of the class instance"""
        dic_temp = self.__dict__
        dic_temp["__class__"] = self.__class__.__name__
        dic_temp["created_at"] = self.fmt_time(self.created_at)
        dic_temp["update_at"] = self.fmt_time(self.update_at)
        return dic_temp

    def fmt_time(self, curr):
        """ Format the time and date"""
        return curr.isoformat()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
