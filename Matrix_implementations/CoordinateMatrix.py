from typing import List
from Matrix_implementations.Sparse_matrix import SparseMatrix
from Coordinate import Coordinate


class CoordinateMatrix(SparseMatrix):
    def __init__(self, size: int, coordinates: List[Coordinate]):
        self.size = size
        self.coordinates = coordinates

    def size(self) -> int:
        return self.size

    def get(self, i: int, j: int) -> int:
        return next((c.value for c in self.coordinates if c.i == i and c.j == j), 0)

    def transpose(self) -> 'CoordinateMatrix':
        transposed_coordinates = [Coordinate(c.j, c.i, c.value) for c in self.coordinates]
        return CoordinateMatrix(self.size, transposed_coordinates)