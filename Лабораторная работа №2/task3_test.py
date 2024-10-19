import unittest
import task3


class TestCalculations(unittest.TestCase):

    def test_ruthenium_103(self):
        self.assertEqual(task3.radioactive_funcs["Ru_103"](100, 10), 83.71683896936682)

    def test_ruthenium_106(self):
        self.assertEqual(task3.radioactive_funcs["Ru_106"](100, 10), 98.13407587090127)


if __name__ == '__main__':

    unittest.main()
