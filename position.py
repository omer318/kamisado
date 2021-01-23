class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if other is Position:
            return self.x == other.x and self.y == other.y
        elif other is tuple:
            return self.x == other[0] and self.y == other[1]

    def __str__(self):
        return f"({self.x}, {self.y})"

