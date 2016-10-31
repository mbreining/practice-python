#!/usr/bin/python
# vim: foldlevel=0

"""
You are given transactions, and a way to check if any 2 transactions are done
by the same customer. If more than 50% of the transactions are done by the same
person then it is considered fraud.

Majority algorithm: https://www.youtube.com/watch?v=zOyOwDEF1Rc
"""


def is_same_transaction(t1, t2):
    return t1 == t2


def get_majority(transactions):
    candidate, count = None, 0
    for i in range(len(transactions)):
        if count == 0:
            candidate, count = transactions[i], 1
        else:
            if is_same_transaction(transactions[i], candidate):
                count += 1
            else:
                count -= 1
    return candidate


def detect_fraud(transactions):
    """
    >>> detect_fraud('aabacaad')
    True
    >>> detect_fraud('aabacc')
    False
    """
    # Get majority candidate.
    candidate = get_majority(transactions)

    # Check whether it is actually the majority.
    count = 0
    for i in range(len(transactions)):
        if transactions[i] == candidate:
            count += 1
    if count > len(transactions)//2:
        return True
    return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()
