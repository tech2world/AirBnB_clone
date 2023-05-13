#!/usr/bin/python3
"""creates a city module"""
from models.base_model import BaseModel


class City(BaseModel):
    """city module inherits from BaseModel"""
    state_id = ""
    name = ""
