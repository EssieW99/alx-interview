#!/usr/bin/python3
""" Minimum Operations Function"""


def minOperations(n):
    """
    calculates the fewest number of operations needed to result in
    exactly n H characters in the file
    """

    if n <= 1:
        return 0

    factor = 2
    operations = 0

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    return operations
