#!/usr/bin/python
# vim: foldlevel=0

"""
Problem 1: Add two numbers represented by two linked lists in reverse order, and
return the sum as a linked list.

Problem 2: Same as above but the input linked lists are in forward order.
"""
from linked_list import Node, randlinkedlist


def add_reversed(node1, node2, carry):
    if not node1 and not node2 and carry == 0:
        return
    sum = carry
    if node1:
        sum += node1.value
    if node2:
        sum += node2.value
    q, r = divmod(sum, 10)
    node = Node(r)
    node.next = add_reversed(node1.next if node1 else None,
                             node2.next if node2 else None,
                             q)
    return node


def solution1(head1, head2):
    return add_reversed(head1, head2, 0)


def add_forward(node1, node2):
    if not node1 and not node2:
        return (None, 0)
    next, carry = add_forward(node1.next, node2.next)
    q, r = divmod(node1.value + node2.value + carry, 10)
    node = Node(r)
    node.next = next
    return (node, q)


def length(head):
    len = 0
    node = head
    while node:
        node, len = node.next, (len+1)
    return len


def pad_with_zeros(head, count):
    for i in range(count):
        node = Node(0)
        node.next, head = head, node  # insert at front
    return head


def solution2(head1, head2):
    # If linked lists have different lengths, pad with 0s
    len1, len2 = length(head1), length(head2)
    if len1 < len2:
        head1 = pad_with_zeros(head1, len2-len1)
    elif len1 > len2:
        head2 = pad_with_zeros(head2, len1-len2)

    # Now that the linked lists are of equal size, add them
    head, carry = add_forward(head1, head2)
    if carry != 0:
        node = Node(carry)
        node.next, head = head, node  # insert at front

    return head


if __name__ == "__main__":
    def _print(head):
        cur = head
        while cur:
            print cur.value
            cur = cur.next

    ll1 = randlinkedlist(3, max=9)
    ll2 = randlinkedlist(5, max=9)
    print "Linked list 1:"
    _print(ll1.head)
    print "Linked list 2:"
    _print(ll2.head)

    print "Sum of linked lists (reversed):"
    _print(solution1(ll1.head, ll2.head))

    print "Sum of linked lists (not reversed):"
    _print(solution2(ll1.head, ll2.head))
