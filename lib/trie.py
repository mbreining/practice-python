
class Trie(object):
    def __init__(self):
        self.root = Node('/')

    def add(self, word):
        word = word.lower()
        node = self.root
        for c in word:
            idx = ord(c)-ord('a')
            if not node.children[idx]:
                node.children[idx] = Node(c)
            node = node.children[idx]

    def find(self, word):
        word = word.lower()
        node = self.root
        for c in word:
            idx = ord(c)-ord('a')
            node = node.children[idx]
            if not node:
                return
        return node


class Node(object):
    def __init__(self, key):
        self.key = key
        self.children = [None] * 26  # latin alphabet
