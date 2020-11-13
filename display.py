import pygame as pg


class Display:
    """
    docstring
    """

    def __init__(self, game, screen_height, screen_width, offset_height, offset_width, background_color):
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.screen = pg.display.set_mode((screen_width, screen_height))
        self.offset_height = offset_height
        self.offset_width = offset_width
        self.background_color = background_color
        self.game = game

    def draw_screen(self):
        self.screen.fill(self.background_color)
        cell_h = self.game.cell_height
        for i in range(10):
            thickness = self.game.line_thickness
            if i % 3 == 0:
                thickness = self.game.line_thickness * 2
            pg.draw.line(self.screen, self.game.line_color,
                         pg.Vector2(
                             ((i * cell_h) + self.offset_width, self.offset_height)),
                         pg.Vector2((i * cell_h) + self.offset_width, 9 * cell_h + self.offset_height), thickness)
            pg.draw.line(self.screen, cell_h,
                         pg.Vector2(self.offset_width,
                                    (i * cell_h) + self.offset_height),
                         pg.Vector2(9 * cell_h + self.offset_width, (i * cell_h) + self.offset_height), thickness)

        self.game.draw_numbers(
            self.screen, self.offset_width, self.offset_height)
        pg.display.update()
