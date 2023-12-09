#!/usr/bin/python3
"""User test cases"""

# Import the unittest module and the User class
import unittest
from user import User

# Define a test class that inherits from unittest.TestCase
class TestUser(unittest.TestCase):

    # Define a setUp method to create an instance of User
    def setUp(self):
        self.user = User()

    # Define a tearDown method to delete the instance of User
    def tearDown(self):
        del self.user

    # Define a test method to check the initialization of the instance
    def test_init(self):
        # Check that the instance is a subclass of BaseModel
        self.assertIsInstance(self.user, BaseModel)
        # Check that the instance has the correct attributes
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))
        # Check that the attributes have the correct default values
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    # Define a test method to check the string representation of the instance
    def test_str(self):
        # Check that the string representation has the correct format
        expected = "[{}] ({}) {}".format(self.user.class.__name, self.user.id, self.user.__dict_)
        self.assertEqual(str(self.user), expected)

    # Define a test method to check the to_dict method of the instance
    def test_to_dict(self):
        # Call the to_dict method
        user_dict = self.user.to_dict()
        # Check that the returned value is a dictionary
        self.assertIsInstance(user_dict, dict)
        # Check that the dictionary has the correct keys and values
        self.assertEqual(user_dict["class"], self.user._class.__name_)
        self.assertEqual(user_dict["id"], self.user.id)
        self.assertEqual(user_dict["created_at"], self.user.created_at.isoformat())
        self.assertEqual(user_dict["updated_at"], self.user.updated_at.isoformat())
        self.assertEqual(user_dict["email"], self.user.email)
        self.assertEqual(user_dict["password"], self.user.password)
        self.assertEqual(user_dict["first_name"], self.user.first_name)
        self.assertEqual(user_dict["last_name"], self.user.last_name)

    # Define a test method to check the corner case of passing kwargs to the instance
    def test_init_kwargs(self):
        # Create a dictionary of kwargs
        kwargs = {
            "_class": "Test",
            "id": "1234",
            "created_at": "2023-12-09T18:06:20.000000",
            "updated_at": "2023-12-09T18:06:20.000000",
            "email": "test@example.com",
            "password": "secret",
            "first_name": "Alice",
            "last_name": "Smith"
        }
        # Create an instance of User with kwargs
        user = User(**kwargs)
        # Check that the instance has the correct attributes from kwargs
        self.assertEqual(user.id, kwargs["id"])
        self.assertEqual(user.created_at, datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(user.updated_at, datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(user.email, kwargs["email"])
        self.assertEqual(user.password, kwargs["password"])
        self.assertEqual(user.first_name, kwargs["first_name"])
        self.assertEqual(user.last_name, kwargs["last_name"])
        # Check that the instance is a subclass of BaseModel
        self.assertIsInstance(user, BaseModel)
        # Check that the instance has the correct class name
        self.assertEqual(user._class, User)

# Run the tests
if _name_ == "_main_":
    unittest.main()
