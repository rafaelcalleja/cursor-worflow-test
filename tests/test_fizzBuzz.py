# tests/test_fizzBuzz.py
import unittest
from src.fizzBuzz import fizzbuzz # Assuming the function is named fizzbuzz

# [RATIONALE] Using unittest for standard Python testing framework.
# Tests cover standard FizzBuzz cases: divisible by 3, 5, both, and neither.

class TestFizzBuzz(unittest.TestCase):
    """Test suite for the fizzbuzz function."""

    def test_fizz(self):
        """Test that numbers divisible by 3 return 'Fizz'."""
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(6), "Fizz")
        # [OBSERVED_FAILURE_CONTEXT] Initial implementation might miss edge cases like 0 or negatives if not considered.
        # Adding 9 to cover another multiple of 3.
        self.assertEqual(fizzbuzz(9), "Fizz")

    def test_buzz(self):
        """Test that numbers divisible by 5 return 'Buzz'."""
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(10), "Buzz")
        # Adding 20 to cover another multiple of 5.
        self.assertEqual(fizzbuzz(20), "Buzz")

    def test_fizzbuzz(self):
        """Test that numbers divisible by both 3 and 5 return 'FizzBuzz'."""
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fizzbuzz(30), "FizzBuzz")
        # Adding 45 to cover another multiple of 15.
        self.assertEqual(fizzbuzz(45), "FizzBuzz")

    def test_number(self):
        """Test that numbers not divisible by 3 or 5 return the number itself."""
        self.assertEqual(fizzbuzz(1), 1)
        self.assertEqual(fizzbuzz(2), 2)
        self.assertEqual(fizzbuzz(4), 4)
        self.assertEqual(fizzbuzz(7), 7)

if __name__ == '__main__':
    unittest.main() 