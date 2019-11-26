import numpy as np
from math import sqrt


def is_perfect_square(n):
    '''
    is_perfect_square, accepts a number and returns True if it's a perfect square
    and False if it's not. A perfect square is any number which has an integer
    square root. So 25 is a perfect square but 24 is not, 9 is a perfect square
    but 8 is not, 100 is a perfect square but 1000 is not.
    '''
    if type(n) == int or float:
        if n > 0:
            dey = round(sqrt(n))
            if dey ** 2 == n:
                return True
        return False


print(is_perfect_square(25))
print(is_perfect_square(8))
print(is_perfect_square(100))
print(is_perfect_square(1000))
print(is_perfect_square(-1))
# print(is_perfect_square('25'))
print(is_perfect_square(4624000000000000))
