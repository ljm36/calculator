import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        test_add = CsvReader('/src/Unit Test Addition.csv').data
        for row in test_add:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtract_method_calculator(self):
        test_sub = CsvReader('/src/Unit Test Subtraction.csv').data
        for row in test_sub:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_multiplication_method_calculator(self):
        test_multiplication = CsvReader('/src/Unit Test Multiplication.csv').data
        for row in test_multiplication:
            self.assertEqual(self.calculator.multiplication(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_division_method_calculator(self):
        test_division = CsvReader('/src/Unit Test Division.csv').data
        self.assertEqual(self.calculator.division(row['Value 1'], row['Value 2']), int(row['Result']))
        self.assertEqual(self.calculator.result, int(row['Result']))

    def test_square_method_calculator(self):
        self.assertEqual(self.calculator.square(5), 25)
        self.assertEqual(self.calculator.result, 25)

    def test_root_method_calculator(self):
        self.assertEqual(self.calculator.root(16), 4)
        self.assertEqual(self.calculator.result, 4)


if __name__ == '__main__':
    unittest.main()
