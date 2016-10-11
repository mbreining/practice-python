#!/usr/bin/python
# vim: foldlevel=0

"""
Construct an H-tree, given its center (x and y coordinates), starting_length
and depth. You can assume that you have a drawLine method.

https://www.pramp.com/question/EmYgnOgVd4IElnjAnQqn
"""


def draw_tree(x, y, length, depth):
    if depth == 0:
        return

    offset = length/2
    drawLine(x-offset, y, x+offset, y)  # horizontal line
    drawLine(x-offset, y-offset, x-offset, y+offset)  # left vertical line
    drawLine(x+offset, y-offset, x+offset, y+offset)  # right vertical line

    draw_tree(x-offset, y+offset, length/sqrt(2), depth-1)
    draw_tree(x+offset, y+offset, length/sqrt(2), depth-1)
    draw_tree(x+offset, y-offset, length/sqrt(2), depth-1)
    draw_tree(x-offset, y-offset, length/sqrt(2), depth-1)


draw_tree(x, y, starting_length, depth)
