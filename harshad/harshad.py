# harshad.py
#
# -------------------
# Input: integer
# Output: integer
# Generates the sum of all the digits in the number


def sum_digits(n):
    return sum(int(x) for x in str(n))

# -------------------
# Input: integer
# Output: Boolean
# Checks whether a number is a prime number or not


def is_prime(n):
    import math

    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

# -------------------
# Base Class with one method which checks if
# the given number is a Harshad number or not


class Harshad:
    def check(self, n):
        return (n % sum_digits(n) == 0)

# -------------------
# Derived class with one method which checks if
# the given number is a Hard harshad number or not


class StrongHarshad (Harshad):

    def check(self, n):
        return Harshad.check(self, n) and is_prime(n/sum_digits(n))
