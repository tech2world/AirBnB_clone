#!/usr/bin/python3
"""Unittest for City"""
import unittest
from models.city import City
from models.base_model import BaseModel
from datetime import datetime
import time


class TestCity(unittest.TestCase):
    """Tests for City"""
    def setUp(self):
        """set up for testing"""
        self.city = City()

    def test_isinstance(self):
        """Test if the instance belongs to BaseModel"""
        self.assertIsInstance(self.city, BaseModel)

    def test_attribute(self):
        """Test if it has attribute"""
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertEqual(self.city.state_id, "")
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(self.city.name, "")

    def test_to_dict(self):
        """Test the to_dict method"""
        city_dict = self.city.to_dict()
        self.assertTrue(type(city_dict) is dict)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(type(city_dict['created_at']), str)
        self.assertEqual(type(city_dict['updated_at']), str)
        self.assertNotIn('_sa_instance_state', city_dict)

    def test_save(self):
        """Test if the save method works"""
        updated_at = self.city.updated_at
        time.sleep(0.1)  # Wait for a short time to avoid time resolution issues
        self.city.save()
        self.assertNotEqual(updated_at, self.city.updated_at)

    def test_dict(self):
        """Test if dictionary representation is correct"""
        city = City()
        city_dict = city.to_dict()
        for attr in city_dict:
            if attr == '__class__':
                self.assertEqual(city_dict[attr], 'City')
            elif attr == 'created_at' or attr == 'updated_at':
                self.assertEqual(city_dict[attr], city.created_at.isoformat())
            else:
                self.assertEqual(city_dict[attr], getattr(city, attr))

    def test_dict_to_instance(self):
        """Test if an instance is created from dictionary"""
        city_dict = {'__class__': 'City',
                     'id': '1234',
                     'created_at': '2022-05-12T12:30:45.123456',
                     'updated_at': '2022-05-12T12:30:45.123456',
                     'state_id': '5678',
                     'name': 'San Francisco'}
        city = City.dict_to_instance(city_dict)
        self.assertIsInstance(city, City)
