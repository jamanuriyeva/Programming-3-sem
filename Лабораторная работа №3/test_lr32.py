import unittest
from lr32 import calculate

class TestCalculate(unittest.TestCase):

    def test_calc1(self):
        self.assertEqual(calculate(1, 2, 3, operator='+'), 6)

    def test_calc2(self):
        self.assertEqual(calculate(10, 5, 3, operator='-'), 2)


    def test_calc3(self):
        self.assertEqual(calculate(2.587, 3.223, 4.111, operator='*'), 34.277111)


    def test_calc4(self):
        self.assertEqual(calculate(10, 2, operator='/'), 5)


    def test_calc5(self):
        self.assertEqual(calculate(10, 0, operator='/'), "You can't divide by zero!")

    def test_calc6(self):
        self.assertEqual(calculate(1, 2, 3, 4, 5, 6, 7, operator='medium'), 4)

    def test_calc7(self):
        self.assertEqual(calculate(5, 2, 3, 5, 4, 5, operator='varians'), 1.6)

    def test_calc8(self):
        self.assertEqual(calculate(2, 4, 4, 4, 5, 5, 7, 9,  operator='std_deviation'), 2.13809)

    def test_calc9(self):
        self.assertEqual(calculate(2, 6, 3, 4, 6, 9, 1, 3, operator='median'), 3.5)

    def test_calc10(self):
        self.assertEqual(calculate(2, 6, 3, 4, 6, 9, 1, 3, operator='IQR'), 4)


if __name__ == '__main__':
    unittest.main()