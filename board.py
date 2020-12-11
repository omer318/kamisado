import pygame
from color import COLOR
from game_tile import GameTile


class Board:
    def __init__(self, screen, unit_size, board_file_path):
        self.screen = screen
        self.unit_size = unit_size
        self.board = []
        self.init_board(board_file_path)

    def init_board(self, board_file_path):
        self.parse_board(board_file_path)
        self.build_board()

    def parse_board(self, board_file_path):
        with open(board_file_path, "r") as board_file:
            raw = board_file.read().split("\n")
        for i in range(len(raw)):
            self.board.append(raw[i].split(" "))

    def build_board(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(COLOR[(self.board[i][j]).upper()].value)
                self.board[i][j] = GameTile(self.screen, self.unit_size, COLOR[(self.board[i][j]).upper()].value, i, j)
                self.board[i][j].draw()
