#!/usr/bin/python
# vim: foldlevel=0


M = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]

i, j = 0, 0
for k in range(len(M)+len(M[0])-1):
    r, c = i, j
    while r >= 0 and c < len(M[0]):
        print M[r][c]
        r -= 1
        c += 1
    if i < len(M)-1:
        i += 1
    else:
        j += 1
