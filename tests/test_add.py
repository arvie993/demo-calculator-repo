import unittest
from add import addition


class TestAddition(unittest.TestCase):
    def test_addition_integers(self):
        self.assertEqual(addition(2, 3), 5)

    def test_addition_floats(self):
        self.assertAlmostEqual(addition(2.5, 3.1), 5.6, places=7)

    def test_addition_negatives(self):
        self.assertEqual(addition(-2, -3), -5)

    def test_addition_mixed_signs(self):
        self.assertEqual(addition(-2, 3), 1)


if __name__ == "__main__":
    unittest.main()
