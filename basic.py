import pprint as pp
import timeit

UNDEFINED_CELL = (-1, -1)

board = [[0, 0, 0, 0, 7, 0, 0, 4, 5],
         [4, 0, 0, 0, 0, 0, 8, 0, 0],
         [8, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 8, 0, 0, 0, 2, 0, 0, 0],
         [0, 0, 0, 5, 9, 0, 0, 6, 0],
         [2, 1, 0, 0, 0, 4, 0, 0, 0],
         [5, 0, 0, 4, 0, 0, 0, 0, 3],
         [0, 0, 2, 0, 0, 0, 0, 0, 7],
         [0, 0, 0, 6, 0, 0, 0, 5, 4]]


def get_col(arr, col):
    return [row[col] for row in arr]


def find_blank_cell(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 0:
                return (i, j)
    return UNDEFINED_CELL


def is_fitting_square(arr, pos, new_value):
    (x, y) = pos
    square_x = x // 3
    square_y = y // 3

    for i in range(square_x * 3, (square_x + 1) * 3):
        for j in range(square_y * 3, (square_y + 1) * 3):
            if arr[i][j] == new_value:
                return False
    return True


def get_square(arr, pos):
    (x, y) = pos
    square_x = x // 3
    square_y = y // 3

    return [row[col] for row in arr[square_x * 3:square_x * 3 + 3] for col in range(square_y * 3, (square_y + 1) * 3)]


def is_valid_move(arr, new_value, pos):
    (x, y) = pos

    if new_value in arr[x]:
        return False

    if new_value in get_col(arr, y):
        return False

    # if not is_fitting_square(arr, pos, new_value):
    #     return False
    if new_value in get_square(arr, pos):
        return False
    return True


def resolve_sudoku(arr):

    pos = find_blank_cell(arr)
    if pos != UNDEFINED_CELL:
        (x, y) = pos
    else:
        return True

    for new_val in range(1, 10):
        if is_valid_move(arr, new_val, pos):
            arr[x][y] = new_val

            if resolve_sudoku(arr):
                return True

        arr[x][y] = 0

    return False


def main():

    pp.pprint(board)
    print("=========================================")
    if not resolve_sudoku(board):
        print("No solution found!")
    else:
        pp.pprint(board)


if __name__ == "__main__":
    main()
