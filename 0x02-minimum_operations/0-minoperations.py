#!/usr/bin/python3
"""
Module for calculating the minimum number of operations to achieve n H characters.
"""


def minOperations(n):
    """Calculates the minimum number of operations to achieve n H characters."""
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    # Prime factorization approach to find the minimum number of operations
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n /= divisor
        divisor += 1

    return operations
