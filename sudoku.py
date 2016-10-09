#!/usr/bin/python
# vim: foldlevel=0

"""
Write a function that checks whether a given sudoku board is solvable.

https://www.pramp.com/question/O5PGrqGEyKtq9wpgw6XP
"""

dimension = 9


def get_next_empty_cell(board):
    try:
        return next((i, j) for i in range(dimension) for j in range(dimension) if not board[i][j])
    except StopIteration:
        pass


def get_candidate_cell_values(i, j, board):
    row_values = set([board[i][y] for y in range(dimension) if y != j and board[i][y]])
    col_values = set([board[x][j] for x in range(dimension) if x != i and board[x][j]])
    block_values = set()
    xbase, ybase = i - i%3, j - j%3
    for x in range(xbase, xbase+3):
        for y in range(ybase, ybase+3):
            if x == i and y == j or not board[x][y]:
                continue
            block_values.add(board[x][y])
    return list(set(range(1, dimension+1)) - row_values - col_values - block_values)


def solve_sudoku(board):
    next_empty = get_next_empty_cell(board)
    if next_empty is None:
        return True
    i, j = next_empty
    candidates = get_candidate_cell_values(i, j, board)
    for c in candidates:
        board[i][j] = c
        if solve_sudoku(board):
            return True
        board[i][j] = None
    return False


if __name__ == '__main__':
    board = [[None for j in range(dimension)] for i in range(dimension)]
    board[0][0] = 5
    board[0][1] = 3
    board[0][4] = 7
    board[1][0] = 6
    board[1][3] = 1
    board[1][4] = 9
    board[1][5] = 5
    board[2][1] = 9
    board[2][2] = 8
    board[2][7] = 6
    board[3][0] = 8
    board[3][4] = 6
    board[3][8] = 3
    board[4][0] = 4
    board[4][3] = 8
    board[4][5] = 3
    board[4][8] = 1
    board[5][0] = 7
    board[5][4] = 2
    board[5][8] = 6
    board[6][1] = 6
    board[6][6] = 2
    board[6][7] = 8
    board[7][3] = 4
    board[7][4] = 1
    board[7][5] = 9
    board[7][8] = 5
    board[8][4] = 8
    board[8][7] = 7
    board[8][8] = 9
    if solve_sudoku(board):
        print 'Solvable!\n'
        for i in range(dimension):
            print ' '.join([str(board[i][j]) for j in range(dimension)])
    else:
        print 'Not solvable!'
