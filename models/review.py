#!/usr/bin/env python3
"""
Reviews
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Create reviews"""
    place_id = ""
    user_id = ""
    text = ""
