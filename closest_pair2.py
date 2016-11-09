#!/usr/bin/python
# vim: foldlevel=0

"""
Given two sorted arrays and a number x, find the pair whose sum is closest to x and the
pair has an element from each array.

http://www.geeksforgeeks.org/given-two-sorted-arrays-number-x-find-pair-whose-sum-closest-x/
"""
import sys


def solution(arr1, arr2, x):
    """
    >>> solution([1, 4, 5, 7], [10, 20, 30, 40], 32)
    (1, 30)
    >>> solution([1, 4, 5, 7], [10, 20, 30, 40], 50)
    (7, 40)
    >>> initial_solution([1, 4, 5, 7], [10, 20, 30, 40, 60], 50)
    (7, 40)
    """
    closest_sum = sys.maxint

    i, j = 0, len(arr2)-1
    while i <= len(arr1)-1 and j >= 0:
        if arr1[i] + arr2[j] == x:
            closest_sum_pair = (arr1[i], arr2[j])
            break
        if abs(arr1[i] + arr2[j] - x) < abs(closest_sum - x):
            closest_sum = abs(arr1[i] + arr2[j])
            closest_sum_pair = (arr1[i], arr2[j])
        if arr1[i] + arr2[j] < x:
            i += 1
        else:
            j -= 1

    return closest_sum_pair


def initial_solution(arr1, arr2, x):
    """
    Not the most concise.
    >>> initial_solution([1, 4, 5, 7], [10, 20, 30, 40], 32)
    (1, 30)
    >>> initial_solution([1, 4, 5, 7], [10, 20, 30, 40], 50)
    (7, 40)
    >>> initial_solution([1, 4, 5, 7], [10, 20, 30, 40, 60], 50)
    (7, 40)
    """
    closest_sum = arr1[0] + arr2[0]
    closest_sum_pair = (arr1[0], arr2[0])

    i, j = 0, 0
    while i < len(arr1)-1 or j < len(arr2)-1:
        # Increment i or j in order to minimize (cur_sum - x)
        if i < len(arr1)-1 and j < len(arr2)-1:
            next_sum1 = arr1[i+1] + arr2[j]
            next_sum2 = arr1[i] + arr2[j+1]
            if abs(next_sum1 - x) <= abs(next_sum2 - x):
                i += 1
            else:
                j += 1
        elif i < len(arr1)-1:
            i += 1
        else:
            j += 1

        # Check if we have a new closest pair
        cur_sum = arr1[i] + arr2[j]
        if abs(cur_sum - x) < abs(closest_sum - x):
            closest_sum = cur_sum
            closest_sum_pair = (arr1[i], arr2[j])
            if closest_sum == x:
                break

    return closest_sum_pair


if __name__ == "__main__":
    import doctest
    doctest.testmod()
