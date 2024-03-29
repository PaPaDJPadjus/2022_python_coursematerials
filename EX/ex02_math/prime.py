"""Prime numbers."""


def is_prime_number(number: int):
    """
    Check if the number is a prime number.

    Prime number is a natural number which is only divisible by 1 and itself. 0 and 1 are not prime numbers.

    Conditions:
    1. If number is a prime number, then return boolean True
    2. If number is not a prime number, then return boolean False

    param number: the number to check.
    return: boolean True if number is a prime number or False if number is not a prime number.
    """
    sum_total = 0
    for i in range(2, number + 1):
        if number % i == 0:
            sum_total += 1

    if sum_total == 1:
        return True
    else:
        return False
