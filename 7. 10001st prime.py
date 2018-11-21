import math
import time


def is_prime(number):

    limit = int(math.sqrt(number)) + 1

    for i in range(2, limit):
        if number % i == 0:
            return False

    return True


def generete_primes(limit):

    number = 2
    primes = []

    while len(primes) < limit:
        if is_prime(number):
            primes.append(number)
        number += 1

    return primes


start_time = time.time()

prime_numbers = generete_primes(10001)

last_value = prime_numbers[-1]

print(last_value)
print(f"My program took {time.time() - start_time}s to run.")
