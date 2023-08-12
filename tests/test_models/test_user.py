#!/usr/bin/env python3
"""
Unittest for ```User``` class
"""
import unittest
from models.user import User
import models.user


class TestUser(unittest.TestCase):
    """Test User class"""

    def test_module_doc(self):
        self.assertIsNotNone(models.user.__doc__)

    def test_class_doc(self):
        self.assertIsNotNone(User.__doc__)

    def test_attribute_email(self):
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "")
        self.assertTrue(type(user.email) == str)

    def test_attribute_password(self):
        user = User()
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, "")
        self.assertTrue(type(user.password) == str)

    def test_attribute_first_name(self):
        user = User()
        self.assertTrue(hasattr(user, "first_name"))
        self.assertEqual(user.first_name, "")
        self.assertTrue(type(user.first_name) == str)

    def test_attribute_last_name(self):
        user = User()
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.last_name, "")
        self.assertTrue(type(user.last_name) == str)


if __name__ == "__main__":
    unittest.main()
