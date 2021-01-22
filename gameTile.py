import pygame

tiles_in_row = 8


class GameTile:
    def __init__(self, screen, unit_size, color, x=0, y=0, piece=None):
        self.x = x
        self.y = y
        self.screen = screen
        self.color = color
        self.piece = piece
        self.unit_size = unit_size
        self.tile = pygame.Rect(self.x * self.unit_size, self.y * self.unit_size, self.unit_size, self.unit_size)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.tile)
        if self.piece is not None:
            self.piece.draw()
        pygame.display.flip()

    def select(self):
        try:
            self.piece.select()
        except AttributeError:
            return

    def deselect(self):
        try:
            self.piece.deselect()
        except AttributeError:
            return
