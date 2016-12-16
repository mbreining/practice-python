#!/usr/bin/python
# vim: foldlevel=0

"""
Merge sort.
"""

import random

arr = []
for i in range(25):
    arr.append(random.randint(0, 50))
print "The array: {0}".format(arr)


def merge(arr, left, right):
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def mergesort(a):
    if len(a) == 1:
        return a
    mid = len(a)//2
    left = a[:mid]
    right = a[mid:]
    mergesort(left)
    mergesort(right)
    merge(a, left, right)


mergesort(arr)
print arr
