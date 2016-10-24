#!/usr/bin/python
# vim: foldlevel=0

"""
How to check if a string contains an anagram of another string?

Example: The string "coding interview questions" contains an anagram of the string
"weivretni".

http://blog.gainlo.co/index.php/2016/04/08/if-a-string-contains-an-anagram-of-another-string/
http://www.geeksforgeeks.org/anagram-substring-search-search-permutations/
"""


def solution(a, b):
    """
    >>> solution("coding interview questions", "weivretni")
    True
    >>> solution("coding interviw questions", "weivretni")
    False
    >>> solution("coding interview questions", "abcde")
    False
    """
    tracker = [0] * 256
    for i in range(len(b)):
        tracker[ord(b[i])] += 1
    lo = 0
    for hi in range(len(a)):
        tracker[ord(a[hi])] -= 1
        while hi-lo+1 > len(b):
            tracker[ord(a[lo])] += 1
            lo += 1
        if hi-lo+1 == len(b) and all([c == 0 for c in tracker]):
            return True
    return False


def solution1(a, b):
    """
    >>> solution1("coding interview questions", "weivretni")
    True
    >>> solution1("coding interviw questions", "weivretni")
    False
    >>> solution1("coding interview questions", "abcde")
    False
    """
    target_hash, rolling_hash = 0, 0
    for i in range(len(b)):
        target_hash += ord(b[i]) // 101
        rolling_hash += ord(a[i]) // 101

    i = 0
    for j in range(len(b), len(a)):
        if rolling_hash == target_hash:
            return True
        rolling_hash += ord(a[j]) // 101
        rolling_hash -= ord(a[i]) // 101
        i += 1
    return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()
