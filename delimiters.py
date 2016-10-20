#!/usr/bin/python
# vim: foldlevel=0

"""
Write a function that determines if all of the delimiters in an expression
are matched and closed.

http://blog.gainlo.co/index.php/2016/09/30/uber-interview-question-delimiter-matching/
"""


def solution(A):
    """
    >>> solution('{ac[bb]}')
    True
    >>> solution('[dklf(df(kl))d]{}')
    True
    >>> solution('{[[[]]]}')
    True
    >>> solution('{3234[fd')
    False
    >>> solution('{df][d}')
    False
    >>> solution('([)]')
    False
    """
    stack = []
    for i in range(len(A)):
        c = A[i]
        if c not in '()[]{}':
            continue
        if c in '({[':  # open delimiter
            stack.append(c)
        else:  # close delimiter
            last = stack[-1]
            if c == ')' and last != '(' or c == ']' and last != '[' or c == '}' and last != '{':
                return False
            stack.pop()
    return len(stack) == 0


if __name__ == "__main__":
    import doctest
    doctest.testmod()
