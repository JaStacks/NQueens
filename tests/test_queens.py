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

from queens import QueensState, Position
import unittest



class TestQueensState(unittest.TestCase):
    def test_zero_queen_count_initially(self):
        state = QueensState(5, 5)
        self.assertEqual(state.queen_count(), 0)


    def test_one_queen_count(self):
        state = QueensState(8,8)
        P = Position(2,2)
        state.with_queens_added(P)
        self.assertEqual(state.queen_count(), 1)

    def test_two_queen_count(self):
        state = QueensState(5,5)
        P = Position(2,3)
        Q = Position(3,2)
        state.with_queens_added([P,Q])
        self.assertEqual(state.queen_count(),2)
    def test_three_queens_count(self):
        state = QueensState(8,8)
        state.with_queens_added([Position(1,0),Position(1,2),Position(2,0)])
        self.assertEqual(state.queen_count(),3)
    def test_position_of_one_queen(self):
        P = Position(2,2)
        state = QueensState(5,5)
        state.with_queens_added(P)
        self.assertEqual(len(state.queens()),1)

    def test_position_of_two_queens(self):
        state = QueensState(8,8)
        state.with_queens_added([Position(2,2),Position(0,1)])
        self.assertEqual(len(state.queens()),2)



if __name__ == '__main__':
    unittest.main()
