"""
Solving the 8 queens problem in python

"""
class UnsafeException(Exception):
    pass

class Chessboard(object):
    """simulates a Chessboard."""
    def __init__(self, n=8):
        self.board = [[0] * n for _ in range(n)]

    def total_solutions(self):
        pass

    def is_safe(self, row, col):
        """checks if location is safe"""
        return not self.board[row][col]

    def _change_row(self, row, option='unsafe', idx=0):
        if idx == len(self.board[row]) - 1:
            self.board[row][idx] += 1 if option == 'unsafe' else -1
            return
        self.board[row][idx] += 1 if option == 'unsafe' else -1
        return self._change_row(row, option, idx=(idx+1))

    def _change_col(self, col, option="unsafe"):
        pass

    def _change_diag(self, row, col, option="unsafe"):
        pass

    def place(self, row, col):
        """places a queen at the specified location"""
        if self.is_safe(row, col):
            self.board[row][col] = Queen()
            self._change_row(row)
            self._change_col(col)
            self._change_diag(row, col)
            return
        raise UnsafeException('Unsafe cell')

    def remove(self, row, col):
        """removes the queen at the location"""
        pass


class Queen(object):
    """queen chess piece"""
    def __init__(self):
        pass

    def __str__(self):
        return "Q"

    def __add__(self, other):
        return self

    def __repr__(self):
        return self.__str__()
