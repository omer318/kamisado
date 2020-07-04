import pygame
import time
from enum import Enum

width = 8
length = 8
tile_size = 64


class COLOR(Enum):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BROWN = (102, 51, 0)
    GREEN = (50, 153, 0)
    RED = (153, 0, 0)
    YELLOW = (204, 204, 0)
    PINK = (255, 104, 204)
    PURPLE = (104, 0, 104)
    BLUE = (0, 0, 153)
    ORANGE = (255, 255 / 2, 0)


class game_tile():
    def __init__(self, color, x=0, y=0):
        self.x = x
        self.y = y
        self.color = color
        self.occupied = False
        self.tile = pygame.Rect(self.x * tile_size, self.y * tile_size, tile_size, tile_size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.tile)
        pygame.display.flip()

    def move(self, x, y):
        self.x += x
        self.y += y
        if self.x >= 8:
            self.x -= 8
            x -= 8
        if self.x < 0:
            self.x += 8
            x += 8
        if self.y >= 8:
            self.y -= 8
            y -= 8
        if self.y < 0:
            self.y += 8
            y += 8
        self.tile.x += x * tile_size
        self.tile.y += y * tile_size


def main():
    screen = setup_game()
    loop_game(screen)


def setup_game():
    screen = pygame.display.set_mode((width * tile_size, length * tile_size))
    pygame.display.set_caption("Game")
    screen.fill(COLOR.BLACK.value)
    build_board(screen)
    pygame.display.flip()
    return screen


def build_board(screen):
    tile = game_tile(COLOR.ORANGE.value)
    for i in range(8):
        tile.draw(screen)
        tile.move(1, 1)
        pygame.display.flip()

    tile = game_tile(COLOR.BLUE.value, 1)
    for i in range(8):
        tile.draw(screen)
        tile.move(3, 1)
        pygame.display.flip()

    tile = game_tile(COLOR.PURPLE.value, 2)
    for i in range(8):
        tile.draw(screen)
        tile.move(5, 1)
        pygame.display.flip()

    tile = game_tile(COLOR.PINK.value, 3)
    for i in range(8):
        tile.draw(screen)
        tile.move(1, -1)
        pygame.display.flip()

    tile = game_tile(COLOR.YELLOW.value, 4)
    for i in range(8):
        tile.draw(screen)
        tile.move(1, 1)
        pygame.display.flip()

    tile = game_tile(COLOR.RED.value, 5)
    for i in range(8):
        tile.draw(screen)
        tile.move(3, 1)
        pygame.display.flip()

    tile = game_tile(COLOR.GREEN.value, 6)
    for i in range(8):
        tile.draw(screen)
        tile.move(5, 1)
        pygame.display.flip()

    tile = game_tile(COLOR.BROWN.value, 7)
    for i in range(8):
        tile.draw(screen)
        tile.move(-1, 1)
        pygame.display.flip()


def loop_game(screen):
    colors = iter(COLOR)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()


def quit_game():
    pygame.quit()


if __name__ == '__main__':
    main()
