#!/usr/bin/python3
"""creates a review module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """creates a review class that inherits from Basemodel"""
    place_id = ""
    user_id = ""
    text = ""
