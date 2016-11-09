#!/usr/bin/python
# vim: foldlevel=0

"""
Write an implementation of the game Connect-4 (http://en.wikipedia.org/wiki/Connect_Four).
In Connect-4, there are two players, and each of the players take turns trying
to get four of their game pieces in a row. Write a functional subset of the code
for the game board, game pieces, and player state. Your code should include
functions to place a piece into the game board and check if one of the players
has won the game. Your code should simulate the turns taken by players
(in other words, you do NOT have to collect actual input from players, so you
should not build UI to do so).

Your code should also include a function to print out the board, in ASCII.
For example, here is a plausible print out after two turns - one from player 'x'
and player 'o':

  * * * * * * *
  * * * * * * *
  * * * * * * *
  * * * * * * *
  * x o * * * *

"""

from collections import namedtuple
from itertools import chain, cycle

Player = namedtuple('Player', ['color', 'marker'])


class InvalidMove(Exception):
    pass


class ConnectFour(object):
    def __init__(self, cols=7, rows=6):
        self.cols = cols
        self.rows = rows
        # Note: columns and rows are 0-indexed.
        self.board = [['*' for c in range(self.cols)] for r in range(self.rows)]
        self.over = False
        self.moves = 0  # keep track of number of moves
        self.players = (Player('red', 'x'), Player('yellow', 'o'))
        self.next_player = cycle(self.players).next
        self.winner = None

    def play(self, col):
        """
        Play the next move, i.e. have the next player add a piece into the game board,
        check whether it is a valid move, and if so check to see if one the players has
        won the game. Note that the game internally knows who the next player is.

        :param: col - The column number in which a piece is added.
        :type: int
        """
        player = self.next_player()
        print "Next player is {0}: adding piece {1} into column {2}".format(player.color,
                                                                            player.marker,
                                                                            col)

        if col < 0 or col > self.cols-1:
            raise InvalidMove("Invalid column number {0}; exiting...".format(str(col)))

        self._add_piece(player, col)
        self._check_status()
        if self.over:
            print "We have a winner after {0} moves: {1}".format(self.moves,
                                                                 self.winner.color)

    def display(self):
        """
        Display board as ascii.
        """
        grid = "\n"
        for row in self.board:
            grid += " ".join([str(c) for c in row])
            grid += "\n"
        print grid

    def _add_piece(self, player, col):
        """
        Add a piece into the game board.
        :param: player - The player that's adding a piece
        :type: Player namedtuple
        :param: col - The column number where a piece is being added (0-indexed)
        :type: int
        """
        for row in reversed(range(self.rows)):
            if self.board[row][col] == '*':
                self.board[row][col] = player.marker
                break
        else:  # no break
            raise InvalidMove("There is no more room in this column; exiting...")
        self.moves += 1

    def _check_status(self):
        """
        Check if we have a winner, i.e. four consecutive pieces of the same color.
        If a winner is found, self.over and self.winner are set appropriately.
        """
        for slice in chain(self._get_rows(),
                           self._get_columns(),
                           self._get_diagonals()):
            winner = self._check_slice(list(slice))
            if winner:
                self.winner = filter(lambda p: p.marker == winner, self.players)[0]
                self.over = True
                return

    def _check_slice(self, slice):
        """
        Check if a slice (row, column, diagonal) contains four consecutive pieces of the
        same color.

        :param: slice - A slice representing a row, column or diagonal.
        :type: list
        """
        start, prev = -1, '*'
        for i in range(len(slice)):
            if slice[i] == '*':  # no piece
                start, prev = -1, '*'
            elif prev == '*':  # a new piece x or o
                start, prev = i, slice[i]
            elif slice[i] == prev:  # a piece that matches the previous one visited
                if i-start+1 == 4:
                    return slice[i]
            else:  # a piece that does not match the previous one visited
                start, prev = i, slice[i]

    def _get_rows(self):
        return self.board

    def _get_columns(self):
        return zip(*self.board)

    def _get_diagonals(self):
        diags = []
        for offset in range(self.cols+self.rows-1):
            # Each iteration generates two diagonals:
            # top-left to bottom-right and bottom-left to top-right
            diag1, diag2 = [], []
            for i in range(self.rows):
                for j in range(self.cols):
                    if i+j == offset:
                        diag1.append(self.board[i][j])
                        diag2.append(self.board[self.rows-i-1][j])
            diags += [diag1, diag2]
        return diags


if __name__ == "__main__":
    # Game w/ winning pieces in a column
    #moves = (m for m in [5, 5, 0, 0, 5, 0, 5, 6, 2, 2, 5, 0, 2, 0])
    # Game w/ winning pieces in a row
    #moves = (m for m in [5, 5, 1, 0, 3, 0, 4, 6, 2, 2, 5, 0, 2, 0])
    # Game w/ winning pieces in a diagonal
    moves = (m for m in [5, 5, 0, 0, 5, 0, 5, 6, 2, 2, 5, 1, 2, 1, 6, 3, 4, 1, 4, 0])

    game = ConnectFour()
    while not game.over:
        try:
            game.play(moves.next())
        except StopIteration:
            print "There is no winner in this game!"
            break
        game.display()
