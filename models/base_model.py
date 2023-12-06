#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """A base class for other classes"""

    def _init_(self, *args, **kwargs):
        """Initialize a new instance"""

        if kwargs: # if kwargs is not empty
            for key, value in kwargs.items(): # iterate over the key-value pairs
                if key == "_class": # skip the __class_ key
                    continue
                elif key == "created_at" or key == "updated_at": # convert datetime strings to objects
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value) # set the attribute with the value
                else:
                    self.id = str(uuid.uuid4()) # generate a unique id
                    self.created_at = datetime.now()
                    self.updated_at = self.created_at
                    storage.new(self)

                    def _str_(self):
                        """Return a string representation of the instance"""
                        return "[{}] ({}) {}".format(self._class.__name, self.id, self.__dict_)

                    def save(self):
                        """Update the updated_at attribute with the current datetime and save the instance to the storage"""
                        self.updated_at = datetime.now()
                        storage.save()

                        def to_dict(self):
                            """Return a dictionary representation of the instance"""
                            result = self._dict_.copy()
                            result["_class"] = self.__class.__name_
                            result["created_at"] = self.created_at.isoformat()
                            result["updated_at"] = self.updated_at.isoformat()
                            return result
