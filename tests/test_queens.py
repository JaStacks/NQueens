# test_queens.py
#
# ICS 33 Fall 2022
# Project 0: History of Modern
#
# Unit tests for the QueensState class in "queens.py".
#
# Docstrings are not required in your unit tests, though each test does need to have
# a name that clearly indicates its purpose.  Notice, for example, that the provided
# test method is named "test_zero_queen_count_initially" instead of something generic
# like "test_queen_count", since it doesn't entirely test the "queen_count" method,
# but instead focuses on just one aspect of how it behaves.  You'll want to do likewise.

from queens import QueensState, Position, MissingQueenError
import unittest



class TestQueensState(unittest.TestCase):
    def test_zero_queen_count_initially(self):
        state = QueensState(5,5)
        self.assertEqual(state.queen_count(), 0)
    def test_return_queens(self):

        state = QueensState(8,8)
        board = state.with_queens_added([Position(4,4)])
        self.assertEqual(board.queens(),[Position(4,4)])

    def test_queen_true_position(self):

        state = QueensState(8,8)
        board = state.with_queens_added([Position(2,2)])
        self.assertEqual(board.has_queen(Position(2,2)),True)
        self.assertEqual(board.has_queen(Position(0,0)),False)


if __name__ == '__main__':
    unittest.main()
