#!/usr/bin/python3
"""This module creates a place class"""

from models.base_model import BaseModel

class Place(BaseModel):
    """A class that represents a place"""

    city_id = "" # a string attribute for city id
    user_id = "" # a string attribute for user id
    name = "" # a string attribute for name
    description = "" # a string attribute for description
    number_rooms = 0 # an integer attribute for number of rooms
    number_bathrooms = 0 # an integer attribute for number of bathrooms
    max_guest = 0 # an integer attribute for maximum number of guests
    price_by_night = 0 # an integer attribute for price by night
    latitude = 0.0 # a float attribute for latitude
    longitude = 0.0 # a float attribute for longitude
    amenity_ids = [] # a list of string attribute for amenity ids
