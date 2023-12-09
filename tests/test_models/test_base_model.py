#!/usr/bin/python3
"""Test cases for base_model.py"""

import unittest
from base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base = BaseModel()

    def tearDown(self):
        del self.base

    def test_init(self):
        self.assertIsNotNone(self.base.id)
        self.assertIsNotNone(self.base.created_at)
        self.assertIsNotNone(self.base.updated_at)
        self.assertEqual(self.base._class, BaseModel)
        self.assertIn(self.base, storage.all())

    def test_str(self):
        expected = "[{}] ({}) {}".format(self.base.class.__name, self.base.id, self.base.__dict_)
        self.assertEqual(str(self.base), expected)

    def test_save(self):
        old_updated_at = self.base.updated_at
        self.base.save()
        self.assertNotEqual(self.base.updated_at, old_updated_at)
        self.assertIn(self.base, storage.all())

    def test_to_dict(self):
        base_dict = self.base.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertEqual(base_dict["class"], self.base._class.__name_)
        self.assertEqual(base_dict["id"], self.base.id)
        self.assertEqual(base_dict["created_at"], self.base.created_at.isoformat())
        self.assertEqual(base_dict["updated_at"], self.base.updated_at.isoformat())

    def test_init_kwargs(self):
        kwargs = {
            "_class": "Test",
            "id": "1234",
            "created_at": "2023-12-09T18:06:20.000000",
            "updated_at": "2023-12-09T18:06:20.000000",
            "name": "Alice"
        }
        base = BaseModel(**kwargs)
        self.assertEqual(base.id, kwargs["id"])
        self.assertEqual(base.created_at, datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(base.updated_at, datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(base.name, kwargs["name"])
        self.assertEqual(base._class, BaseModel)
        self.assertIn(base, storage.all())

    def test_init_empty_kwargs(self):
        base = BaseModel(**{})
        self.assertIsNotNone(base.id)
        self.assertIsNotNone(base.created_at)
        self.assertIsNotNone(base.updated_at)
        self.assertEqual(base._class, BaseModel)
        self.assertIn(base, storage.all())

    def test_init_invalid_kwargs(self):
        kwargs = {
            "id": 1234,
            "created_at": 2023,
            "updated_at": "invalid"
        }
        base = BaseModel(**kwargs)
        self.assertIsNotNone(base.id)
        self.assertIsNotNone(base.created_at)
        self.assertIsNotNone(base.updated_at)
        self.assertEqual(base._class, BaseModel)
        self.assertIn(base, storage.all())

if _name_ == "_main_":
    unittest.main()
