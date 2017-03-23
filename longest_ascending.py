#!/usr/bin/python
# vim: foldlevel=0

"""
Given a sequence of numbers, write a function to find the length of a longest
increasing subsequence of the given sequence without the consecutive constraint.

Same problem but with the consecutive constraint:
http://blog.gainlo.co/index.php/2017/02/02/uber-interview-questions-longest-increasing-subarray/
"""


def lis(arr, j):
    """ list(j) is the max length of seq ending at i, with arr[j] being part of it.
        list(j) = 1 + max(lis(i)) if arr[i] < arr[j] else 1
    """
    if j == 0:
        return 1
    curmax = 0
    for i in range(j):
        lis_i = lis(arr, i)
        if arr[i] < arr[j] and lis_i+1 > curmax:
            curmax = lis_i+1
    return curmax
    # Alternatively:
    # return 1 + max([lis(arr, i) for i in range(j) if arr[i] < arr[j]] + [0])


def solution1(arr):
    """
    Recursive.
    >>> solution1([10, 22, 9, 33, 21, 50, 41, 60, 80])
    6
    >>> solution1([1, 3, -1])
    2
    >>> solution1([1, 3, 2, 4, 5, 1])
    4
    >>> solution1([1, 20, 5, 15, 40, 10, -5, -2])
    4
    """
    return max(lis(arr, i) for i in range(len(arr)))


def lis2(arr, j, memo):
    """
    It's very easy to make mistakes here.
    - You want to make sure that all max ascending subsequences for i in 0..j are
      being computed. So watch for the if condition on line 7 (it has to be after
      the recursive call to lis(i).
    - Likewise don't try to make the code more concise. This won't work:
      # return 1 + max([lis(X, i, memo) for i in range(j) if X[i] < X[j]] + [0])
    """
    if memo[j] == -1:
        curmax = 0
        for i in range(j):
            lis_i = lis2(arr, i, memo)
            if arr[i] < arr[j] and lis_i+1 > curmax:
                curmax = lis_i+1
        memo[j] = curmax
    return memo[j]


def solution2(arr):
    """
    Dynamic programming. O(n^2)
    >>> solution2([10, 22, 9, 33, 21, 50, 41, 60, 80])
    6
    >>> solution2([1, 3, -1])
    2
    >>> solution2([1, 3, 2, 4, 5, 1])
    4
    >>> solution2([1, 20, 5, 15, 40, 10, -5, -2])
    4
    """
    memo = [-1] * len(arr)
    memo[0] = 1
    lis2(arr, len(arr)-1, memo)
    return max(memo)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
