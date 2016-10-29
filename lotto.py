#!/usr/bin/python
# vim: foldlevel=0

"""
Your favorite uncle, Morty, is crazy about the lottery and even crazier about
how he picks his "lucky" numbers. And even though his "never fail" strategy has
yet to succeed, Uncle Morty doesn't let that get him down. Every week he
searches through the Sunday newspaper to find a string of digits that might be
potential lottery picks. But this week the newspaper has moved to a new
electronic format, and instead of a comfortable pile of papers, Uncle Morty
receives a text file with the stories.

Help your Uncle find his lotto picks. Given a large series of number strings,
return each that might be suitable for a lottery ticket pick. Note that a valid
lottery ticket must have 7 unique numbers between 1 and 59, digits must be used
in order, and every digit must be used.

For example, given the following strings:

["1", "42", "100848", "4938532894754", "1234567", "472844278465445"]

Your function should return:

4938532894754 -> 49 38 53 28 9 47 54
1234567 -> 1 2 3 4 5 6 7
"""


def get_candidates(S, i, num):
    ''' Given an index i in string S and an incomplete set of lotto numbers in
        num, return the next valid candidates (up to two max).
    '''
    def _check_valid(n):
        if 1 <= int(n) <= 59 and n[0] != '0' and n not in num:
            return True
        return False
    candidates = [S[i:i+1]]
    if i < len(S)-1:
        candidates.append(S[i:i+2])
    return [c for c in candidates if _check_valid(c)]


def pick_number(S, i, num):
    ''' Using backtracking, check if a string S can be used as a lotto number.
    '''
    # Do we have a valid lotto number?
    if i >= len(S):
        if len(num) == 7:
            return True
        else:
            return False

    # We don't have a valid lotto number yet.
    # Cycle through the next possible candidates.
    for candidate in get_candidates(S, i, num):
        num.append(candidate)
        if pick_number(S, i+len(candidate), num):
            return True  # we have a winner!
        num.pop()  # we don't have a winner so backtrack!

    return False


def lotto(numbers):
    """
    >>> lotto(['1', '42', '100848', '4938532894754', '1234567', '472844278465445', '120349876'])
    [('4938532894754', '49 38 53 28 9 47 54'), ('1234567', '1 2 3 4 5 6 7'), ('120349876', '1 20 3 49 8 7 6')]
    """
    res = []
    for S in numbers:
        if len(S) < 7 or len(S) > 14:
            continue
        num = []
        pick_number(S, 0, num)
        if num:
            res.append((S, ' '.join(num)))
    return res


if __name__ == "__main__":
    import doctest
    doctest.testmod()
