#!/usr/bin/env python3
"""
"""
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_attribute_name(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, "")
        self.assertTrue(type(amenity.name) == str)


if __name__ == '__main__':
    unittest.main()
