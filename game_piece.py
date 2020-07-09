import pygame

tiles_in_row = 8


class game_piece():
    def __init__(self, color, unit_size, x=0, y=0):
        self.x = x
        self.y = y
        self.radius = int((unit_size *0.8 ) / 2)
        self.color = color
        self.occupied = False
        self.unit_size = int(unit_size)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int((self.x + 0.5) * self.unit_size), int((self.y + 0.5) * self.unit_size)),
                           self.radius)
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
