#!/usr/bin/python
# vim: foldlevel=0

"""
Given a 2D matrix M, filled with either 0s or 1s, count the number of islands
of 1s in M. An island is a group of adjacent values that are all 1s. Every cell
 in M can be adjacent to the 4 cells that are next to it on the same row or column.

https://www.pramp.com/question/yZm60L6d5juM7K38KYZ6
"""


def nullify(M, i, j):
    if i < 0 or i >= len(M):
        return
    if j < 0 or j >= len(M[0]):
        return
    if M[i][j] == 0:
        return
    M[i][j] = 0
    nullify(M, i, j-1)
    nullify(M, i-1, j)
    nullify(M, i, j+1)
    nullify(M, i+1, j)


def island_count(M):
    count = 0
    for j in range(len(M[0])):
        for i in range(len(M)):
            if M[i][j] == 0:
                continue
            count += 1
            nullify(M, i, j)
    return count
