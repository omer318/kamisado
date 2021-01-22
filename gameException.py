from enums import GAME_EXCEPTION


class GameException(Exception):
    def __init__(self, game_exception):
        self.type = GAME_EXCEPTION[game_exception.upper()]
        self.message = f"{self.type}_EXCEPTION: {self.type.value}"
        super().__init__(self.message)
