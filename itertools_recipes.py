#!/usr/bin/python

"""
Itertools recipes

https://docs.python.org/2/library/itertools.html#recipes
"""
from itertools import chain, combinations, count, imap, islice
import operator


def take(n, iterable):
    """ Return the first n elements of the iterable as a list.
    >>> take(4, [1, 2, 3, 4, 5, 6, 7])
    [1, 2, 3, 4]
    """
    return list(islice(iterable, n))


def tabulate(function, start=0):
    """ Return function(0), function(1), ...
    """
    return imap(function, count(start))


def flatten(list_of_lists):
    """ Flatten one level of nesting.
    >>> flatten([[1, 3, 4], [5, 6, 7, 8], [9, 0]])
    [1, 3, 4, 5, 6, 7, 8, 9, 0]
    """
    # return list(chain(*list_of_lists))
    # or:
    return list(chain.from_iterable(list_of_lists))


def dotproduct(vec1, vec2):
    """ Sum of the dot product.
    >>> dotproduct([1, 2, 3], [4, 5, 6])
    32
    """
    return sum(imap(operator.mul, vec1, vec2))


def powerset(iterable):
    """
    >>> powerset([1, 2, 3])
    [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
    """
    return list(chain.from_iterable([combinations(iterable, i) for i in range(len(iterable)+1)]))


"""
# Warmup

You are given two iterators. Exhaust both iterators in any order and return the
unique elements as another iterator.

e.g.
it1 = iter([9,0,1,3,3])
it2 = iter([1,3,5,6,0,2])
your_it = ([9,0,1,3,5,6,2])

# Followup

Your solution uses O(n+m) space in the worst case. Can you do better if the
lists are always sorted?

e.g.
it1 = iter([0,1,3,5])
it2 = iter([1,3,5,6])
your_it = ([0,1,3,5,6])

# Difficulties

* Know about iterators (the only way to know they're empty is if they throw an exception)

# Solutions

* Warmup - use a set() to store seen numbers, exhaust both iterators in order
* Followup - grab an element, exhaust both iterators of this element (use caching)
* Followup - implement via a peeking iterator https://leetcode.com/problems/peeking-iterator/
"""


def warmup(it1, it2):
    """
    >>> list(warmup(iter([4, 1, 1, 3, 4]), iter([0, 0, 1, 4, 3, 5])))
    [4, 1, 3, 0, 5]
    """
    seen = set()
    for element in chain(it1, it2):
        if element not in seen:
            seen.add(element)
            yield element
    return


def exhaust(it, val):
    res = None
    try:
        while True:
            res = next(it)
            if res != val:
                break
    except StopIteration:
        pass
    return res


def followup(it1, it2):
    """
    >>> list(followup(iter([1, 1, 2, 3, 4]), iter([0, 0, 1, 3, 3, 5])))
    [0, 1, 2, 3, 4, 5]
    """
    next1, next2 = next(it1), next(it2)
    while next1 is not None and next2 is not None:
        if next1 <= next2:
            res = next1
            next1 = exhaust(it1, res)
            if next2 == res:
                next2 = exhaust(it2, res)
        else:
            res = next2
            next2 = exhaust(it2, res)
        yield res
    while next1 is not None:
        res = next1
        next1 = exhaust(it1, res)
        yield res
    while next2 is not None:
        res = next2
        next2 = exhaust(it2, res)
        yield res


def followup2(it1, it2):
    pit1 = PeekingIterator(it1)
    pit2 = PeekingIterator(it2)
    prev = None
    while pit1.peek() and pit2.peek():
        if pit1.peek() <= pit2.peek():
            next = pit1.next()
        else:
            next = pit2.next()
        if not prev or next != prev:
            yield next
    while pit1.peek():
        next = pit1.next()
        if not prev or next != prev:
            yield next
    while pit2.has_next():
        next = pit2.next()
        if not prev or next != prev:
            yield next


class PeekingIterator(object):
    def __init__(self, iterator):
        self.iterator = iterator
        self._next = None
        self._get_next()

    def _get_next(self, prev=None):
        try:
            self._next = next(self.iterator)
        except StopIteration:
            self._next = None

    def next(self):
        res = None
        if self._next:
            res = self._next
            self._get_next(res)
        return res

    def peek(self):
        return self._next


if __name__ == "__main__":
    import doctest
    doctest.testmod()
