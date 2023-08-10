#!/usr/bin/env python3
"""
Unittest for ```State``` class
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    def test_attributes(self):
        state = State()
        self.assertEqual(state.name, "")


if __name__ == '__main__':
    unittest.main()
