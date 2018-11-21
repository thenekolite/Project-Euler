def is_palindrome(number):
    return str(number) == str(number)[::-1]


def get_palindrome_numbers(limit):

    max_value = 0
    multiplies = ""

    for i in range(100, limit):

        for j in range(100, limit):

            multiplies_value = i * j

            if is_palindrome(multiplies_value) and multiplies_value > max_value:
                max_value = multiplies_value
                multiplies = f"{i} x {j}"

    return max_value, multiplies


palindrom_values = get_palindrome_numbers(1000)

print(palindrom_values)
