import pygame

tiles_in_row = 8


class GamePiece:
    def __init__(self, screen, unit_size, color, side_color, x=0, y=0):
        self.is_selected = False
        self.x = x
        self.y = y
        self.radius = int((unit_size * 0.8) / 2)
        self.color = color
        self.side_color = side_color
        self.occupied = False
        self.unit_size = int(unit_size)
        self.screen = screen

    def draw(self):
        pygame.draw.circle(self.screen, self.side_color,
                           (int((self.x + 0.5) * self.unit_size), int((self.y + 0.5) * self.unit_size)),
                           self.radius + (3 + int(self.is_selected) * 2))
        pygame.draw.circle(self.screen, self.color,
                           (int((self.x + 0.5) * self.unit_size), int((self.y + 0.5) * self.unit_size)),
                           self.radius)
        pygame.display.flip()

    def move(self, x, y):
        self.x = x
        self.y = y

    def select(self):
        self.is_selected = not self.is_selected
        self.draw()
