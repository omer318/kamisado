import pygame

tiles_in_row = 8

class game_tile():
    def __init__(self, color, unit_size ,x=0, y=0 ):
        self.x = x
        self.y = y
        self.color = color
        self.occupied = False
        self.unit_size = unit_size
        self.tile = pygame.Rect(self.x * self.unit_size, self.y * self.unit_size, self.unit_size, self.unit_size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x * self.unit_size, self.y * self.unit_size, self.unit_size, self.unit_size))
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