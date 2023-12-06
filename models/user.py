#!/usr/bin/python3
"""This module creates a user class"""

from models.base_model import BaseModel

class User(BaseModel):
    """A class that represents a user"""

    email = "" # a string attribute for email
    password = "" # a string attribute for password
    first_name = "" # a string attribute for first name
    last_name = "" # a string attribute for last name
