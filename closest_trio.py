#!/usr/bin/python
# vim: foldlevel=0

"""
Given three sorted arrays A, B and C, find three elements i, j and k from A, B and C
respectively such that max(abs(A[i]-B[j]), abs(B[j]-C[k]), abs(C[k]-A[i]) is
minimized.

http://www.geeksforgeeks.org/find-three-closest-elements-from-given-three-sorted-arrays/
"""
import sys


def solution(a, b, c):
    """
    >>> solution([1, 4, 10], [2, 15, 20], [10, 12])
    (10, 15, 10)
    >>> solution([20, 24, 100], [2, 19, 22, 79, 800], [10, 12, 23, 24, 119])
    (24, 22, 23)
    """
    closest_trio = None
    diff = sys.maxint

    i, j, k = 0, 0, 0
    while i < len(a) and j < len(b) and k < len(c):
        # Do we have a new closest trio?
        curdiff = max(abs(a[i]-b[j]), abs(b[j]-c[k]), abs(c[k]-a[i]))
        if curdiff < diff:
            diff = curdiff
            closest_trio = (a[i], b[j], c[k])

        # Increment i, j or k
        curmin = min([a[i], b[j], c[k]])
        if a[i] == curmin:
            i += 1
        elif b[j] == curmin:
            j += 1
        elif c[k] == curmin:
            k += 1

    return closest_trio


if __name__ == "__main__":
    import doctest
    doctest.testmod()
