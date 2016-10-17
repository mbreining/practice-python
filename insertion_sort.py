#!/usr/bin/python
# vim: foldlevel=0

"""
Insertion sort
"""
from random_array import randlist

arr = randlist(50, 100)
print "The input array: {0}".format(arr)


def sort(arr):
    for i in range(1, len(arr)):
        cur = arr[i]
        j = i-1
        while j >=0 and arr[j] > cur:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = cur


sort(arr)
print "The sorted array: {0}".format(arr)
