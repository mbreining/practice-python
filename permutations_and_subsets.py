#!/usr/bin/python
# vim: foldlevel=0

"""
Find all permutations (no repeats) and subsets of a string.
"""


def find_permutations(chars, cur):
    ''' n! permutations '''
    if len(cur) == len(chars):
        print "".join(cur)
        return
    for c in set(chars)-set(cur):
        cur.append(c)
        find_permutations(chars, cur)
        cur.pop()


def find_subsets(chars, subset, j):
    ''' 2^n subsets '''
    if j < 0:
        print "".join([chars[i] for i, v in enumerate(subset) if v])
        return
    for value in (True, False):
        subset[j] = value
        find_subsets(chars, subset, j-1)
        subset[j] = None


text = "hat"
print "Permutations"
find_permutations(list(text), [])
print "\nSubsets"
find_subsets(list(text), [None]*len(text), len(text)-1)
