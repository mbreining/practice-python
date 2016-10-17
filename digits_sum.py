#!/usr/bin/python
# vim: foldlevel=0

"""
Given two integers 'n' and 'sum', find count of all n digit numbers with sum of digits
as 'sum'. Leading 0's are not counted as digits. Return -1 if not possible.

http://www.geeksforgeeks.org/count-of-n-digit-numbers-whose-sum-of-digits-equals-to-given-sum/
"""


def digits_sum(n, target_sum, start):
    if target_sum == 0:
        return 1
    if n == 0:
        return 0
    count = 0
    for i in range(start, 10):
        if i <= target_sum:
            count += digits_sum(n-1, target_sum-i, 0)
    return count


def recursive(n, target_sum):
    """
    >>> recursive(2, 2)
    2
    >>> recursive(2, 5)
    5
    >>> recursive(3, 6)
    21
    """
    print digits_sum(n, target_sum, 1)


def digits_sum_memo(n, target_sum, start, memo):
    if target_sum == 0:
        return 1
    if n == 0:
        return 0

    if memo.get((n, target_sum)):
        return memo[(n, target_sum)]

    count = 0
    for i in range(start, 10):
        if i <= target_sum:
            count += digits_sum_memo(n-1, target_sum-i, 0, memo)

    memo[(n, target_sum)] = count
    return count


def dp(n, target_sum):
    """
    >>> dp(2, 2)
    2
    >>> dp(2, 5)
    5
    >>> dp(3, 6)
    21
    """
    memo = dict()
    print digits_sum_memo(n, target_sum, 1, memo)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
