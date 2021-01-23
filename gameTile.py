import pygame

from enums import COLOR

tiles_in_row = 8


class GameTile:
    def __init__(self, screen, unit_size, color, x=0, y=0, piece=None):
        self.x = x
        self.y = y
        self.screen = screen
        self.color = color
        self.piece = piece
        self.unit_size = unit_size
        self.is_marked = False
        self.tile = pygame.Rect(self.x * self.unit_size, self.y * self.unit_size, self.unit_size, self.unit_size)

    def draw(self):
        pygame.draw.rect(self.screen, self.color.value, self.tile)
        if self.piece is not None:
            self.piece.draw()
        if self.is_marked:
            pygame.draw.circle(self.screen, COLOR.BLACK.value,
                               (int((self.x + 0.5) * self.unit_size), int((self.y + 0.5) * self.unit_size)), 4)
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

    def mark(self):
        self.is_marked = True

    def unmark(self):
        self.is_marked = False
