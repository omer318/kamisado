import pygame
from color import COLOR

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
        if self.is_forward(x, y) :
            print(f"Moving the {COLOR(self.color).name.lower()} piece to ({x}, {y}) forward")
            self.x = x
            self.y = y
        elif self.is_diagonal(x, y):
            print(f"Moving the {COLOR(self.color).name.lower()} piece to ({x}, {y}) diagonaly")
            self.x = x
            self.y = y
        else:
            print(f"NOT Moving the {COLOR(self.color).name.lower()} piece to ({x}, {y})")
            raise Exception("Illegal Move")

    def select(self):
        self.is_selected = not self.is_selected
        self.draw()

    def is_forward(self, x, y):
        if self.side_color == COLOR["WHITE"]:
            return self.x == x and self.y > y
        if self.side_color == COLOR["BLACK"]:
            return self.x == x and self.y < y

    def is_diagonal(self, x, y):
        if self.side_color == COLOR["WHITE"]:
            return self.y - y == abs(self.x - x) and self.y > y
        if self.side_color == COLOR["BLACK"]:
            return y - self.y == abs(self.x - x) and self.y < y
