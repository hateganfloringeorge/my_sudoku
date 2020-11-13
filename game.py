import pygame as pg


class Game:
    """
    docstring
    """

    def __init__(self, board, line_thickness, line_color, cell_height):
        self.board = board
        self.line_thickness = line_thickness
        self.line_color = line_color
        self.cell_height = cell_height
        self.initial_board = board
        self.undefined_cell = (-1, -1)

    def draw_numbers(self, screen, off_width, off_height):
        font = pg.font.SysFont(None, self.cell_height)
        for i in range(9):
            for j in range(9):
                nr = self.board[i][j]
                n_text = font.render(str(nr), True, pg.Color('black'))
                screen.blit(n_text, pg.Vector2(
                    (i * self.cell_height + off_width + self.cell_height / 3),
                    (j * self.cell_height + off_height + self.cell_height / 4)))

    def get_col(self, col):
        return [row[col] for row in self.board]

    def find_blank_cell(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    return (i, j)
        return self.undefined_cell

    def is_fitting_square(self, pos, new_value):
        (x, y) = pos
        square_x = x // 3
        square_y = y // 3

        for i in range(square_x * 3, (square_x + 1) * 3):
            for j in range(square_y * 3, (square_y + 1) * 3):
                if self.board[i][j] == new_value:
                    return False
        return True

    def get_square(self, pos):
        (x, y) = pos
        square_x = x // 3
        square_y = y // 3

        return [row[col] for row in self.board[square_x * 3:square_x * 3 + 3] for col in range(square_y * 3, (square_y + 1) * 3)]

    def is_valid_move(self, new_value, pos):
        (x, y) = pos

        if new_value in self.board[x]:
            return False

        if new_value in self.get_col(y):
            return False

        if not self.is_fitting_square(pos, new_value):
            return False
        return True

    def resolve_sudoku(self, screen, refresh):

        pos = self.find_blank_cell()
        if pos != self.undefined_cell:
            (x, y) = pos
        else:
            return True

        for new_val in range(1, 10):
            if self.is_valid_move(new_val, pos):
                self.board[x][y] = new_val
                refresh()
                pg.time.delay(100)
                if self.resolve_sudoku(screen, refresh):
                    return True

            self.board[x][y] = 0

        return False
