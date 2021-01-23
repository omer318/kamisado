import pygame
from math import floor
from enums import COLOR, GAME_EXCEPTION
from board import Board
from position import Position
from gameException import GameException


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
        self.current_player = COLOR.WHITE
        self.current_color = None
        self.is_first_move = True
        self.winner = None

    def setup_game(self):
        print("-" * 36)
        screen = pygame.display.set_mode((self.board_length_pixels, self.board_length_pixels))
        pygame.display.set_caption("Game")
        screen.fill(COLOR.BLACK.value)
        self.board = Board(screen, self.unit_size, "board.txt")
        pygame.display.flip()
        return screen

    def update_game(self):
        self.board.draw_board()
        pygame.display.flip()

    def loop_game(self):
        while True:
            pos = detect_click()
            if pos is not None:
                x, y = map_click(pos)
                if self.selected_piece is None:
                    if self.board.board[x][y].piece is not None:
                        self.board.board[x][y].select()
                        self.selected_piece = Position(x, y)
                        self.show_available_moves()
                else:
                    if self.apply_move(x, y):
                        if self.is_position_blocked():
                            print(f"{self.current_player.name.capitalize()} is blocked.")

                            next_color = self.board.get_tile_by_piece_color_and_side_color(self.board.board[x][y].color,
                                                                                           self.current_player)
                            self.current_color = next_color.color
                            self.current_player = COLOR.BLACK if self.current_player == COLOR.WHITE else COLOR.WHITE
                            print(f"{self.current_player.name.capitalize()} to move next" +
                                  f" with the {COLOR(self.current_color).name.lower()} piece.\n" + "-" * 36)
                self.update_game()
                if self.winner is not None:
                    break
        print(f"{self.winner} Won!")

    def apply_move(self, x, y):
        success = True
        try:
            self.is_legal_move(x, y)
            self.board.board[self.selected_piece.x][self.selected_piece.y].piece.move(x, y)
            self.board.board[x][y].piece = self.board.board[self.selected_piece.x][
                self.selected_piece.y].piece
            self.board.board[self.selected_piece.x][self.selected_piece.y].piece = None
            self.board.board[x][y].deselect()
            if self.check_for_win():
                self.winner = self.current_player.name
            self.pass_turn(x, y)
        except GameException as e:
            print(e)
            self.board.board[self.selected_piece.x][self.selected_piece.y].deselect()
            success = False
        finally:
            self.selected_piece = None
            self.hide_available_moves()
            return success

    def pass_turn(self, x, y):
        if self.is_first_move:
            self.is_first_move = False

        print(f"{self.current_player.name.capitalize()} moved the " +
              f"{COLOR(self.board.board[x][y].piece.color).name.lower()} piece to "
              f"({x}, {y}).")
        self.current_player = self.get_opposite_color()
        self.current_color = self.board.board[x][y].color
        print(f"{self.current_player.name.capitalize()} to move next" +
              f" with the {COLOR(self.current_color).name.lower()} piece.\n" + "-" * 36)

    def check_for_win(self):
        for i in range(len(self.board.board)):
            if self.board.board[i][7].piece is not None and self.board.board[i][7].piece.side_color == COLOR.BLACK:
                return True
            if self.board.board[i][0].piece is not None and self.board.board[i][0].piece.side_color == COLOR.WHITE:
                return True
        return False

    def is_position_blocked(self):
        self.selected_piece = self.board.get_piece_by_color_and_side_color(self.current_color, self.current_player)
        flag = not bool(self.get_available_moves(self.selected_piece.x, self.selected_piece.y))
        self.selected_piece = None
        return flag

    def is_legal_move(self, x, y):
        if not (0 <= x <= 7 and 0 <= y <= 7):
            raise GameException(GAME_EXCEPTION.OFF_THE_BOARD)
        if self.selected_piece.x == x and self.selected_piece.y == y:
            raise GameException(GAME_EXCEPTION.MOVE_TO_SAME_SPOT)
        if self.board.board[x][y].piece is not None:
            raise GameException(GAME_EXCEPTION.ILLEGAL_MOVE)
        if self.board.board[self.selected_piece.x][self.selected_piece.y].piece.side_color != self.current_player:
            raise GameException(GAME_EXCEPTION.WRONG_TURN)
        if self.board.board[self.selected_piece.x][self.selected_piece.y].piece.color != self.current_color:
            if not self.is_first_move:
                raise GameException(GAME_EXCEPTION.WRONG_COLOR)

    def show_available_moves(self):
        moves = self.get_available_moves(self.selected_piece.x, self.selected_piece.y)
        for move in moves:
            self.board.board[move.x][move.y].mark()

    def hide_available_moves(self):
        moves = [Position(tile.x, tile.y) for row in self.board.board for tile in row]
        for move in moves:
            self.board.board[move.x][move.y].unmark()

    def get_available_moves(self, x, y):
        legal_moves = []
        piece = self.board.board[x][y].piece
        if piece.side_color == COLOR.WHITE:
            # Move Up
            for i in range(1, piece.y + 1):
                try:
                    self.is_legal_move(piece.x, piece.y - i)
                    legal_moves.append(Position(piece.x, piece.y - i))
                except GameException:
                    break
            # Move right diagonally
            for i in range(1, min(piece.y, 7 - piece.x) + 1):
                try:
                    self.is_legal_move(piece.x + i, piece.y - i)
                    legal_moves.append(Position(piece.x + i, piece.y - i))
                except GameException:
                    break
            # Move left diagonally
            for i in range(1, min(piece.y, piece.x) + 1):
                try:
                    self.is_legal_move(piece.x - i, piece.y - i)
                    legal_moves.append(Position(piece.x - i, piece.y - i))
                except GameException:
                    break

        if piece.side_color == COLOR.BLACK:
            # Move down
            for i in range(1, 7 - piece.y + 1):
                try:
                    self.is_legal_move(piece.x, piece.y + i)
                    legal_moves.append(Position(piece.x, piece.y + i))
                except GameException:
                    break
            # Move right diagonally
            for i in range(1, min(7 - piece.y, 7 - piece.x) + 1):
                try:
                    self.is_legal_move(piece.x + i, piece.y + i)
                    legal_moves.append(Position(piece.x + i, piece.y + i))
                except GameException:
                    break

            for i in range(1, min(7 - piece.y, piece.x) + 1):
                try:
                    self.is_legal_move(piece.x - i, piece.y + i)
                    legal_moves.append(Position(piece.x - i, piece.y + i))
                except GameException:
                    break
        return legal_moves

    def get_opposite_color(self):
        return COLOR.BLACK if self.current_player == COLOR.WHITE else COLOR.WHITE
