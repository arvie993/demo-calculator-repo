import sys
import subprocess
import unittest
from multiply import multiply_numbers


class TestMultiply(unittest.TestCase):
    def test_multiply_integers(self):
        self.assertEqual(multiply_numbers(4, 5), 20)

    def test_multiply_floats(self):
        self.assertAlmostEqual(multiply_numbers(2.5, 4), 10.0, places=7)

    def test_cli_integers_prints_int(self):
        out = subprocess.check_output([sys.executable, "multiply.py", "2", "3"], text=True, cwd=str("."))
        self.assertEqual(out.strip(), "6")

    def test_cli_float_and_int_prints_float(self):
        out = subprocess.check_output([sys.executable, "multiply.py", "2.5", "2"], text=True, cwd=str("."))
        self.assertEqual(out.strip(), "5.0")


if __name__ == "__main__":
    unittest.main()
