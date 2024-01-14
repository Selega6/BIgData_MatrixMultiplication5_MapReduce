from Matrix import Matrix
from Matrix_builder import MatrixBuilder
from Matrix_implementations.Dense_matrix import DenseMatrix


class DenseMatrixBuilder(MatrixBuilder):
    def __init__(self, size):
        self.size = size
        self.values = [[0] * size for _ in range(size)]

    def set(self, i, j, value):
        self.values[i][j] = value

    def get(self) -> Matrix:
        return DenseMatrix(self.values)
