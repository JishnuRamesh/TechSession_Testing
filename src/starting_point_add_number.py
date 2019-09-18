
"""

    This is a sample class to showcase how we can use unit testing


"""


class SumOfNumbers:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate(self, x, y):
        self.x = x
        self.y = y

    def sum_no_arithmetic_operators(self):

        while True:
            carry = self.x & self.y
            self.x = self.x ^ self.y
            self.y = carry << 1
            if self.y == 0:
                break
        return self.x


if __name__ == "__main__":
    sumClass = SumOfNumbers(3,None)
    sumClass.sum_no_arithmetic_operators()