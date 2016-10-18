#!/usr/bin/python
# vim: foldlevel=0

"""
Given an array of integers, find the nearest smaller number for every element such that
the smaller element is on left side.

http://www.geeksforgeeks.org/find-the-nearest-smaller-numbers-on-left-side-in-an-array/
"""


def solution(arr):
    """
    >>> solution([1, 6, 4, 10, 2, 5])
    [None, 1, 1, 4, 1, 2]
    >>> solution([1, 3, 0, 2, 5])
    [None, 1, None, 0, 2]
    """
    nearest_smaller = [None]
    stack = [arr[0]]
    for i in range(1, len(arr)):
        while stack and stack[-1] > arr[i]:
            stack.pop()
        if stack:
            nearest_smaller.append(stack[-1])
        else:
            nearest_smaller.append(None)
        stack.append(arr[i])
    return nearest_smaller


if __name__ == "__main__":
    import doctest
    doctest.testmod()
