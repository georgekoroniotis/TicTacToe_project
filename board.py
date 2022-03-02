from numpy import *


class Board:
    def __init__(self):
        self.board = reshape(array([['', '', ''], ['', '', ''], ['', '', '']]), (3, 3))

    def display_board(self):
        print(self.board)

    def mark_occurrences(self, marker):
        return count_nonzero(self.board == marker)
