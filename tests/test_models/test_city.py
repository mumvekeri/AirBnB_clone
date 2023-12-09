#!/usr/bin/python3
"""These are test cases for the city class module"""

import unittest
from models.city import City
from models.base_model import BaseModel

class TestCity(unittest.TestCase):
    def test_city_instance(self):
        """Test if City is an instance of BaseModel"""
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_city_attributes(self):
        """Test if City has the expected attributes"""
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

    def test_city_attribute_types(self):
        """Test if City attributes have the correct types"""
        city = City()
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)

    def test_city_attributes_default_values(self):
        """Test if City attributes have the correct default values"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_attributes_set_values(self):
        """Test if City attributes can be set with correct values"""
        city = City()
        city.state_id = "CA"
        city.name = "San Francisco"
        self.assertEqual(city.state_id, "CA")
        self.assertEqual(city.name, "San Francisco")

if __name__ == '__main__':
    unittest.main()

