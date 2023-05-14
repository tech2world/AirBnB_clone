#!/usr/bin/python3
"""unittest for Place class"""

import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Defines unittests for Place class"""

    def test_attributes(self):
        """Tests the class attributes of Place"""
        place = Place()
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))
        self.assertTrue(hasattr(place, "city_id"))
        self.assertTrue(hasattr(place, "user_id"))
        self.assertTrue(hasattr(place, "name"))
        self.assertTrue(hasattr(place, "description"))
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertTrue(hasattr(place, "latitude"))
        self.assertTrue(hasattr(place, "longitude"))
        self.assertTrue(hasattr(place, "amenity_ids"))

    def test_inheritance(self):
        """Tests if Place inherits from BaseModel"""
        place = Place()
        self.assertTrue(issubclass(type(place), BaseModel))

    def test_init(self):
        """Tests if __init__ method initializes attributes correctly"""
        place = Place(city_id="1234", user_id="5678", name="Test Place")
        self.assertEqual(place.city_id, "1234")
        self.assertEqual(place.user_id, "5678")
        self.assertEqual(place.name, "Test Place")

    def test_dict(self):
        """test the dictionary representation of a Place object"""
        place = Place()
        place_dict = place.to_dict()
        attrs = ["id", "created_at", "updated_at", "city_id", "__class__"]
        for attr in attrs:
            self.assertIn(attr, place_dict)

        self.assertEqual(place_dict["__class__"], "Place")

        place.city_id = "12345"
        place_dict = place.to_dict()
        self.assertEqual(place_dict["city_id"], "12345")

    def test_dict_to_instance(self):
        """Tests if dict_to_instance method returns a Place instance"""
        place_dict = {'__class__': 'Place',
                      'id': '1234',
                      'created_at': '2022-05-12T12:30:45.123456',
                      'updated_at': '2022-05-12T12:30:45.123456',
                      'city_id': '5678',
                      'user_id': '9101',
                      'name': 'Test Place'}
        place = Place.dict_to_instance(place_dict)
        self.assertIsInstance(place, Place)
        self.assertEqual(place.id, "1234")
        self.assertEqual(place.city_id, "5678")
        self.assertEqual(place.user_id, "9101")
        self.assertEqual(place.name, "Test Place")


if __name__ == "__main__":
    unittest.main()
