#!/usr/bin/python
# vim: foldlevel=0

"""
Transform word1 into word2. At each step you must transform one word into another word.
You are not allowed to transform a word into a non-word.

http://interactivepython.org/runestone/static/pythonds/Graphs/TheWordLadderProblem.html
A good example of graph BFS.
"""
from collections import defaultdict, deque
from graph import Graph, Vertex


def build_graph(word_file='/usr/share/dict/words'):
    buckets = defaultdict(list)
    words = open(word_file, 'r')
    for word in words:
        word = word[:-1]  # remove \n character at end of string
        if len(word) != 4:
            continue
        for i in range(4):
            key = list(word)
            key[i] = '_'
            key = "".join(key)
            buckets[key].append(word)

    graph = Graph()
    while buckets:
        bucket, words = buckets.popitem()
        for word1 in words:
            v1 = graph.add_vertex(word1)
            for word2 in words:
                if word1 != word2:
                    v2 = graph.add_vertex(word2)
                    v1.add_neighbor(v2)

    return graph


def print_shortest_path(vertex):
    stack = []
    while vertex:
        stack.append(vertex.key)
        vertex = vertex.parent

    print
    print "The shortest path is:"
    print
    while stack:
        print stack.pop()


def find_shortest_path(graph, word1='pool', word2='sage'):
    queue = deque()
    queue.appendleft(word1)  # the starting point
    graph.vertices[word1].color = Vertex.GRAY

    while queue:
        word = queue.pop()
        print "Processing vertex {0}".format(word)
        vertex = graph.vertices[word]

        if vertex.key == word2:  # we found the end point
            print "Found end point {0}".format(word2)
            print_shortest_path(vertex)
            break

        for neighbor in vertex.neighbors:
            if neighbor.color == Vertex.WHITE:
                queue.appendleft(neighbor.key)
                neighbor.color = Vertex.GRAY
                neighbor.parent = vertex
        vertex.color = Vertex.BLACK


g = build_graph()
find_shortest_path(g, 'okee', 'stam')
