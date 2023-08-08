#!/usr/bin/env python3
"""
Module of the class Reviews
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    class Review

    Attributes:
        place_id (str): The ID of the place being reviewed.
        user_id (str): The ID of the user who wrote the review.
        text (str): The text content of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
