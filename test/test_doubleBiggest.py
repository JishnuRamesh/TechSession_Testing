import unittest
from src.double_of_biggest_number import DoubleBiggest


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.double_biggest = DoubleBiggest(2,3)

    def test_double3shouldgive6(self):
        self.assertEqual(self.double_biggest.find_double_of_bigger(), 6, msg='double of t3 must be 6')

    def test_doubleNegative(self):
        self.assertEqual(self.double_biggest.computeBigger(-10, -4), -8, msg='double of -4 must be -8')

    def test_doubleZero(self):
        self.assertEqual(self.double_biggest.computeBigger(-1, 0), 0, msg='double of 0 must be 0')


if __name__ == '__main__':
    unittest.main()
