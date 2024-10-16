import proga1
import unittest
from proga1 import calculate


class TestCalculations(unittest.TestCase):

    def test_calc(self):
        self.assertEqual(calculate(3, 4, "+"), 7)


if __name__ == '__main__':

    unittest.main()
