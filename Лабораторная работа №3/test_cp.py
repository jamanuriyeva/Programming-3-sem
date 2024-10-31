import unittest
from convert_precision import convert_precision

class TestCalculate(unittest.TestCase):

    def test_cp1(self):
        self.assertEqual(convert_precision(0.00001), 5)

    def test_cp2(self):
        self.assertEqual(convert_precision(0.00000001), 8)

    def test_cp3(self):
        self.assertEqual(convert_precision(0), "Tolerance cannot be zero.")


if __name__ == '__main__':
    unittest.main()