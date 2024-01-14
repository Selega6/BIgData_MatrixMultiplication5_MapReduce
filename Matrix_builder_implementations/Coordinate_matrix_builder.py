from Matrix import Matrix
from Matrix_implementations.CoordinateMatrix import CoordinateMatrix
from Matrix_builder_implementations.Sparse_matrix_builder import SparseMatrixBuilder


class CoordinateMatrixBuilder(SparseMatrixBuilder):
    def __init__(self, size):
        super().__init__(size)

    def get(self) -> Matrix:
        return CoordinateMatrix(self.size, self.coordinates)
