#!/usr/bin/python3
from models.base_model import BaseModel

class Review(BaseModel):
    """A class that represents a review"""

    place_id = "" # a string attribute for place id
    user_id = "" # a string attribute for user id
    text = "" # a string attribute for text
