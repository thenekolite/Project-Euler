def multiples_3_or_5(num):

    return True if num % 3 == 0 or num % 5 == 0 else False


numbers = list(range(1, 1000))

numbers_multiplies_3_or_5 = list(
    filter(lambda num: multiples_3_or_5(num), numbers))

total = sum(numbers_multiplies_3_or_5)

print(numbers_multiplies_3_or_5)
print(total)
