#!/usr/bin/env python3
"""
Create a user
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ User details"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
