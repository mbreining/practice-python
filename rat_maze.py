#!/usr/bin/python
# vim: foldlevel=0

"""
A Maze is given as N*N binary matrix of blocks where source block is the upper
left most block i.e., maze[0][0] and destination block is lower rightmost block
i.e., maze[N-1][N-1]. A rat starts from source and has to reach destination.
The rat can move only in two directions: forward and down.

In the maze matrix, 0 means the block is dead end and 1 means the block can be
used in the path from source to destination.

http://www.geeksforgeeks.org/backttracking-set-2-rat-in-a-maze/
"""
from collections import deque


def get_next_candidates(maze, key):
    N = len(maze)
    candidates = [key+1, key+N]
    return [k for k in candidates if 0 <= k <= (N*N)-1 and maze[k // N][k % N] == 1]


def dfs(maze, cur_key, path):
    N = len(maze)
    if cur_key == (N*N)-1:
        return True
    for k in get_next_candidates(maze, cur_key):
        path[k // N][ k % N] = 1
        if dfs(maze, k, path):
            return True
        path[k // N][ k % N] = 0
    return False


def dp(maze, i, j, path, memo):
    path.appendleft((i, j))
    if memo[i][j] is None:
        res = False
        if i == 0 and j == 0:
             res = True
        else:
            if j-1 >=0 and maze[i][j-1] == 1 and dp(maze, i, j-1, path, memo):
                res = True
            if i-1 >=0 and maze[i-1][j] == 1 and dp(maze, i-1, j, path, memo):
                res = True
        memo[i][j] = res
    if not memo[i][j]:
        path.popleft()
    return memo[i][j]


if __name__ == '__main__':
    N = 4
    maze = [[0 for j in range(N)] for i in range(N)]
    maze[0][0] = 1
    maze[1][0] = 1
    maze[1][1] = 1
    maze[1][3] = 1
    maze[2][1] = 1
    maze[3][0] = 1
    maze[3][1] = 1
    maze[3][2] = 1
    maze[3][3] = 1

    # Backtracking
    path = [[0 for j in range(N)] for i in range(N)]
    start = 0
    path[0][0] = 1
    if dfs(maze, start, path):
        print 'Found a path!\n'
        for i in range(N):
            print ' '.join([str(path[i][j]) for j in range(N)])
    else:
        print 'No path found!'

    # Dynamic programming
    print '\n'
    path = deque()
    memo = [[None for j in range(N)] for i in range(N)]
    if dp(maze, 3, 3, path, memo):
        print 'Found a path!\n'
        print ' '.join([str(c) for c in path])
    else:
        print 'No path found!'
