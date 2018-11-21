import math


def get_factors(number):

    factors = []

    for i in range(1, int(math.sqrt(number) + 1)):
        if number % i == 0:
            factors.append(i)

    factors.append(number)

    return factors


def is_prime(number):

    return len(get_factors(number)) == 2


all_factors = get_factors(600851475143)

# prime_factors = list(filter(lambda num: is_prime(num), all_factors))

# max_factor = max(prime_factors)

# print(prime_factors)
# print(max_factor)

print(all_factors)
