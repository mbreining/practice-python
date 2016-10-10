#!/usr/bin/python
# vim: foldlevel=0

"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a
pair of nodes), write a function to check whether these edges make up a valid tree.

Note: you can assume that no duplicate edges will appear in edges. Since all edges are
undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

For example:
Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

Follow-up: Same but with a directed graph.

http://nb4799.neu.edu/wordpress/?p=1143
http://www.geeksforgeeks.org/detect-cycle-undirected-graph/
"""


def union(parents, v1, v2):
    parents[v1] = v2


def find(parents, v):
    while parents[v] != -1:
        v = parents[v]
    return v


def undirected1(n, edges):
    """
    Time complexity: O(Elog(V))
    >>> undirected1(5, [[0, 1], [0, 2], [0, 3], [1, 4]])
    True
    >>> undirected1(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])
    False
    """
    if len(edges) != n-1:
        return False

    # Initialize union find array
    parents = [-1] * n

    # Check for cycles
    for v1, v2 in edges:
        s1, s2 = find(parents, v1), find(parents, v2)
        if s1 == s2:
            return False
        union(parents, v1, v2)

    return True


class Vertex(object):
    def __init__(self, key):
        self.key = key
        self.adjlist = []
        self.color = 0  # 0 for white, 1 for grey and 2 for black
        self.parent = None


def has_cycle(u, vertices):
    u.color = 1  # visited
    for v in u.adjlist:
        if v.color == 0:  # not visited
            v.parent = u
            if has_cycle(v, vertices):
                return True
        else:  # vertex has already been visited
            if v != u.parent:
                return True  # we found a cycle
    return False


def undirected2(n, edges):
    """
    Time complexity: O(E+V)
    >>> undirected2(5, [[0, 1], [0, 2], [0, 3], [1, 4]])
    True
    >>> undirected2(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])
    False
    """
    vertices = {}  # the graph
    # Build graph
    for i, j in edges:
        if not vertices.get(i):
            vertices[i] = Vertex(i)
        u = vertices[i]
        if not vertices.get(j):
            vertices[j] = Vertex(j)
        v = vertices[j]
        u.adjlist.append(v)
        v.adjlist.append(u)

    # Run DFS on graph
    for _, vertex in vertices.iteritems():
        if vertex.color == 0:  # not visited
            if has_cycle(vertex, vertices):
                return False

    return True


def has_cycle2(u, vertices):
    u.color = 1  # visited
    for v in u.adjlist:
        if v.color == 0:  # not visited
            if has_cycle2(v, vertices):
                return True
        elif v.color == 1:  # visited but not processed yet
            return True  # we found a cycle
    u.color = 2  # processed
    return False


def directed(n, edges):
    """
    Time complexity: O(E+V)
    >>> directed(5, [[0, 1], [0, 2], [0, 3], [1, 4]])
    True
    >>> directed(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])
    True
    >>> directed(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4], [3, 4], [4,0]])
    False
    """
    vertices = {}  # the graph
    # Build graph
    for i, j in edges:
        if not vertices.get(i):
            vertices[i] = Vertex(i)
        u = vertices[i]
        if not vertices.get(j):
            vertices[j] = Vertex(j)
        v = vertices[j]
        u.adjlist.append(v)  # directed

    # Run DFS on graph
    for _, vertex in vertices.iteritems():
        if vertex.color == 0:  # not visited
            if has_cycle2(vertex, vertices):
                return False

    return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()
