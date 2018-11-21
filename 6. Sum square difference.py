
# 1^2 + 2^2 + ... + 10^2 = 385


def sum_of_squares(n):

    return (n * (n + 1) * (2 * n + 1)) // 6

# (1 + 2 + ... + 10)^2 = 55^2 = 3025


def square_of_sum(n):

    return ((n * (n + 1)) // 2) ** 2


result = square_of_sum(100) - sum_of_squares(100)

print(result)
