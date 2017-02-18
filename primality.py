#!/usr/bin/python
# vim: foldlevel=0

"""
Check if an integer is a prime number.
"""

from math import sqrt


def is_prime(n):
    """
    >>> is_prime(2)
    False
    >>> is_prime(4)
    False
    >>> is_prime(6)
    False
    >>> is_prime(11)
    True
    >>> is_prime(27)
    False
    >>> is_prime(59)
    True
    """
    if n < 2 or (n % 2) == 0:
        return False
    for i in range(2, int(sqrt(n))):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
