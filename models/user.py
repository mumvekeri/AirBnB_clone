#!/usr/bin/python3
"""This module creates a user class"""

from models.base_model import BaseModel


class User(BaseModel):
    """A class that represents a user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
