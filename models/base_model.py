#!/usr/bin/python3
""" This file defines the BaseModel class, which represents
the base model for all other models in the HBnB project.
"""


import models
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    Represents the base model for all HBnB models.

    Attributes:
        id (str): A unique identifier for the model instance.
        created_at (datetime): The date and time the model instance was created
        updated_at (datetime): The date and time the model instance was last.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance.

        Args:
            *args (any): Unused arguments.
            **kwargs (dict): Key/value pairs of attributes to set on the
        """
        # Define date and time format for string conversion
        date_time_format = "%Y-%m-%dT%H:%M:%S.%f"

        # Generate unique identifier
        self.id = str(uuid4())

        # Set creation and update timestamps
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        # Populate attributes from kwargs
        if kwargs:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    # Parse date/time strings
                    setattr(self, key, datetime.strptime
                            (value, date_time_format))
                else:
                    # Set other attributes directly
                    setattr(self, key, value)
        else:
            # Register new instance with storage
            models.storage.new(self)

    def save(self):
        """
        Updates the model instance's updated_at timestamp and saves change.
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the model instance.

        Includes a "__class__" key-value pair for identifying the class of.
        """
        # Create copy of object's internal dictionary
        object_dict = self.__dict__.copy()

        # Convert date/time attributes to ISO format strings
        object_dict["created_at"] = self.created_at.isoformat()
        object_dict["updated_at"] = self.updated_at.isoformat()

        # Add "__class__" entry with class name
        object_dict["__class__"] = self.__class__.__name__

        # Return the complete dictionary
        return object_dict

    def __str__(self):
        """
        Returns the string representation of the model instance.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
