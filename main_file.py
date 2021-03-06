import pygame
import time
from enum import Enum
import game_tile

board_length_pixels = 512
board_length_units = 8
unit_size = board_length_pixels / board_length_units

board = []


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


def main():
    screen = setup_game()
    loop_game(screen)


def setup_game():
    screen = pygame.display.set_mode((board_length_pixels, board_length_pixels))
    pygame.display.set_caption("Game")
    screen.fill(COLOR.BLACK.value)
    build_board(screen)
    pygame.display.flip()
    return screen


def build_board(screen):
    tile = game_tile.game_tile(COLOR.ORANGE.value, unit_size, 0)
    for i in range(8):
        tile.draw(screen)
        tile.move(1, 1)
        pygame.display.flip()

    tile = game_tile.game_tile(COLOR.BLUE.value, unit_size, 1)
    for i in range(8):
        tile.draw(screen)
        tile.move(3, 1)
        pygame.display.flip()

    tile = game_tile.game_tile(COLOR.PURPLE.value, unit_size, 2)
    for i in range(8):
        tile.draw(screen)
        tile.move(5, 1)
        pygame.display.flip()

    tile = game_tile.game_tile(COLOR.PINK.value, unit_size, 3)
    for i in range(8):
        tile.draw(screen)
        tile.move(1, -1)
        pygame.display.flip()

    tile = game_tile.game_tile(COLOR.YELLOW.value, unit_size, 4)
    for i in range(8):
        tile.draw(screen)
        tile.move(1, 1)
        pygame.display.flip()

    tile = game_tile.game_tile(COLOR.RED.value, unit_size, 5)
    for i in range(8):
        tile.draw(screen)
        tile.move(3, 1)
        pygame.display.flip()

    tile = game_tile.game_tile(COLOR.GREEN.value, unit_size, 6)
    for i in range(8):
        tile.draw(screen)
        tile.move(5, 1)
        pygame.display.flip()

    tile = game_tile.game_tile(COLOR.BROWN.value, unit_size, 7)
    for i in range(8):
        tile.draw(screen)
        tile.move(-1, 1)
        pygame.display.flip()


def loop_game(screen):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


if __name__ == '__main__':
    main()
