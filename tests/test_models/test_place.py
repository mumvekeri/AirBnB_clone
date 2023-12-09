#!/usr/bin/python3
import unittest
from place import Place

# Define a test class that inherits from unittest.TestCase
class TestPlace(unittest.TestCase):

    # Define a setUp method to create an instance of Place
    def setUp(self):
        self.place = Place()

    # Define a tearDown method to delete the instance of Place
    def tearDown(self):
        del self.place

    # Define a test method to check the initialization of the instance
    def test_init(self):
        # Check that the instance is a subclass of BaseModel
        self.assertIsInstance(self.place, BaseModel)
        # Check that the instance has the correct attributes
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertTrue(hasattr(self.place, "amenity_ids"))
        # Check that the attributes have the correct default values
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    # Define a test method to check the string representation of the instance
    def test_str(self):
        # Check that the string representation has the correct format
        expected = "[{}] ({}) {}".format(self.place.class.__name, self.place.id, self.place.__dict_)
        self.assertEqual(str(self.place), expected)

    # Define a test method to check the to_dict method of the instance
    def test_to_dict(self):
        # Call the to_dict method
        place_dict = self.place.to_dict()
        # Check that the returned value is a dictionary
        self.assertIsInstance(place_dict, dict)
        # Check that the dictionary has the correct keys and values
        self.assertEqual(place_dict["class"], self.place._class.__name_)
        self.assertEqual(place_dict["id"], self.place.id)
        self.assertEqual(place_dict["created_at"], self.place.created_at.isoformat())
        self.assertEqual(place_dict["updated_at"], self.place.updated_at.isoformat())
        self.assertEqual(place_dict["city_id"], self.place.city_id)
        self.assertEqual(place_dict["user_id"], self.place.user_id)
        self.assertEqual(place_dict["name"], self.place.name)
        self.assertEqual(place_dict["description"], self.place.description)
        self.assertEqual(place_dict["number_rooms"], self.place.number_rooms)
        self.assertEqual(place_dict["number_bathrooms"], self.place.number_bathrooms)
        self.assertEqual(place_dict["max_guest"], self.place.max_guest)
        self.assertEqual(place_dict["price_by_night"], self.place.price_by_night)
        self.assertEqual(place_dict["latitude"], self.place.latitude)
        self.assertEqual(place_dict["longitude"], self.place.longitude)
        self.assertEqual(place_dict["amenity_ids"], self.place.amenity_ids)

    # Define a test method to check the corner case of passing kwargs to the instance
    def test_init_kwargs(self):
        # Create a dictionary of kwargs
        kwargs = {
            "_class": "Test",
            "id": "1234",
            "created_at": "2023-12-09T18:06:20.000000",
            "updated_at": "2023-12-09T18:06:20.000000",
            "city_id": "5678",
            "user_id": "9012",
            "name": "My Place",
            "description": "A nice place",
            "number_rooms": 3,
            "number_bathrooms": 2,
            "max_guest": 5,
            "price_by_night": 100,
            "latitude": -26.2041,
            "longitude": 28.0473,
            "amenity_ids": ["3456", "7890"]
        }
        # Create an instance of Place with kwargs
        place = Place(**kwargs)
        # Check that the instance has the correct attributes from kwargs
        self.assertEqual(place.id, kwargs["id"])
        self.assertEqual(place.created_at, datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(place.updated_at, datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(place.city_id, kwargs["city_id"])
        self.assertEqual(place.user_id, kwargs["user_id"])
        self.assertEqual(place.name, kwargs["name"])
        self.assertEqual(place.description, kwargs["description"])
        self.assertEqual(place.number_rooms, kwargs["number_rooms"])
        self.assertEqual(place.number_bathrooms, kwargs["number_bathrooms"])
        self.assertEqual(place.max_guest, kwargs["max_guest"])
        self.assertEqual(place.price_by_night, kwargs["price_by_night"])
        self.assertEqual(place.latitude, kwargs["latitude"])
        self.assertEqual(place.longitude, kwargs["longitude"])
        self.assertEqual(place.amenity_ids, kwargs["amenity_ids"])
        # Check that the instance is a subclass of BaseModel
        self.assertIsInstance(place, BaseModel)
        # Check that the instance has the correct class name
        self.assertEqual(place._class, Place)

# Run the tests
if _name_ == "_main_":
    unittest.main()
