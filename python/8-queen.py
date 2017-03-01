from board import Chessboard, Queen, UnsafeException, QueenNotFoundException


def main():
    """main function"""
    pass
    # b = Chessboard()
    # print(find_solutions_recursive(b))


def find_solutions(b, row=0, col=0):
    pass
    # if row == len(b):
    #     return
    # col += 1 if place_queen_in_row(0, row, col)


def find_solutions_recursive(b, row=0, col=0):
    try:
        if row == 0 and place_queen_in_row(b, row, col) is False:
            return
        if row == len(b) - 1:
            if place_queen_in_row(b, row, col):
                b.num_solutions += 1
                return find_solutions_recursive(b, row, col)
            return find_solutions_recursive(b, (row-1), col)
        row += 1 if else -1
        # import pdb; pdb.set_trace()
        return find_solutions_recursive(b, row, col)
    except:
        import pdb; pdb.set_trace()


def place_queen_in_row(b, row, col=0):
    if col == len(b):
        return False
    try:
        b.place(row, col)
        return True
    except UnsafeException:
        if isinstance(b.board[row][col], Queen):
            b.remove(row, col)
        return False or place_queen_in_row(b, row, (col+1))


if __name__ == '__main__':
    main()
