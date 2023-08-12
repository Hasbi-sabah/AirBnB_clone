#!/usr/bin/env python3
"""
"""
import unittest
from models.amenity import Amenity
import models.amenity


class TestAmenity(unittest.TestCase):
    def test_attribute_name(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")
        self.assertTrue(type(amenity.name) == str)

    def test_class_doc(self):
        self.assertIsNotNone(Amenity.__doc__)

    def test_module_doc(self):
        self.assertIsNotNone(models.amenity.__doc__)


if __name__ == "__main__":
    unittest.main()
