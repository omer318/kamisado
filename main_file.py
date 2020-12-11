import pygame
import time
from color import COLOR
from board import Board
from game_tile import GameTile

board_length_pixels = 512
board_length_units = 8
unit_size = board_length_pixels / board_length_units

board = None


def main():
    print(COLOR["BLUE"].value)
    screen = setup_game()
    loop_game(screen)


def setup_game():
    screen = pygame.display.set_mode((board_length_pixels, board_length_pixels))
    pygame.display.set_caption("Game")
    screen.fill(COLOR.BLACK.value)
    board = Board(screen, unit_size, "board.txt")
    pygame.display.flip()
    return screen


def loop_game(screen):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


if __name__ == '__main__':
    main()
