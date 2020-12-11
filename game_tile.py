import pygame
import game_piece
tiles_in_row = 8


class game_tile():
    def __init__(self, screen, color, unit_size, x=0, y=0):
        self.x = x
        self.y = y
        self.mo
        self.color = color
        self.occupied = None
        self.screen = screen
        self.unit_size = unit_size

    def draw(self):
        pygame.draw.rect(self.screen, self.color,
                         pygame.Rect(self.x * self.unit_size, self.y * self.unit_size, self.unit_size, self.unit_size))
        pygame.display.flip()

    def move(self, x, y):
        self.x += x
        self.y += y
        if self.x >= tiles_in_row:
            self.x -= tiles_in_row
            x -= tiles_in_row
        if self.x < 0:
            self.x += tiles_in_row
            x += tiles_in_row
        if self.y >= tiles_in_row:
            self.y -= tiles_in_row
            y -= tiles_in_row
        if self.y < 0:
            self.y += tiles_in_row
            y += tiles_in_row

    def is_occupied(self):
        return self.occupied is None

    def get_game_piece(self):
        return self.occupied

    def occupy(self,obj):
        if isinstance(obj, game_piece.game_piece):
            self.occupied = obj
        else:
            self.occupied = None