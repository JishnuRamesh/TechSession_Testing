
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
        return self.sum_no_arithmetic_operators()

    def sum_no_arithmetic_operators(self):
    # add negative accepted

        # Exception example
        if type(self.x) != int or type(self.y) != int:
            raise Exception("X and Y should be numbers to add them")

        # logic change example
        # if self.x < 0 or self.y < 0:
        #     return 0

        while True:
            carry = self.x & self.y
            self.x = self.x ^ self.y
            self.y = carry << 1
            if self.y == 0:
                break
        return self.x


if __name__ == "__main__":
    sumClass = SumOfNumbers(4,6)
    print(sumClass.sum_no_arithmetic_operators())
    print(sumClass.calculate(2,3))