from functools import reduce
from operator import mul


def product(fracs):
    t = reduce(mul, fracs)
    return t.numerator, t.denominator
