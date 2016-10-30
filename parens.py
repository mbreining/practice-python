#!/usr/bin/python
# vim: foldlevel=0

"""
Implement an algorithm to print all valid (i.e. properly opened and closed)
combinations of n-pairs of parentheses.
"""


def parens(P, i, open):
    if i == len(P):
        if open == 0:
            print ''.join(P)
        return
    candidates = []
    if open < len(P)//2:
        candidates.append('(')
    if open > 0:
        candidates.append(')')
    for v in candidates:
        P[i] = v
        parens(P, i+1, open+1 if v == '(' else open-1)
        P[i] = None

n = 3
P = [None] * (2*n)
parens(P, 0, 0)
