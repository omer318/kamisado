from enum import Enum


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

    def __eq__(self, other):
        return self.value == other


class GAME_EXCEPTION(Enum):
    ILLEGAL_MOVE = "Pieces can move only straight forward or diagonally forward"
    WRONG_TURN = "Players aren't allowed to play not in their turn"
    WRONG_COLOR = "Only the piece which matches the color of the tile that the opponent played to can move"
    OCCUPIED_TILE = "Pieces can't move on top of other pieces"
    MOVE_TO_SAME_SPOT = "Pieces can't move to their current position"
