!/usr/bin/python3
""" This file tests
"""

import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        # Ensure that the file path is set to a temporary file
        self.file_path = "test_file.json"
        FileStorage._file_path = self.file_path
        self.storage = FileStorage()

    def tearDown(self):
        # Remove the temporary file after testing
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        # Test if all returns the correct dictionary of objects
        obj1 = BaseModel()
        obj2 = User()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.assertEqual(self.storage.all(), {"BaseModel.{}".format(obj1.id): obj1,
                                              "User.{}".format(obj2.id): obj2})

    def test_new(self):
        # Test if new adds the object to the dictionary
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn("BaseModel.{}".format(obj.id), self.storage.all())

    def test_save_reload(self):
        # Test if save and reload work together to store and load objects
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        self.assertEqual(new_storage.all(), {"BaseModel.{}".format(obj.id): obj})

    def test_reload_file_not_found(self):
        # Test if reload handles the FileNotFoundError when the file is not found
        with self.assertRaises(FileNotFoundError):
            self.storage.reload()

    def test_reload_empty_file(self):
        # Test if reload works when the file is empty
        with open(self.file_path, "w") as f:
            f.write("")

        self.storage.reload()
        self.assertEqual(self.storage.all(), {})

    def test_reload_invalid_json(self):
        # Test if reload handles invalid JSON in the file
        with open(self.file_path, "w") as f:
            f.write("invalid json")

        with self.assertRaises(json.JSONDecodeError):
            self.storage.reload()

    def test_reload_invalid_class(self):
        # Test if reload handles invalid class names in the file
        with open(self.file_path, "w") as f:
            f.write('{"invalid_class": {"id": "123"}}')

        self.storage.reload()
        self.assertEqual(self.storage.all(), {})


if __name__ == '__main__':
    unittest.main()

