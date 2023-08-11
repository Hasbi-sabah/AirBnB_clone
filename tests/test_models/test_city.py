#!/usr/bin/env python3
"""
Unittest for ```City``` class
"""
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """ Test City class"""
    def test_attribut_state_id(self):
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertEqual(city.state_id, "")
        self.assertTrue(type(city.state_id) == str)

    def test_attribut_name(self):
        city = City()
        self.assertTrue(hasattr(city, 'name'))
        self.assertEqual(city.name, "")
        self.assertTrue(type(city.name) == str)


if __name__ == '__main__':
    unittest.main()
