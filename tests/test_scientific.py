import math
import unittest
from scientific import (
    sin, cos, tan,
    asin, acos, atan,
    log, log10, log2,
    exp, power, sqrt
)


class TestScientific(unittest.TestCase):
    # Trigonometric
    def test_sin(self):
        self.assertAlmostEqual(sin(math.pi / 2), 1.0, places=9)

    def test_cos(self):
        self.assertAlmostEqual(cos(0), 1.0, places=9)

    def test_tan(self):
        self.assertAlmostEqual(tan(0), 0.0, places=9)

    def test_asin(self):
        self.assertAlmostEqual(asin(1), math.pi / 2, places=9)

    def test_acos(self):
        self.assertAlmostEqual(acos(1), 0.0, places=9)

    def test_atan(self):
        self.assertAlmostEqual(atan(1), math.pi / 4, places=9)

    # Logarithmic
    def test_log_natural(self):
        self.assertAlmostEqual(log(math.e), 1.0, places=9)

    def test_log_with_base(self):
        self.assertAlmostEqual(log(8, base=2), 3.0, places=9)

    def test_log10(self):
        self.assertAlmostEqual(log10(100), 2.0, places=9)

    def test_log2(self):
        self.assertAlmostEqual(log2(8), 3.0, places=9)

    def test_log_domain_error(self):
        with self.assertRaises(ValueError):
            log(-1)

    # Exponential
    def test_exp(self):
        self.assertAlmostEqual(exp(1), math.e, places=9)

    def test_power(self):
        self.assertEqual(power(2, 3), 8.0)

    # Square root
    def test_sqrt(self):
        self.assertEqual(sqrt(16), 4.0)

    def test_sqrt_domain_error(self):
        with self.assertRaises(ValueError):
            sqrt(-1)


if __name__ == "__main__":
    unittest.main()
