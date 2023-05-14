#!/usr/bin/python3
"""Defines unittests for models/amenity.py."""
import datetime
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Unittests for Amenity."""

    def test_instantiation(self):
        """Test instantiation of Amenity class."""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_reinstantiation(self):
        """Test reinstantiation of Amenity class."""
        amenity = Amenity()
        amenity.name = "Wifi"
        self.assertEqual(amenity.name, "Wifi")

    def test_str(self):
        """Test __str__ method of Amenity class."""
        amenity = Amenity()
        self.assertEqual(str(amenity), "[Amenity] ({}) {}".format(
            amenity.id, amenity.__dict__))

    def test_save(self):
        """Test save method of Amenity class."""
        amenity = Amenity()
        amenity.save()
        self.assertNotEqual(amenity.created_at, amenity.updated_at)

    def test_dict(self):
        """Test to_dict method of Amenity class."""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertEqual(amenity_dict["created_at"],
                         amenity.created_at.isoformat())
        self.assertEqual(amenity_dict["updated_at"],
                         amenity.updated_at.isoformat())
        self.assertEqual(amenity_dict.get("name"), None)

    def test_dict_to_instance(self):
        """Test dict_to_instance method of Amenity class."""
        amenity_dict = {
            "id": "b6a6bba8-85bc-4a0c-b5a5-5a6b44d6fbf2",
            "name": "Wifi",
            "created_at": "2023-05-14T12:29:32.579031",
            "updated_at": "2023-05-14T12:29:32.579031",
            "__class__": "Amenity"
        }
        amenity = BaseModel.dict_to_instance(amenity_dict)
        self.assertIsInstance(amenity, Amenity)
        self.assertEqual(amenity.id, "b6a6bba8-85bc-4a0c-b5a5-5a6b44d6fbf2")
        self.assertEqual(amenity.name, "Wifi")
        self.assertEqual(amenity.created_at, datetime.datetime(2023, 5, 14, 12, 29, 32, 579031))
        self.assertEqual(amenity.updated_at, datetime.datetime(2023, 5, 14, 12, 29, 32, 579031))


if __name__ == "__main__":
    unittest.main()
