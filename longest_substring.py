#!/usr/bin/python
# vim: foldlevel=0

"""
Find the longest substring with k unique characters.

Example: If the string is "aabbccdd", if K is 1, the longest substring can be "aa".
If K is 2, the longest substring can be "aabb".
If K is 3, the longest substring can be "aabbcc".

http://blog.gainlo.co/index.php/2016/04/12/find-the-longest-substring-with-k-unique-characters/
http://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/
"""


def solution(text, k):
    """
    Time complexity: O(n)
    Auxiliary space complexity: O(1)

    >>> solution("aabbccdd", 1)
    'aa'
    >>> solution("aabbccdd", 2)
    'aabb'
    >>> solution("aabbccdd", 3)
    'aabbcc'
    >>> solution("abacbebebe", 3)
    'cbebebe'
    >>> solution("abacbbeb", 3)
    'abacbb'
    >>> solution("ababebebe", 4)
    ''
    """
    def _count_uniques(uniques):
        return len([e for e in uniques if e != 0])

    res = ''
    lo = 0
    # We need to keep track of both the chars we've seen and their count
    chars = [0] * 256

    for hi in range(len(text)):
        # Add new character to window
        chars[ord(text[hi])] += 1

        # Re-adjust window if needed
        while _count_uniques(chars) > k:
            chars[ord(text[lo])] -= 1
            lo += 1

        # Check if we have a new longest substring
        if _count_uniques(chars) == k and (hi-lo+1) > len(res):
            res = text[lo:hi+1]

    return res


if __name__ == "__main__":
    import doctest
    doctest.testmod()
