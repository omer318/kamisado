from math import floor

import pygame
import time
from color import COLOR
from board import Board
from game_tile import GameTile


def map_click(pos):
    return tuple(map(lambda x: floor(x / 64), pos))


def detect_click():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            return pos
    return None


class Game:
    def __init__(self, board_length_pixels, board_length_units):
        self.board = None
        self.board_length_pixels = board_length_pixels
        self.board_length_units = board_length_units
        self.unit_size = self.board_length_pixels / self.board_length_units
        self.screen = self.setup_game()
        self.selected_piece = None

    def setup_game(self):
        screen = pygame.display.set_mode((self.board_length_pixels, self.board_length_pixels))
        pygame.display.set_caption("Game")
        screen.fill(COLOR.BLACK.value)
        self.board = Board(screen, self.unit_size, "board.txt")
        pygame.display.flip()
        return screen

    def update_game(self):
        self.screen.fill(COLOR.BLACK.value)
        self.board.draw_board()
        pygame.display.flip()

    def loop_game(self):
        while True:
            pos = detect_click()
            if pos is not None:
                x, y = map_click(pos)
                if self.selected_piece is None and self.board.board[x][y].occupied is not None:
                    self.board.board[x][y].select()
                    self.selected_piece = (x, y)
                else:
                    self.board.board[self.selected_piece[0]][self.selected_piece[1]].occupied.move(x, y)
                    self.board.board[x][y].occupied = self.board.board[self.selected_piece[0]][self.selected_piece[1]].occupied
                    self.board.board[self.selected_piece[0]][self.selected_piece[1]].occupied = None
                    self.selected_piece = None
                self.update_game()


def main():
    game = Game(512, 8)
    game.loop_game()


if __name__ == '__main__':
    main()
