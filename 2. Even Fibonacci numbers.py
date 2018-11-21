from functools import reduce


def generete_fibonacci(limit):

    fibonacci_numbers = [1, 2]

    while fibonacci_numbers[-1] < limit:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])

    fibonacci_numbers.pop()

    return fibonacci_numbers


fibonacci_numbers = generete_fibonacci(4000000)

even_fibonacci_numbers = list(
    filter(lambda num: num % 2 == 0, fibonacci_numbers))

sum_of_even_fibonacci = reduce(lambda x, y: x + y, even_fibonacci_numbers)

print(sum_of_even_fibonacci)
