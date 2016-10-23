#!/usr/bin/python
# vim: foldlevel=0

"""
Check if a string is a palindrome, e.g. radar.
"""
from collections import deque


def palindrome(text, lo, hi):
    if lo >= hi:
        return True
    if text[lo] == text[hi]:
        return palindrome(text, lo+1, hi-1)
    return False

print palindrome("radar", 0, len("radar")-1)
print palindrome("raddar", 0, len("raddar")-1)
print palindrome("radfar", 0, len("radfar")-1)


def palindrome2(text):
    d = deque()
    for c in text:
        d.appendleft(c)
    while len(d) > 1:
        if d.pop() != d.popleft():
            return False
    return True

print palindrome2("radar")
print palindrome2("raddar")
print palindrome2("radfar")
