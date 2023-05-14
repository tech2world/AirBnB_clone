#!/usr/bin/pyhton3
"""Test for base_model"""

import unittest
from datetime import datetime, time
import time
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """test cases for all instances, functions in the BaseModel"""
    def setUp(self):
        """set up test methods"""
        self.model = BaseModel()

    def tearDown(self):
        """tear down test method"""
        del self.model

    def test_id(self):
        """test id"""
        self.assertIsNotNone(self.model.id)
        self.assertIsInstance(self.model.id, str)

    def test_created_at(self):
        """test created_at method"""
        self.assertIsNotNone(self.model.created_at)
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at(self):
        """test updated_at method"""
        self.assertIsNotNone(self.model.updated_at)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str(self):
        """test the __str__ method"""
        string = "[{}] ({}) {}".format(
            self.model.__class__.__name__, self.model.id, self.model.__dict__)
        self.assertEqual(string, str(self.model))

    def test_save(self):
        """Test save() method"""
        old_updated_at = self.model.updated_at
        time.sleep(0.1)
        self.model.save()
        new_updated_at = self.model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict(self):
        """test to_dict method"""
        dict_copy = self.model.__dict__.copy()
        dict_copy['__class__'] = 'BaseModel'
        dict_copy['created_at'] = dict_copy['created_at'].isoformat()
        dict_copy['updated_at'] = dict_copy['updated_at'].isoformat()
        self.assertDictEqual(dict_copy, self.model.to_dict())


if __name__ == '__main__':
    unittest.main()
