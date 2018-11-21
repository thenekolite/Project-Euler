from math import gcd
from functools import reduce


def lcm(a, b):

    # print(f"a = {a}, b = {b}, a * b = {a * b}, gcd(a, b) = {gcd(a, b)}, (a * b) // gcd(a, b) = {(a * b) // gcd(a, b)}")
    # print()
    return (a * b) // gcd(a, b)


result = reduce(lcm, range(1, 11))

print(result)
