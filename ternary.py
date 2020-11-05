class Ternary(object):
    """ Class to represent ternary representation of a number"""

    def __init__(self, num: int):
        if 0 <= num <= 26:
            self.nines = num // 9
            self.threes = (num % 9) // 3
            self.ones = num % 3
        else:
            self.nines = -1
            self.threes = -1
            self.ones = -1
            raise ValueError("invalid number . it must be between 0 and 26")

    def __str__(self):
        return "nines:{0}, threes:{1}, ones:{2}".format(self.nines, self.threes, self.ones)


if __name__ == '__main__':
    x = int(input("enter value : "))
    ternary_x = Ternary(x)
    print(ternary_x.__str__())