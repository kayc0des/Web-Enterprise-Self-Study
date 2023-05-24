import sys
from os.path import abspath, dirname
# Add the parent directory to the system path
parent_dir = abspath(dirname(dirname(__file__)))
sys.path.append(parent_dir)
# Import the BaseModel class from models subdirectory
from models.base_model import BaseModel
import unittest
from datetime import datetime
from unittest.mock import patch
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Test Class for BaseModel Module
    """

    def setUp(self):
        # Perform setup actions before each test method
        self.test_model = BaseModel()

    def test_initialization(self):
        """
        Test if test_model is an instance of BaseModel
        Test if test_model.id is an instance of a string
        Test if test_model.created_at and test_model.updated_at is an instance of a datetime
        """
        self.assertIsInstance(self.test_model, BaseModel)
        self.assertIsInstance(self.test_model.id, str)
        self.assertIsInstance(self.test_model.created_at, datetime)
        self.assertIsInstance(self.test_model.updated_at, datetime)

    def test_str(self):
        """
        Test string representation of test_model object
        """
        pass

    def test_save(self):
        """
        Test that initial updated_at differs from new updated_at when 
        test_model.save() is called
        """
        initial_updated_at = self.test_model.updated_at
        self.test_model.save()
        new_updated_at = self.test_model.updated_at
        self.assertNotEqual(initial_updated_at, new_updated_at)

    

if __name__ == '__main__':
    unittest.main()