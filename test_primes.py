import unittest
from primes import is_prime

class PrimesTestCase(unittest.TestCase):
    """Tests for `primes.py`."""

    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(is_prime(5))

    def test_is_one_not_a_prime(self):
        self.assertFalse(is_prime(1))

    def test_is_negative_three_not_a_prime(self):
        self.assertFalse(is_prime(-3))

    def test_input_validation_letter(self):
        self.assertFalse('a')

if __name__ == '__main__':
    unittest.main()