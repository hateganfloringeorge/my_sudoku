import pygame as pg


class Button():
    def __init__(self, color, hover_color, x, y, width, height, text=''):
        self.color = color
        self.hover_color = hover_color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.is_hovered = False

    def draw(self, screen, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pg.draw.rect(screen, outline, (self.x-2, self.y -
                                           2, self.width+4, self.height+4), 0)

        button_color = self.color
        if self.is_hovered:
            button_color = self.hover_color
        pg.draw.rect(screen, button_color, (self.x, self.y,
                                            self.width, self.height), 0)

        if self.text != '':
            font = pg.font.SysFont('comicsans', self.height * 4 // 3)
            text = font.render(self.text, 1, (0, 0, 0))
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2),
                               self.y + (self.height/2 - text.get_height()/2.5)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                self.is_hovered = True
                return True

        self.is_hovered = False
        return False
