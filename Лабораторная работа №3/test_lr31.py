import unittest
from lr31 import calculate

class TestCalculate(unittest.TestCase):

    def test_calc1(self):
        self.assertEqual(calculate(1, 2, 3, operator='+'), 6)

    def test_calc2(self):
        self.assertEqual(calculate(10, 5, 3, operator='-'), 2)


    def test_calc3(self):
        self.assertEqual(calculate(2.587, 3.223, 4.111, operator='*'), 34.277111)


    def test_calc14(self):
        self.assertEqual(calculate(10, 2, operator='/'), 5)


    def test_calc5(self):
        self.assertEqual(calculate(10, 0, operator='/'), "You can't divide by zero!")


if __name__ == '__main__':
    unittest.main()