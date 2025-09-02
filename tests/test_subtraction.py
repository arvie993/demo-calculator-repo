import unittest
from subtraction import subtraction


class TestSubtraction(unittest.TestCase):
    def test_subtraction_two_numbers(self):
        self.assertEqual(subtraction(10, 3), 7)

    def test_subtraction_multiple_numbers(self):
        self.assertEqual(subtraction(20, 5, 3, 2), 10)

    def test_subtraction_with_negatives(self):
        self.assertEqual(subtraction(5, -3, -2), 10)

    def test_subtraction_raises_on_insufficient_args(self):
        with self.assertRaises(ValueError):
            subtraction(1)
        with self.assertRaises(ValueError):
            subtraction()


if __name__ == "__main__":
    unittest.main()
