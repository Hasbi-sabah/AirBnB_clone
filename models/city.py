#!/usr/bin/env python3
"""
Module for the class City
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    class City

    Attributes:
        state_id (str): The ID of the state to which the city belongs.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
