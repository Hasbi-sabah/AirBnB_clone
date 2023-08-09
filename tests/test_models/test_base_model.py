#!/usr/bin/env python3
"""
Unittest for ```base_model```
"""

import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """ Test the class ``BaseModel`` """

    def setup(self):
        pass

    def test_class_doc(self):
        """ Test ``BaseModel`` class for documentation"""
        self.assertIsNotNone(BaseModel.__doc__)

    def test_method_docs(self):
        """ Test methods in ``BaseModel`` for documentation"""
        methods = [
                BaseModel.__init__, BaseModel.__str__,
                BaseModel.save, BaseModel.to_dict
                ]
        for meth in methods:
            self.assertIsNotNone(meth.__doc__)

    def test_initial_attribute(self):
        """ Test object id"""
        test_model = BaseModel()
        test_model2 = BaseModel()

        # check if id exists, not NULL and a string
        self.assertTrue(hasattr(test_model, 'id'))
        self.assertIsNotNone(test_model.id)
        self.assertIsInstance(test_model.id, str)

        # Check if id is uuid
        self.assertTrue(uuid.UUID(test_model.id))

        # Check if two instances have the same id
        self.assertNotEqual(test_model.id, test_model2.id)

        # Check if created_at exist, not NULL, and it's from datetime
        self.assertTrue(hasattr(test_model, 'created_at'))
        self.assertIsNotNone(test_model.created_at)
        self.assertIsInstance(test_model.created_at, datetime)

        # Check if updated_at exist, not NULL, and it's from datetime
        self.assertTrue(hasattr(test_model, 'updated_at'))
        self.assertIsNotNone(test_model.updated_at)
        self.assertIsInstance(test_model.updated_at, datetime)

        # Check if updated_at time is after created_at
        self.assertGreater(test_model.updated_at, test_model.created_at)

        # Check that *args was not used
        test_with_arg = BaseModel("args")
        self.assertNotIn("args", test_with_arg.__dict__)


if __name__ == "__main__":
    unittest.main()
