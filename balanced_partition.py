#!/usr/bin/python
# vim: foldlevel=0

"""
You have a set of n integers each in the range 0...K. Partition these integers
into two subsets such that you minimize |S1 - S2|, where S1 and S2 denote the
sums of the elements in each of the two subsets.

https://people.cs.clemson.edu/~bcdean/dp_practice/
http://www.geeksforgeeks.org/dynamic-programming-set-18-partition-problem/
"""


def greedy(A):
    """
    This greedy solution is incorrect as it does not always return the
    optimal solution, e.g.
    # greedy([3, 3, 2, 2, 2])
    # expected: ([3, 3], [2, 2, 2])
    # got: ([3, 2, 2], [3, 2])
    """
    A = sorted(A, reverse=True)
    a = [A[i] for i in range(len(A)) if i % 2 == 0]
    b = [A[i] for i in range(len(A)) if i % 2 == 1]
    return a, b


def dp(A, j, S, memo):
    if S == 0:
        return True
    if j == 0:
        return False
    if memo[j][S] is None:
        if A[j] > S:
            memo[j][S] = dp(A, j-1, S, memo)
        memo[j][S] = dp(A, j-1, S, memo) or dp(A, j-1, S-A[j], memo)
    return memo[j][S]


def solution(A):
    """
    >>> solution([3, 3, 2, 2, 2])
    True
    >>> solution([11, 1, 5, 5])
    True
    >>> solution([5, 1, 5, 3])
    False
    """
    #([3, 3], [2, 2, 2])
    #([11], [5, 5, 1])
    #([5, 1], [5, 3])
    S = sum(A)//2
    memo = [[None for j in range(S+1)] for i in range(len(A))]
    return dp(A, len(A)-1, S, memo)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
