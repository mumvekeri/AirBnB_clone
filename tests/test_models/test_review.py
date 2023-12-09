#!/usr/bin/python3
"""Review test cases"""

# Import the unittest module and the Review class
import unittest
from review import Review

# Define a test class that inherits from unittest.TestCase
class TestReview(unittest.TestCase):

    # Define a setUp method to create an instance of Review
    def setUp(self):
        self.review = Review()

    # Define a tearDown method to delete the instance of Review
    def tearDown(self):
        del self.review

    # Define a test method to check the initialization of the instance
    def test_init(self):
        # Check that the instance is a subclass of BaseModel
        self.assertIsInstance(self.review, BaseModel)
        # Check that the instance has the correct attributes
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))
        # Check that the attributes have the correct default values
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    # Define a test method to check the string representation of the instance
    def test_str(self):
        # Check that the string representation has the correct format
        expected = "[{}] ({}) {}".format(self.review.class.__name, self.review.id, self.review.__dict_)
        self.assertEqual(str(self.review), expected)

    # Define a test method to check the to_dict method of the instance
    def test_to_dict(self):
        # Call the to_dict method
        review_dict = self.review.to_dict()
        # Check that the returned value is a dictionary
        self.assertIsInstance(review_dict, dict)
        # Check that the dictionary has the correct keys and values
        self.assertEqual(review_dict["class"], self.review._class.__name_)
        self.assertEqual(review_dict["id"], self.review.id)
        self.assertEqual(review_dict["created_at"], self.review.created_at.isoformat())
        self.assertEqual(review_dict["updated_at"], self.review.updated_at.isoformat())
        self.assertEqual(review_dict["place_id"], self.review.place_id)
        self.assertEqual(review_dict["user_id"], self.review.user_id)
        self.assertEqual(review_dict["text"], self.review.text)

    # Define a test method to check the corner case of passing kwargs to the instance
    def test_init_kwargs(self):
        # Create a dictionary of kwargs
        kwargs = {
            "_class": "Test",
            "id": "1234",
            "created_at": "2023-12-09T18:06:20.000000",
            "updated_at": "2023-12-09T18:06:20.000000",
            "place_id": "5678",
            "user_id": "9012",
            "text": "Great place!"
        }
        # Create an instance of Review with kwargs
        review = Review(**kwargs)
        # Check that the instance has the correct attributes from kwargs
        self.assertEqual(review.id, kwargs["id"])
        self.assertEqual(review.created_at, datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(review.updated_at, datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(review.place_id, kwargs["place_id"])
        self.assertEqual(review.user_id, kwargs["user_id"])
        self.assertEqual(review.text, kwargs["text"])
        # Check that the instance is a subclass of BaseModel
        self.assertIsInstance(review, BaseModel)
        # Check that the instance has the correct class name
        self.assertEqual(review._class, Review)

# Run the tests
if _name_ == "_main_":
    unittest.main()
