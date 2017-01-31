#!/usr/bin/python
# vim: foldlevel=0

"""
http://blog.gainlo.co/index.php/2016/06/12/flatten-a-linked-list/
"""
from collections import deque


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.child = None


def iterative(head):
    queue = deque()
    node = head
    prev = None
    while node or queue:
        if not node:
            node = queue.pop()
            prev.next = node
        if node.child:
            queue.appendleft(node.child)
        prev, node = node, node.next


queue = deque()


def recursive(node):
    if not node and not queue:
        return
    if not node:
        node = queue.pop()
    if node.child:
        queue.appendleft(node.child)
    node.next = recursive(node.next)
    return node


def print_linked_list(head):
    nodes = []
    while head:
        nodes.append(head.value)
        head = head.next
    print ", ".join([str(n) for n in nodes])


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.child = Node(5)
    head.next.child.next = Node(6)
    head.next.next.next.child = Node(7)
    head.next.child.child = Node(8)
    head.next.next.next.child.child = Node(9)

    iterative(head)
    #recursive(head)
    print_linked_list(head)
