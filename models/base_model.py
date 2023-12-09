#!/usr/bin/python3
"""
Base class for all other models. This class provides common attributes and methods,
including initialization from both keyword arguments and dictionary representations.

Attributes:
    id (str): Unique identifier for the model.
    created_at (datetime): Date and time of the model creation.
    updated_at (datetime): Date and time of the last model update.

Methods:
    __init__(self, *args, **kwargs): Initializes the model with arguments.
    __str__(self): Returns a string representation of the model.
    save(self): Updates the model's `updated_at` attribute.
    to_dict(self): Creates a dictionary representation of the model.
"""


class BaseModel:

    def __init__(self, *args, **kwargs):
        self._initialize_from_kwargs(kwargs)
        if not kwargs:
            self._initialize_new_instance()

    def _initialize_from_kwargs(self, kwargs):
        if kwargs:
            self.id = kwargs.pop("id", str(uuid.uuid4()))
            try:
                self.created_at = datetime.fromisoformat(kwargs.pop("created_at"))
                self.updated_at = datetime.fromisoformat(kwargs.pop("updated_at"))
            except ValueError:
                raise ValueError("Invalid date format in kwargs")
            for key, value in kwargs.items():
                setattr(self, key, value)

    def _initialize_new_instance(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[<{self.__class__.__name__}>] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict_repr = self.__dict__.copy()
        dict_repr.update({
            "__class__": self.__class__.__name__,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        })
        return dict_repr

