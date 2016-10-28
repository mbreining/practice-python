#!/usr/bin/python
# vim: foldlevel=0

"""
Given an input string and a dictionary of words, find out if the input string
can be segmented into a space-separated sequence of dictionary words.

Follow-up: Return all possible space-separated sequence of words.
"""
from collections import deque

dictionary = ['hell', 'hello', 'on', 'obo', 'nobo', 'apple']


def break_word(S, j, memo):
    if not memo[j]:
        if j == 0:
            memo[j] = True
        else:
            for i in range(j):
                word = S[i:j]
                if word in dictionary:
                    if break_word(S, i, memo):
                        memo[j] = True
                        break
            else:  # nobreak
                memo[j] = False
    return memo[j]


def solution(S):
    """
    >>> S = 'hellonobo'
    >>> solution(S)
    True
    >>> S = 'hellonoapple'
    >>> solution(S)
    False
    """
    memo = [None] * (len(S)+1)
    print break_word(S, len(S), memo)


def break_word2(S, j, cur_phrase):
    if j == 0:
        print list(cur_phrase)
    for i in range(j):
        word = S[i:j]
        if word in dictionary:
            cur_phrase.appendleft(word)
            break_word2(S, i, cur_phrase)
            cur_phrase.popleft()


def followup(S):
    """
    >>> S = 'hellonobo'
    >>> followup(S)
    ['hello', 'nobo']
    ['hell', 'on', 'obo']
    >>> S = 'hellonoapple'
    >>> followup(S)
    """
    break_word2(S, len(S), deque())


if __name__ == '__main__':
    import doctest
    doctest.testmod()
