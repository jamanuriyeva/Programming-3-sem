import unittest
from proga1 import calculate


class TestCalculations(unittest.TestCase):

    def test_calc(self):
        self.assertEqual(calculate(3, 4, "+"), 7)
        self.assertEqual(calculate(10, 2, "/"), 5.0)
        self.assertEqual(calculate(5, 4, "-"), 1.0)
        self.assertEqual(calculate(3, 4, "*"), 12.0)
        self.assertEqual(calculate(3, 0, "/"), "You can't divide by zero!")


if __name__ == '__main__':

    unittest.main()
