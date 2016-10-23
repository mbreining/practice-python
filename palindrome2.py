#!/usr/bin/python
# vim: foldlevel=0

"""
Check if a linked list is a palindrome, e.g. r->a->d->a->r.
"""
from linked_list import Node


def visit(node, length):
    if length == 1:
        return node.next
    if length == 2:
        if node.value == node.next.value:
            return node.next.next
        else:
            return -1
    last_node = visit(node.next, length-2)
    if last_node != -1:
        if node.value == last_node.value:
            return last_node.next
    return -1


def palindrome(head):
    length = 0
    node = head
    while node:
        length += 1
        node = node.next
    print visit(head, length)


head = Node('r')
head.next = Node('a')
head.next.next = Node('d')
head.next.next.next = Node('a')
head.next.next.next.next = Node('r')

palindrome(head)  # None if palindrome, -1 otherwise
