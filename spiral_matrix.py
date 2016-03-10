#!/usr/bin/python

"""
Given a 2D array, print it in spiral form. See the following examples.

Input:
    1    2   3   4
    5    6   7   8
    9   10  11  12
    13  14  15  16
Output:
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10

Input:
    1   2   3   4  5   6
    7   8   9  10  11  12
    13  14  15 16  17  18
Output:
1 2 3 4 5 6 12 18 17 16 15 14 13 7 8 9 10 11

http://www.geeksforgeeks.org/print-a-given-matrix-in-spiral-form/
"""


def solution(m):
    """
    This solution traverses and prints either one row or one colum per iteration of the
    while loop. It is not very concise.
    A cleaner solution involves traversing and printing two rows and two columns per
    iteration (one complete circle).
    See: http://www.geeksforgeeks.org/median-of-stream-of-integers-running-integers/

    >>> solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
    """
    res = []
    pos = [0, 0]
    rows_left, cols_left = len(m), len(m[0])

    i = 0  # iterator
    while rows_left or cols_left:  # one iteration prints either one row or one col
        if i % 2 == 0:  # we're about to print a row, i.e. traverse cols
            cur_row = pos[0]
            if i % 4 == 0:  # from left to right
                cols = range(pos[1], pos[1]+cols_left)
                pos[0] += 1
            else:  # from right to left
                cols = range(pos[1], pos[1]-cols_left, -1)
                pos[0] -= 1
            for j in cols:
                res.append(m[cur_row][j])
            pos[1] = j
            rows_left -= 1
        else:  # we're about to print a col, i.e. traverse rows
            cur_col = pos[1]
            if (i-1) % 4 == 0:  # from top to bottom
                rows = range(pos[0], pos[0]+rows_left)
                pos[1] -= 1
            else:  # from bottom to top
                rows = range(pos[0], pos[0]-rows_left, -1)
                pos[1] += 1
            for j in rows:
                res.append(m[j][cur_col])
            pos[0] = j
            cols_left -= 1
        i += 1
    print " ".join([str(x) for x in res])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
