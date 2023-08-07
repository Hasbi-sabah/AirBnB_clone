import unittest
from models.base_model import BaseModel
import uuid
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        # Create a new BaseModel instance before each test
        self.base_model = BaseModel()

    def test_id_is_uuid_string(self):
        # Check if the id is a valid UUID string
        self.assertTrue(uuid.UUID(self.base_model.id, version=4))

    def test_created_at_is_datetime(self):
        # Check if created_at is a datetime object
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        # Check if updated_at is a datetime object
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_updated_at_changes_on_save(self):
        # Check if updated_at changes when calling the save method
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        new_updated_at = self.base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_str_method(self):
        # Check if __str__ method returns the correct string format
        expected_str = f"[{self.base_model.__class__.__name__}] ({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), expected_str)

    def test_to_dict_method(self):
        # Check if to_dict method returns the correct dictionary representation
        dict_representation = self.base_model.to_dict()

        # Check if "__class__" key is present in the dictionary
        self.assertIn("__class__", dict_representation)

        # Check if "__class__" value is the class name of the object
        self.assertEqual(dict_representation["__class__"], self.base_model.__class__.__name__)

        # Check if created_at and updated_at are in ISO format
        self.assertTrue(datetime.fromisoformat(dict_representation["created_at"]))
        self.assertTrue(datetime.fromisoformat(dict_representation["updated_at"]))

        # Check if id is a valid UUID string in the dictionary
        self.assertTrue(uuid.UUID(dict_representation["id"], version=4))


    def test_init_with_kwargs(self):
        # Check if the __init__ method correctly sets instance attributes from kwargs

        # Simulate a dictionary with attribute names and their corresponding values
        kwargs = {
            "name": "John Doe",
            "age": 30,
            "created_at": "2023-08-05T12:34:56.789012",
            "updated_at": "2023-08-05T12:34:56.789012",
            "__class__": "NotAClass"
        }

        base_model_with_kwargs = BaseModel(**kwargs)

        # Check if the attributes are set correctly
        self.assertEqual(base_model_with_kwargs.name, kwargs["name"])
        self.assertEqual(base_model_with_kwargs.age, kwargs["age"])

        # Check if created_at and updated_at are converted to datetime objects
        expected_created_at = datetime.fromisoformat(kwargs["created_at"])
        expected_updated_at = datetime.fromisoformat(kwargs["updated_at"])
        self.assertEqual(base_model_with_kwargs.created_at, expected_created_at)
        self.assertEqual(base_model_with_kwargs.updated_at, expected_updated_at)

        # Check if "__class__" is not added as an attribute
        self.assertEqual(base_model_with_kwargs.__class__.__name__, "BaseModel")

    def test_init_with_kwargs_id_and_created_at(self):
        # Check if the __init__ method sets id and created_at when not provided in kwargs

        # Simulate a dictionary with attribute names and their corresponding values
        kwargs = {
            "id": 88,
            "name": "Jane Smith",
            "age": 25,
            "created_at": "2023-08-05T12:34:56.789012",
            "updated_at": "2023-08-05T12:34:56.789012",
        }

        base_model_with_kwargs = BaseModel(**kwargs)

        # Check if created_at is set as a datetime object
        expected_created_at = datetime.fromisoformat(kwargs["updated_at"])
        self.assertIsInstance(base_model_with_kwargs.created_at, datetime)
        self.assertEqual(base_model_with_kwargs.created_at, expected_created_at)

    def test_save_method(self):
        # Check if save method correctly updates the updated_at attribute

        # Get the initial value of updated_at
        initial_updated_at = self.base_model.updated_at

        # Call the save method
        self.base_model.save()

        # Get the new value of updated_at after calling save
        new_updated_at = self.base_model.updated_at

        # Check if updated_at has changed
        self.assertNotEqual(initial_updated_at, new_updated_at)

    def test_to_dict_method_with_extra_attributes(self):
        # Check if to_dict method returns the correct dictionary representation
        # even when extra attributes are added to the instance

        self.base_model.name = "Extra attribute"
        dict_representation = self.base_model.to_dict()

        # Check if the extra attribute "name" is present in the dictionary
        self.assertIn("name", dict_representation)
        self.assertEqual(dict_representation["name"], "Extra attribute")

if __name__ == "__main__":
    unittest.main()
