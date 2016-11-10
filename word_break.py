#!/usr/bin/python
# vim: foldlevel=0

"""
Given an input string and a dictionary of words, find out if the input string
can be segmented into a space-separated sequence of dictionary words.

Follow-up: Return all possible space-separated sequence of words.

Follow-up 2: You are given a scrambled input sentence. Each word is scrambled
independently, and the results are concatenated. So:

'hello to the world' might become: 'elhloothtedrowl'

You have a dictionary with all words in it. Unscramble the sentence.

Follow-up 3: https://repl.it/ETxc/1

http://thenoisychannel.com/2011/08/08/retiring-a-great-interview-problem
"""
from collections import defaultdict, deque

dictionary = ['hell', 'hello', 'on', 'obo', 'nobo', 'apple']


def break_word(S, j, memo):
    if not memo[j]:
        if j == 0:
            memo[j] = True
        else:
            for i in range(j):
                word = S[i:j]  # check suffix
                if word in dictionary:
                    if break_word(S, i, memo):  # check prefix recursively
                        memo[j] = True
                        break
            else:  # nobreak
                memo[j] = False
    return memo[j]


def solution(S):
    """
    Time complexity of recursive solution: O(2^n) - power set
    Time complexity of dp solution: O(n^2)
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


dictionary2 = ['listen', 'silent', 'niels', 'hello', 'hole', 'on', 'apple', 'pale']


def s(word):
    return ''.join(sorted(word))


def break_word3(S, j, dictionary, cur_phrase):
    if j == 0:
        print list(cur_phrase)
    for i in range(j):
        word = S[i:j]
        word = s(word)
        if dictionary.get(word):
            cur_phrase.appendleft(dictionary[word][-1])  # arbitrarily pick last
            break_word3(S, i, dictionary, cur_phrase)
            cur_phrase.popleft()


def followup2(S):
    """
    >>> S = 'nslietloehl'
    >>> followup2(S)
    ['silent', 'hello']
    """
    s_dict = defaultdict(list)
    for w in dictionary2:
        s_dict[s(w)].append(w)
    break_word3(S, len(S), s_dict, deque())


if __name__ == '__main__':
    import doctest
    doctest.testmod()
