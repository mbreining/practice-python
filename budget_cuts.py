#!/usr/bin/python
# vim: foldlevel=0

"""
The awards committee had planned to give n research grants this year, out of a its total
yearly budget. However, the budget was reduced to b dollars. The committee members has
decided to affect the minimal number of highest grants, by applying a maximum cap c on
all grants: every grant that was planned to be higher than c will now be c dollars.
Help the committee to choose the right value of c that would make the total sum of
grants equal to the new budget.

Given an array of grants g and a new budget b, explain and code an efficient method to
find the cap c. Analyze the time and space complexity of your solution.

Example:

grants 10 30 50 70 120 150
total requested 430
budget 240

cumsum 10 40 90 160 280 430
final grants 10 30 50 50 50 50
so c = 50

https://www.pramp.com/question/r1Kw0vwG6OhK9AEGAyWV
"""


def solution(g, b):
    """
    >>> solution([10, 30, 50, 70, 120, 150], 240)
    50
    >>> solution([10, 30, 50, 70, 120, 150], 1000)
    0
    """
    g.sort()

    cumsum = [g[0]]
    for i in range(1, len(g)):
        cumsum.append(cumsum[i-1] + g[i])

    if cumsum[len(g)-1] <= b:
        return 0

    def capped_sum(i):
        return cumsum[i] + (len(g)-i)*g[i]

    lo, hi = 0, len(g)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if capped_sum(mid-1) <= b <= capped_sum(mid):
            break
        if capped_sum(mid) <= b:
            lo = mid+1
        else:
            hi = mid-1

    return (b-cumsum[mid-1])/(len(g)-mid)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
