#!/usr/bin/python

"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a
pair of nodes), write a function to check whether these edges make up a valid tree.

Note: you can assume that no duplicate edges will appear in edges. Since all edges are
undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

For example:
Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

http://nb4799.neu.edu/wordpress/?p=1143
http://www.geeksforgeeks.org/detect-cycle-undirected-graph/
"""


def union(parents, v1, v2):
    parents[v1] = v2


def find(parents, v):
    while parents[v] != -1:
        v = parents[v]
    return v


def solution1(n, edges):
    """
    >>> solution1(5, [[0, 1], [0, 2], [0, 3], [1, 4]])
    True
    >>> solution1(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])
    False
    """
    if len(edges) != n-1:
        return False

    # Initialize union find array
    parents = []
    for i in range(5):
        parents[i] = -1

    # Check for cycles
    for v1, v2 in edges:
        s1, s2 = find(parents, v1), find(parents, v2)
        if s1 == s2:
            return False
        union(parents, v1, v2)

    return True


def dfs(vertex, vertices, recstack, visited):
    recstack.append(vertex)
    visited[vertex] = True
    for v in vertices[vertex]:
        if v in recstack:
            return True
        if not visited[v]:
            dfs(v, vertices, recstack, visited)
    recstack.pop()
    return False


def solution2(n, edges):
    """
    >>> solution2(5, [[0, 1], [0, 2], [0, 3], [1, 4]])
    True
    >>> solution2(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])
    False
    """
    from collections import defaultdict

    # Build adjacency list
    vertices = defaultdict(list)
    for v1, v2 in edges:
        vertices[v1].append(v2)
        vertices[v2].append(v1)

    # Check for cycles w/ DSF
    recstack = []  # recursion stack
    visited = []
    for v in vertices:
        visited[v] = False

    for v in vertices:
        if not visited[v]:
            has_cycle = dfs(v, vertices, recstack, visited)
            if has_cycle:
                return False

    return True
