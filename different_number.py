#!/usr/bin/python
# vim: foldlevel=0

"""
Given an array arr of n unique non-negative integers, how can you most efficiently find
a non-negative integer that is not in the array?

Your solution should return such an integer or null if arr contains all possible
integers. Analyze the runtime and space complexity of your solution.

https://www.pramp.com/question/aK6V5GVZ9MSPqvG1vwQp
"""
from collections import defaultdict
import sys


def solution1(arr):
    """
    >>> solution1([7, 40, 2, 13, 25, 29, 49, 26, 5, 31])
    0
    >>> solution1([0, 1, 2, 13, 25, 29, 49, 26, 5, 31])
    3
    """
    arr_len = len(arr)
    if arr_len == sys.maxint:
        return -1

    arr_map = defaultdict(int)
    for x in arr:
        arr_map[x] = 1

    for i in range(arr_len+1):
        if not arr_map[i]:
            return i


def solution2(arr):
    """
    >>> solution2([7, 40, 2, 13, 25, 29, 49, 26, 5, 31])
    0
    >>> solution2([0, 1, 2, 6, 8, 29, 49, 26, 5, 31])
    3
    """
    arr_len = len(arr)
    if arr_len == sys.maxint:
        return -1

    arr2 = list()
    for i in range(arr_len+1):
        arr2.append(0)

    for x in arr:
        arr2[x % (arr_len+1)] = 1

    for i in range(arr_len+1):
        if not arr2[i]:
            return i


if __name__ == "__main__":
    import doctest
    doctest.testmod()
