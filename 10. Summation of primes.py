# author: Rizky Ramadhan
# date: November 20 2018

import time
import math


def is_prime(number):

    # untuk mendapatkan limit dari perulangan
    # yang akan dilakukan
    limit = int(math.sqrt(number)) + 1

    # perulangan berjalan dari 2 sampai limit
    # dimulai dari 2 karena 2 adalah prime number pertama
    for i in range(2, limit):

        # jika number mod i adalah 0, maka return false
        # contoh: 9 mod 3 -> false
        if number % i == 0:
            return False

    # selain itu maka return true
    return True


# *** solution 1 ***

# def get_prime_numbers(limit):

#     primes = [2]
#     number = 3

#     while primes[-1] < limit:

#         if is_prime(number):
#             primes.append(number)

#         number += 1

#     primes.pop()

#     return primes


# all_primes = get_prime_numbers(2000000)

# total = sum(all_primes)

# print(total)


# *** solution 2 ***

def get_sum_numbers(limit):

    # sum_of_prime = 2 karena 2 adalah prime pertama
    sum_of_prime = 2

    # number untuk perulangan dimulai dari 3
    # karena prime number setelah 2 adalah 3
    number = 3

    # perulangan dilakukan selama number kurang dari limit
    while number < limit:

        # jika merupakan bilagan prima,
        # maka tambahkan dengan sum_of_prime
        if is_prime(number):
            sum_of_prime += number

        # number += 2 agar bilangan genap tidak perlu dicek
        number += 2

    # return sum_of_prime
    return sum_of_prime


# awal program berjalan
start_time = time.time()

# dapatkan result
result = get_sum_numbers(2000000)

# tampilkan result
print(result)

# menampilkan lama nya waktu yang dibutuhkan
# untuk menjalankan program ini
# last time: 13.16s
print(f"This program took {time.time() - start_time:.2f}s to run!")
