#!/usr/bin/env python3
"""
Unittest for ```FileStorage```
"""
import unittest
import os
from models.engine.file_storage import FileStorage
import models.engine.file_storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    __file_path = "file.json"

    def test_module_doc(self):
        self.assertIsNotNone(models.engine.file_storage.__doc__)

    def test_class_doc(self):
        self.assertIsNotNone(FileStorage.__doc__)

    def setUp(self):
        """Create a strorage instance"""
        self.storage = FileStorage()

    def tearDown(self):
        """Remove the json file"""
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_initial_attributes(self):
        """Test it is a dictionary"""
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_all(self):
        """Test the all method"""
        all_obj = self.storage.all()
        self.assertIsInstance(all_obj, dict)
        self.assertIs(all_obj, self.storage._FileStorage__objects)

    def test_new(self):
        """Test the new method"""
        base_model = BaseModel()
        self.storage.new(base_model)
        key = "{}.{}".format(base_model.__class__.__name__, base_model.id)
        self.assertIn(key, self.storage._FileStorage__objects)

    def test_reload(self):
        """Test the reload method"""
        base_model = BaseModel()
        self.storage.new(base_model)
        self.storage.save()

        # Test updated attribute
        base_model.name = "Updated name"
        base_model.save()

        new_storage = FileStorage()
        new_storage.reload()
        key = "{}.{}".format(base_model.__class__.__name__, base_model.id)
        self.assertIn(key, self.storage._FileStorage__objects)
        reloaded_ins = new_storage.all()[key]
        #self.assertEqual(reloaded_ins.name, "Updated Name")


    def test_reload_with_no_file(self):
        """Test reload when json file doesn't exist does not raise error"""
        try:
            self.storage.reload()
        except FileNotFoundError:
            self.fail("Error raised")


if __name__ == "__main__":
    unittest.main()
