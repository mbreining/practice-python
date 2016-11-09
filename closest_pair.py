#!/usr/bin/python
# vim: foldlevel=0

"""
Given a sorted array and a number x, find a pair in array whose sum is closest to x.

http://geeksquiz.com/given-sorted-array-number-x-find-pair-array-whose-sum-closest-x/
"""
import sys


def solution(arr, x):
    """
    >>> solution([10, 22, 28, 29, 30, 40], 54)
    (22, 30)
    >>> solution([1, 3, 4, 7, 10], 15)
    (4, 10)
    """
    diff = sys.maxint

    i, j = 0, len(arr)-1
    while i < j:
        if arr[i] + arr[j] == x:
            closest_sum_pair = (arr[i], arr[j])
            break
        elif abs(arr[i] + arr[j] - x) < diff:
            diff = abs(arr[i] + arr[j] - x)
            closest_sum_pair = (arr[i], arr[j])
        if arr[i] + arr[j] < x:
            i += 1
        else:
            j -= 1

    return closest_sum_pair


if __name__ == "__main__":
    import doctest
    doctest.testmod()
