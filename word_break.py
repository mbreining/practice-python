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
"""
from collections import defaultdict, deque

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


dictionary2 = ['listen', 'silent', 'niels', 'hello', 'hole', 'on', 'apple', 'pale']


def s(word):
    return ''.join(sorted(word))


def unscramble(S, i, s_dict, res):
    if i == len(S):
        return True
    for j in range(i+1, len(S)):
        k = s(S[i:j+1])
        if not s_dict.get(k):
            continue
        res.append(s_dict[k][-1])  # pick the last word (or first or any word in the list)
        if unscramble(S, j+1, s_dict, res):
            return True
        res.pop()
    return False


def followup2(S):
    """
    >>> S = 'nslietloehl'
    >>> followup2(S)
    ['silent', 'hello']
    """
    s_dict = defaultdict(list)
    for w in dictionary2:
        s_dict[s(w)].append(w)

    res = []
    unscramble(S, 0, s_dict, res)
    return res


if __name__ == '__main__':
    import doctest
    doctest.testmod()
