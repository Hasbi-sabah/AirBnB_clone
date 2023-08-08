#!/usr/bin/env python3
"""
Module of te class User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    class User

    Attributes:
        email (str): The email address of the user.
        password (str): The password associated with the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
