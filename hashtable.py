#!/usr/bin/python
# vim: foldlevel=0

''' Basic hash table implementation with chaining '''


class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def add(self, key, value):
        if not self.head:
            self.head = Node(key, value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(key, value)

    def find(self, key):
        if not self.head:
            return
        node = self.head
        while node:
            if node.key == key:
                return node
            node = node.next


class HashTable(object):
    def __init__(self, size=101):
        self.size = size
        self.data = [LinkedList() for i in range(self.size)]

    def insert(self, key, value):
        i = self._get_hash(key)
        node = self.data[i].find(key)
        if node:
            node.key = key
            node.value = value
        else:
            self.data[i].add(key, value)

    def get(self, key):
        i = self._get_hash(key)
        node = self.data[i].find(key)
        if node:
            return node.value

    def _get_hash(self, key):
        h = 0
        for i in range(len(key)):
            h = (256*h + ord(key[i])) % self.size
        #print 'hash for %s is %d' % (key, h)
        return h


if __name__ == '__main__':
    d = HashTable(5)
    d.insert('jelly', 123)
    d.insert('bean', 456)
    print d.get('jelly')
    print d.get('ice')
    print d.get('bean')
