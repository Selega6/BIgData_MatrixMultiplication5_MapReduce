from Coordinate import Coordinate
from Matrix import Matrix
from Matrix_builder import MatrixBuilder


class SparseMatrixBuilder(MatrixBuilder):

    def __init__(self, size):
        self.size = size
        self.coordinates = []

    def set(self, i, j, value):
        self.set_coordinate(Coordinate(i, j, value))

    def set_coordinate(self, coordinate):
        self.coordinates.append(coordinate)

    def get(self) -> Matrix:
        pass