#!/usr/bin/python3
"""This module creates a city class"""

from models.base_model import BaseModel

class City(BaseModel):
    """A class that represents a city"""

    state_id = "" # a string attribute for state id
    name = "" # a string attribute for name
