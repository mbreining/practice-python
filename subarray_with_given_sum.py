#!/usr/bin/python
# vim: foldlevel=0

"""
Given an array of non-negative numbers, find continuous subarray with sum to S.

Follow-up:
Given an array of numbers, find subarray with sum to S.

http://blog.gainlo.co/index.php/2016/06/01/subarray-with-given-sum/
"""

def sol(A, S):
    """
    >>> sol([7, 0, 8, 1, 9, 2, 3, 4, 5], 12)
    [1, 9, 2]
    >>> sol([7, 0, 8, 1, 9, 2, 3, 4, 5], 7)
    [7]
    >>> sol([7, 0, 8, 1, 9, 2, 3, 4, 5], 39)
    [7, 0, 8, 1, 9, 2, 3, 4, 5]
    >>> sol([7, 0, 8, 1, 9, 2, 3, 4, 5], 5)
    [2, 3]
    >>> sol([7, 0, 8, 1, 9, 2, 3, 4, 5], 99)
    -1
    """
    i, j = 0, 0
    cursum = 0
    while j < len(A):
        cursum += A[j]
        if cursum == S:
            return A[i:j+1]
        while cursum > S:
            cursum -= A[i]
            i += 1
        j += 1
    return -1


def solution(arr, s):
    """
    Time complexity: O(n)
    >>> solution([7, 0, 8, 1, 9, 2, 3, 4, 5], 12)
    [1, 9, 2]
    >>> solution([7, 0, 8, 1, 9, 2, 3, 4, 5], 7)
    [7]
    >>> solution([7, 0, 8, 1, 9, 2, 3, 4, 5], 39)
    [7, 0, 8, 1, 9, 2, 3, 4, 5]
    >>> solution([7, 0, 8, 1, 9, 2, 3, 4, 5], 5)
    [2, 3]
    >>> solution([7, 0, 8, 1, 9, 2, 3, 4, 5], 99)
    -1
    """
    lo, hi = 0, 0
    cursum = 0
    for hi in range(len(arr)):
        cursum += arr[hi]
        while cursum > s:
            cursum -= arr[lo]
            lo += 1
        if cursum == s:
            return arr[lo:hi+1]
    return -1


def rec(A, j, S, res):
    if S == 0:
        return res
    if j == 0:
        return []

    res[j-1] = True  # use element at position j-1
    if rec(A, j-1, S-A[j-1], res):
        return res

    res[j-1] = False  # do not use element at position j-1
    return rec(A, j-1, S, res)


def followup(arr, s):
    """
    >>> followup([7, 0, 8, 1, 9, 2, 3, 4, 5], 12)
    [3, 4, 5]
    >>> followup([7, 2, -1, 4, -3], 6)
    [7, 2, -3]
    >>> followup([7, 2, -1, 4, -3], 99)
    []
    """
    res = [False]*len(arr)
    return [arr[i] for i, v in enumerate(rec(arr, len(arr), s, res)) if v]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
