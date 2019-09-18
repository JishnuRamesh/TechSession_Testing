
from add_numbers import SumOfNumbers


class DoubleBiggest:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def find_double_of_bigger(self):

        if self.x >= self.y:
            return SumOfNumbers(self.x, self.x).sum_no_arithmetic_operators()
        else:
            return SumOfNumbers(self.y, self.y).sum_no_arithmetic_operators()

    # refactor example
    def computeBigger(self, x, y):
        self.x = x
        self.y = y
        return self.find_double_of_bigger()


if __name__ == "__main__":
    doubleBiggest = DoubleBiggest(-10, 0)
    print(doubleBiggest.find_double_of_bigger())