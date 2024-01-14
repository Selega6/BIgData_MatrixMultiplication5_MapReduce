class Coordinate:
    def __init__(self, i, j, value):
        self.i = i
        self.j = j
        self.value = value

    def __repr__(self):
        return f"Coordinate(i={self.i}, j={self.j}, value={self.value})"