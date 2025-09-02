import unittest
from divide import divide_numbers


class TestDivide(unittest.TestCase):
    def test_divide_normal(self):
        self.assertEqual(divide_numbers(10, 2), 5.0)

    def test_divide_negative(self):
        self.assertEqual(divide_numbers(-9, 3), -3.0)

    def test_divide_by_zero(self):
        self.assertEqual(divide_numbers(10, 0), "Error: Cannot divide by zero.")


if __name__ == "__main__":
    unittest.main()
