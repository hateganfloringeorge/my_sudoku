import pygame as pg
import sys

from display import Display
from game import Game
from buttons import Button

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

    game = Game(my_board, 3, pg.Color('black'), 55)
    disp = Display(game, 550, 750, 10, pg.Color('white'))

    running = True

    buttons = []

    start_button = Button(pg.Color('green'),
                          pg.Color('white'), 100, 600, 70, 30, 'Start')

    quit_button = Button(pg.Color('blue'),
                         pg.Color('white'), 300, 600, 70, 30, 'Quit')

    buttons.append(start_button)
    buttons.append(quit_button)

    while running:
        for event in pg.event.get():
            pos = pg.mouse.get_pos()

            if event.type == pg.QUIT:
                running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    disp.game.resolve_sudoku(disp.screen, disp.draw_screen)

            if event.type == pg.MOUSEBUTTONDOWN:
                if quit_button.isOver(pos):
                    running = False
                if start_button.isOver(pos):
                    running = False

            if event.type == pg.MOUSEMOTION:
                for button in buttons:
                    button.isOver(pos)

        disp.draw_screen()
        for button in buttons:
            button.draw(disp.screen, pg.Color('black'))
        pg.display.update()


if __name__ == "__main__":
    main()
