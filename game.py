import pygame
from math import floor
from color import COLOR
from board import Board


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
                print(f"x: {x}, y: {y}")
                if self.selected_piece is None:
                    if self.board.board[x][y].piece is not None:
                        self.board.board[x][y].select()
                        self.selected_piece = (x, y)
                else:
                    self.apply_move(x, y)
                self.update_game()

    def apply_move(self, x, y):
        try:
            self.board.board[self.selected_piece[0]][self.selected_piece[1]].piece.move(x, y)
            self.board.board[x][y].piece = self.board.board[self.selected_piece[0]][
                self.selected_piece[1]].piece
            self.board.board[self.selected_piece[0]][self.selected_piece[1]].piece = None
            self.board.board[x][y].deselect()
            self.selected_piece = None
        except Exception as e:
            self.board.board[self.selected_piece[0]][self.selected_piece[1]].deselect()
            self.selected_piece = None
            print(e)
