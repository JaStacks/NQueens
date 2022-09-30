# queens.py
#
# ICS 33 Fall 2022
# Project 0: History of Modern
#
# A module containing tools that could assist in solving variants of the
# well-known "n-queens" problem.  Note that we're only implementing one part
# of the problem: immutably managing the "state" of the board (i.e., which
# queens are arranged in which cells).
#
# Your goal is to complete the QueensState class described below, though
# you'll need to build it incrementally, as well as test it incrementally by
# writing unit tests in test_queens.py.  Make sure you've read the project
# write-up before you proceed, as it will explain the requirements around
# following (and documenting) an incremental process of solving this problem.
#
# DO NOT MODIFY THE Position NAMEDTUPLE OR THE PROVIDED EXCEPTION CLASSES.

from collections import namedtuple



Position = namedtuple('Position', ['row', 'column'])

# Ordinarily, we would write docstrings within classes or their methods.
# Since a namedtuple builds those classes and methods for us, we instead
# add the documentation by hand afterward.
Position.__doc__ = 'A position on a chessboard, specified by zero-based row and column numbers.'
Position.row.__doc__ = 'A zero-based row number'
Position.column.__doc__ = 'A zero-based column number'



class DuplicateQueenError(Exception):
    """An exception indicating an attempt to add a queen where one is already present."""

    def __init__(self, position: Position):
        """Initializes the exception, given a position where the duplicate queen exists."""
        self._position = position


    def __str__(self) -> str:
        return f'duplicate queen in row {self._position.row} column {self._position.column}'



class MissingQueenError(Exception):
    """An exception indicating an attempt to remove a queen where one is not present."""

    def __init__(self, position: Position):
        """Initializes the exception, given a position where a queen is missing."""
        self._position = position


    def __str__(self) -> str:
        return f'missing queen in row {self._position.row} column {self._position.column}'



class QueensState:
    """Immutably represents the state of a chessboard being used to assist in
    solving the n-queens problem."""

    def __init__(self, rows: int, columns: int):
        """Initializes the chessboard to have the given numbers of rows and columns,
        with no queens occupying any of its cells."""
        board = []
        self.board = board
        self.rows = rows
        self.columns = columns

        for i in range(columns):
            empty_row = []
            for j in range(rows):
                empty_row.append(0)
            board.append(empty_row)


    def queen_count(self) -> int:
        """Returns the number of queens on the chessboard."""
        count = 0
        for i in self.board:
            for j in i:
                if j == 'Q':
                    count += 1
        return count
    def queens(self) -> list[Position]:
        """Returns a list of the positions in which queens appear on the chessboard,
        arranged in no particular order."""
        position_list = []
        for column in range(0,len(self.board)):
            for row in range(0,len(self.board)):
                if self.board[row][column] == 'Q':
                    position_list.append(Position(row,column))

        print(position_list)
        return position_list



    def has_queen(self, position: Position) -> bool:
        """Returns True if a queen occupies the given position on the chessboard, or
        False otherwise."""
        if self.board[position.row][position.column] == 'Q':
            return True
        else:
            return False


    def any_queens_unsafe(self) -> bool:
        """Returns True if any queens on the chessboard are unsafe (i.e., they can
        be captured by at least one other queen on the chessboard), or False otherwise."""
        pass

    def with_queens_added(self, positions: list[Position]) -> 'QueensState':
        """Builds a new QueensState with queens added in the given positions.
        Raises a DuplicateQueenException when there is already a queen in at
        least one of the given positions."""

        S = QueensState(8,8)
        for i in positions:
            S.board[i.row][i.column] = 'Q'
        return S

    def with_queens_removed(self, positions: list[Position]) -> 'QueensState':
        """Builds a new QueensState with queens removed from the given positions.
        Raises a MissingQueenException when there is no queen in at least one of
        the given positions."""
        for i in positions:
            if self.board[i.row][i.column] == 'Q':
                self.board[i.row][i.column] = 0
            else:
                raise MissingQueenError(Position(i.row,i.column))
