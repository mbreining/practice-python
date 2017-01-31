#!/usr/bin/python
# vim: foldlevel=0

"""
Find the kth to last element of a singly linked list.
"""
from linked_list import randlinkedlist


def iterative(head, k):
    cur, runner = head, head
    for i in range(k):
        runner = runner.next
    while runner:
        runner = runner.next
        cur = cur.next
    return cur.value


def visit(node, k, value):
    if not node:
        return 0
    count = 1 + visit(node.next, k, value)
    if count == k:
        value.append(node.value)
    return count


def recursive(head, k):
    value = list()  # passing a list rather than an int since list are mutable, not ints
    visit(head, k, value)
    return value[0]


if __name__ == "__main__":
    def _print(head):
        cur = head
        while cur:
            print cur.value
            cur = cur.next

    ll = randlinkedlist()
    print "Original linked list: "
    _print(ll.head)
    print "Kth to last element (iterative): %d" % iterative(ll.head, 6)
    print "Kth to last element (recursive): %d" % recursive(ll.head, 6)
