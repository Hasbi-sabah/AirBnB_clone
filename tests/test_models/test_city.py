#!/usr/bin/env python3
"""
Unittest for ```City``` class
"""
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """ Test City class"""
    def test_attributes(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == '__main__':
    unittest.main()
