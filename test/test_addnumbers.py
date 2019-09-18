import unittest
from src.add_numbers import SumOfNumbers


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.sumClass = SumOfNumbers(1, 2)

    def test_sum(self):
        self.assertEqual(3, self.sumClass.sum_no_arithmetic_operators(), msg="addition of 1 and 2 should give 3")

    def test_negative_integer(self):
        self.assertEqual(-3, self.sumClass.calculate(-1, -2), msg="addition of 1 and 2 should give 3")

    def test_invalid_sum(self):
        self.assertRaises(Exception,  self.sumClass.calculate, None, None)

    def test_large_sum(self):
        self.assertEqual(24691357824, self.sumClass.calculate(12345678912, 12345678912),
                         msg="current implementation cannot handle large numbers")


if __name__ == '__main__':
    unittest.main()
