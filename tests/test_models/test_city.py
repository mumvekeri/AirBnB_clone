#!/usr/bin/python3
"""Test cases for city class"""

import unittest
from city import City

class TestCity(unittest.TestCase):
"""City Tests"""

    def setUp(self):
        self.city = City()

    def tearDown(self):
        del self.city

    def test_init(self):
        self.assertIsInstance(self.city, BaseModel)
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_str(self):
        expected = "[{}] ({}) {}".format(self.city.class.__name, self.city.id, self.city.__dict_)
        self.assertEqual(str(self.city), expected)

    def test_to_dict(self):
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict["class"], self.city._class.__name_)
        self.assertEqual(city_dict["id"], self.city.id)
        self.assertEqual(city_dict["created_at"], self.city.created_at.isoformat())
        self.assertEqual(city_dict["updated_at"], self.city.updated_at.isoformat())
        self.assertEqual(city_dict["state_id"], self.city.state_id)
        self.assertEqual(city_dict["name"], self.city.name)

    def test_init_kwargs(self):
        kwargs = {
            "_class": "Test",
            "id": "1234",
            "created_at": "2023-12-09T18:06:20.000000",
            "updated_at": "2023-12-09T18:06:20.000000",
            "state_id": "5678",
            "name": "Johannesburg"
        }
        city = City(**kwargs)
        self.assertEqual(city.id, kwargs["id"])
        self.assertEqual(city.created_at, datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(city.updated_at, datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(city.state_id, kwargs["state_id"])
        self.assertEqual(city.name, kwargs["name"])
        self.assertIsInstance(city, BaseModel)
        self.assertEqual(city._class, City)

if _name_ == "_main_":
    unittest.main()
