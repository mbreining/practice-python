#!/usr/bin/python
# vim: foldlevel=0

"""
Given a vector x of n floating-point numbers (positive or negative), return the maximum
sum found in any contiguous subvector of the input. When all inputs are negative,
the maximum-sum subvector is the empty vector, which has sum zero.

Programming Pearls p77
"""


def algo1(x):
    """
    Calculate x[i:j] for each pair (i, j).
    Time complexity: O(n3)
    >>> algo1([31, -41, 59, 26, -53, 58, 97, -93, -23, 84])
    187
    >>> algo1([31, 41, 59, 26, 53, 58, 97, 93, 23, 84])
    565
    >>> algo1([31])
    31
    >>> algo1([-31])
    0
    """
    maxsofar = 0
    for i in range(len(x)):
        for j in range(i, len(x)):
            cursum = sum(x[i:j+1])
            maxsofar = max(maxsofar, cursum)
    return maxsofar


def algo2(x):
    """
    Calculate x[i:j] for each pair (i, j) without summing interval on every pass.
    Time complexity: O(n2)
    >>> algo2([31, -41, 59, 26, -53, 58, 97, -93, -23, 84])
    187
    >>> algo2([31, 41, 59, 26, 53, 58, 97, 93, 23, 84])
    565
    >>> algo2([31])
    31
    >>> algo2([-31])
    0
    """
    rollingsum = [0] * (len(x)+1)
    for i in range(len(x)):
        rollingsum[i+1] = rollingsum[i] + x[i]

    maxsofar = 0
    for i in range(len(x)):
        cursum = 0
        for j in range(i, len(x)):
            cursum = rollingsum[j+1] - rollingsum[i]
            maxsofar = max(maxsofar, cursum)

    return maxsofar


def find_largest_subvector(x, left, right):
    if left > right:
        return 0
    if left == right:
        return max(x[left], 0)

    middle = (left+right)//2
    leftmax, rightmax = 0, 0
    cursum = 0
    for elem in reversed(x[left:middle]):
        cursum += elem
        leftmax = max(leftmax, cursum)
    cursum = 0
    for elem in x[middle:right+1]:
        cursum += elem
        rightmax = max(rightmax, cursum)

    return max(leftmax+rightmax,
               find_largest_subvector(x, left, middle-1),
               find_largest_subvector(x, middle+1, right))


def algo3(x):
    """
    Time complexity: O(nlog(n))
    >>> algo3([31, -41, 59, 26, -53, 58, 97, -93, -23, 84])
    187
    >>> algo3([31, 41, 59, 26, 53, 58, 97, 93, 23, 84])
    565
    >>> algo3([31])
    31
    >>> algo3([-31])
    0
    """
    return find_largest_subvector(x, 0, len(x)-1)


def algo4(x):
    """
    Time complexity: O(n)
    >>> algo4([31, -41, 59, 26, -53, 58, 97, -93, -23, 84])
    187
    >>> algo4([31, 41, 59, 26, 53, 58, 97, 93, 23, 84])
    565
    >>> algo4([31])
    31
    >>> algo4([-31])
    0
    """
    maxsofar = 0
    maxendinghere = 0
    for i in range(len(x)):
        maxendinghere = max(maxendinghere + x[i], 0)
        maxsofar = max(maxsofar, maxendinghere)
    return maxsofar


def dp(A, j, memo):
    if memo[j] == -1:
        if j == 0:
            memo[j] = max(A[j], 0)
        else:
            memo[j] = max(dp(A, j-1, memo)+A[j], A[j])
    return memo[j]


def algo5(A):
    """
    Time complexity: O(n)
    >>> algo5([31, -41, 59, 26, -53, 58, 97, -93, -23, 84])
    187
    >>> algo5([31, 41, 59, 26, 53, 58, 97, 93, 23, 84])
    565
    >>> algo5([31])
    31
    >>> algo5([-31])
    0
    """
    memo = [-1] * len(A)
    dp(A, len(A)-1, memo)
    return max(memo)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
