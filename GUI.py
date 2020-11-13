import pygame as pg
import sys

from display import Display
from game import Game


my_board = [[0, 6, 0, 0, 0, 0, 9, 1, 0],
            [2, 0, 3, 0, 1, 5, 6, 8, 0],
            [0, 0, 0, 6, 0, 3, 2, 5, 4],
            [0, 2, 0, 0, 0, 1, 3, 0, 0],
            [1, 5, 0, 0, 4, 0, 0, 0, 6],
            [0, 0, 0, 2, 0, 0, 8, 9, 0],
            [0, 0, 6, 0, 0, 2, 0, 7, 9],
            [4, 0, 7, 0, 9, 0, 0, 6, 2],
            [9, 1, 2, 7, 0, 0, 5, 0, 0], ]


def main():
    pg.font.init()
    pg.display.set_caption("Sudoku by Hategan Florin")

    game = Game(my_board, 3, pg.Color('black'), 70)
    disp = Display(game, 750, 750, 50, 50, pg.Color('white'))

    running = True

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    disp.game.resolve_sudoku(disp.screen, disp.draw_screen)

        disp.draw_screen()


if __name__ == "__main__":
    main()
