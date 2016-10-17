#!/usr/bin/python
# vim: foldlevel=0

"""
Given an array arr of length n where each element is at most k places away from
its sorted position, plan and code an efficient algorithm to sort arr.
Analyze the runtime and space complexity of your solution.

Example: n=10, k=2. The element belonging to index 6 in the sorted array,
may be at indices 4, 5, 6, 7 or 8 on the given array.

https://www.pramp.com/question/XdMZJgZoAnFXqwjJwnBZ
"""


def solution(arr, k):
    h = minheap()
    for i in range(k+1):
        h.insert(arr[i])
    i = 0
    for j in range(k+1, n):
        arr[i] = h.pop()
        h.insert(arr[j])
    while h:
        arr[i] = h.pop()
