# test_primematrix.py
"""
Tests for PrimeMatrix module.
"""

import unittest
from primematrix import PrimeMatrix

class TestPrimeMatrix(unittest.TestCase):
    """Test cases for PrimeMatrix class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PrimeMatrix()
        self.assertIsInstance(instance, PrimeMatrix)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PrimeMatrix()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
