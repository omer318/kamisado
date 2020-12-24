import pygame
import game_piece
tiles_in_row = 8


class GameTile:
    def __init__(self, screen, unit_size, color, x=0, y=0):
        self.x = x
        self.y = y
        self.screen = screen
        self.color = color
        self.occupied = None
        self.screen = screen
        self.unit_size = unit_size

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.tile)
        pygame.display.flip()
