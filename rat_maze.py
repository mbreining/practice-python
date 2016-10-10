#!/usr/bin/python
# vim: foldlevel=0

"""
"""

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
    path = [[0 for j in range(N)] for i in range(N)]
    start = 0
    path[0][0] = 1
    if dfs(maze, start, path):
        print 'Found a path!\n'
        for i in range(N):
            print ' '.join([str(path[i][j]) for j in range(N)])
    else:
        print 'No path found!'
