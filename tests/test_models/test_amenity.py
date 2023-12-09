#!/usr/bin/python3
"""this file has test cases for amenity.py"""

import unittest
from amenity import Amenity

class TestAmenity(unittest.TestCase):
"""Amenity test class"""

    def setUp(self):
        self.amenity = Amenity()

    def tearDown(self):
        del self.amenity

    def test_init(self):
        self.assertIsInstance(self.amenity, BaseModel)
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, "")

    def test_str(self):
        expected = "[{}] ({}) {}".format(self.amenity.class.__name, self.amenity.id, self.amenity.__dict_)
        self.assertEqual(str(self.amenity), expected)

    def test_to_dict(self):
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict["class"], self.amenity._class.__name_)
        self.assertEqual(amenity_dict["id"], self.amenity.id)
        self.assertEqual(amenity_dict["created_at"], self.amenity.created_at.isoformat())
        self.assertEqual(amenity_dict["updated_at"], self.amenity.updated_at.isoformat())
        self.assertEqual(amenity_dict["name"], self.amenity.name)

    def test_init_kwargs(self):
        kwargs = {
            "_class": "Test",
            "id": "1234",
            "created_at": "2023-12-09T18:06:20.000000",
            "updated_at": "2023-12-09T18:06:20.000000",
            "name": "Wifi"
        }
        amenity = Amenity(**kwargs)
        self.assertEqual(amenity.id, kwargs["id"])
        self.assertEqual(amenity.created_at, datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(amenity.updated_at, datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(amenity.name, kwargs["name"])
        self.assertIsInstance(amenity, BaseModel)
        self.assertEqual(amenity._class, Amenity)

if _name_ == "_main_":
    unittest.main()
