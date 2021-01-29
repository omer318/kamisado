from enums import COLOR


def hex_to_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb


class Win:
    SERIALIZED_LENGTH = 15

    def __init__(self, winner, piece, is_sumo_win):
        self.winner = winner
        self.piece = piece
        self.is_sumo_win = is_sumo_win

    def get_winner(self):
        return self.winner.name.capitalize()

    def get_piece(self):
        return self.piece.name.capitalize()

    def serialize(self):
        return f"{self.winner.name}:{rgb_to_hex(self.piece.value)}:{int(self.is_sumo_win)}".encode("ASCII")

    @staticmethod
    def deserialize(string):
        string = string.decode("ASCII")
        winner, hex_color, is_sumo = string.split(':')
        winner = COLOR[winner]
        color = hex_to_rgb(hex_color)
        is_sumo = bool(int(is_sumo))
        return Win(winner, color, is_sumo)
