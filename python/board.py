"""
Solving the 8 queens problem in python

"""
class UnsafeException(Exception):
    pass


class QueenNotFoundException(Exception):
    pass


class Chessboard(object):
    """simulates a Chessboard."""
    def __init__(self, n=8):
        self.board = [[0] * n for _ in range(n)]
        self.num_solutions = 0
        self.num_queens = 0

    def __len__(self):
        return len(self.board)

    def is_safe(self, row, col):
        """checks if location is safe"""
        return not self.board[row][col]

    def _change_row(self, row, unsafe=True, idx=0):
        if idx == len(self):
            return
        self.board[row][idx] += 1 if unsafe else -1
        return self._change_row(row, unsafe, idx=(idx+1))

    def _change_col(self, col, unsafe=True, idx=0):
        if idx == len(self):
            return
        self.board[idx][col] += 1 if unsafe else - 1
        return self._change_col(col, unsafe, idx=(idx+1))

    def _change_diag(self, row, col, unsafe=True):
        last_idx = len(self) - 1
        posn_left = (0, (col-row)) if row < col else ((row-col), 0)
        posn_right = (0, col + (row - 0)) if (row - 0) < (last_idx - col) else (row - (last_idx - col), last_idx)

        def _change_diag_left(self, row, col, unsafe):
            if any(val == len(self) for val in (row, col)):
                return
            self.board[row][col] += 1 if unsafe else -1
            return _change_diag_left(self, (row+1), (col+1), unsafe)

        def _change_diag_right(self, row, col, unsafe):
            if row == len(self) or col < 0:
                return
            self.board[row][col] += 1 if unsafe else -1
            # import pdb; pdb.set_trace()
            return _change_diag_right(self, (row+1), (col-1), unsafe)

        _change_diag_left(self, posn_left[0], posn_left[1], unsafe)
        _change_diag_right(self, posn_right[0], posn_right[1], unsafe)

    def place(self, row, col):
        """places a queen at the specified location"""
        if self.is_safe(row, col):
            self.board[row][col] = Queen()
            self._change_row(row)
            self._change_col(col)
            self._change_diag(row, col)
            self.num_queens += 1
            return
        raise UnsafeException('Unsafe cell')

    def remove(self, row, col):
        """removes the queen at the location"""
        if isinstance(self.board[row][col], Queen):
            self._change_row(row, unsafe=False)
            self._change_col(col, unsafe=False)
            self._change_diag(row, col, unsafe=False)
            self.board[row][col] = 0
            self.num_queens -= 1
            return
        raise QueenNotFoundException('Queen not found')


class Queen(object):
    """queen chess piece"""
    def __init__(self):
        pass

    def __add__(self, n):
        return self

    def __str__(self):
        return "Q"

    def __repr__(self):
        return self.__str__()
