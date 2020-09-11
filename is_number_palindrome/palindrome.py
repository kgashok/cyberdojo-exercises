import math


# solution requires two traversals
def is_number_palindrome(number):
    digits = []
    number = abs(number)
    while number:
        digits.append(number % 10)
        number = number // 10
    print(digits)
    for i in range(len(digits) // 2):
        if digits[i] is not digits[-i - 1]:
            return False
    return True

# reverse the digits and check if same


def is_number_palindrome(number):
    result, n_remaining = 0, abs(number)

    while n_remaining:
        result = 10 * result + n_remaining % 10
        n_remaining //= 10

    if number < 0:
        return result == -number
    return result == number

# Use MSD mask to reverse number


def is_number_palindrome(number):

    number = abs(number)

    try:
        number_of_digits = math.floor(math.log10(number) + 1)
    except ValueError:
        # to handle number zero
        number_of_digits = 1

    msd_mask = 10 ** (number_of_digits - 1)

    while number:
        if number // msd_mask != number % 10:
            return False
        number %= msd_mask
        number //= 10
        msd_mask //= 100

    return True

# using a generator


def is_number_palindrome(number):

    def generate_digits():
        n = abs(number)
        while n:
            yield n % 10
            n //= 10

    dlist = list(generate_digits())

    return all(dlist[i] == dlist[-i - 1]
               for i in range(len(dlist) // 2)
               )
