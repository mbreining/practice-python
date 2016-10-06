#!/usr/bin/python
# vim: foldlevel=0

"""
Given a dictionary, a method to lookup a word in the dictionary and a MxN board
where every cell has one character, find all possible words that can be formed
by a sequence of adjacent characters.

http://www.geeksforgeeks.org/boggle-find-possible-words-board-characters/
"""


class Vertex(object):
    def __init__(self, key):
        self.key = key
        self.adjlist = []
        self.visited = False


def get_cell_key(i, j, M, N):
    return i*N+j


def get_adjacent_cells(i, j, M, N):
    adj = [(i+1, j), (i+1, j-1), (i, j-1), (i-1, j-1), (i-1, j), (i-1, j+1), (i, j+1), (i+1, j+1)]
    return [(x, y) for x, y in adj if 0 <= x <= M-1 and 0 <= y <= N-1]


def add_vertex(key, vertices):
    if not vertices.get(key):
        vertices[key] = Vertex(key)
    return vertices[key]


def build_graph(board):
    vertices = {}  # the graph
    M, N = len(board), len(board[0])
    for i in range(M):
        for j in range(N):
            key = get_cell_key(i, j, M, N)
            u = add_vertex(key, vertices)
            for adj_i, adj_j in get_adjacent_cells(i, j, M, N):
                key = get_cell_key(adj_i, adj_j, M, N)
                v = add_vertex(key, vertices)
                u.adjlist.append(v)
    return vertices


def is_word(w, dictionary):
    ''' Naive implementation. A better solution would use a trie. '''
    return w in dictionary


def dfs(u, vertices, board, dictionary, stack, res):
    u.visited = True
    stack.append(u.key)

    # Check if we have a word
    M = len(board)
    curword = ''.join([board[k / M][k % M] for k in stack])
    if is_word(curword, dictionary):
        res.append(curword)

    # Process vertices in the current adjacent list
    for v in u.adjlist:
        if not v.visited:
            dfs(v, vertices, board, dictionary, stack, res)

    stack.pop()
    u.visited = False


def solution(dictionary, board):
    """
    >>> board = [['g', 'i', 'z'], ['u', 'e', 'k'], ['q', 's', 'e']]
    >>> solution(['geeks', 'for', 'quiz', 'go'], board)
    ['geeks', 'quiz']
    """
    res = []
    vertices = build_graph(board)
    for _, u in vertices.iteritems():
        if not u.visited:
            dfs(u, vertices, board, dictionary, [], res)
    return res


if __name__ == '__main__':
    import doctest
    doctest.testmod()
