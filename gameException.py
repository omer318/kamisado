from enums import GAME_EXCEPTION


class GameException(Exception):
    def __init__(self, game_exception):
        self.message = f"{game_exception}_EXCEPTION: {game_exception.value}"
        super().__init__(self.message)
