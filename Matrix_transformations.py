from Matrix import Matrix
from Matrix_implementations.CoordinateMatrix import CoordinateMatrix
from Matrix_implementations.Dense_matrix import DenseMatrix
from Matrix_builder_implementations.Coordinate_matrix_builder import CoordinateMatrixBuilder
from Matrix_builder_implementations.Dense_matrix_builder import DenseMatrixBuilder


class MatrixTransformations:
    def transform(self, matrix: DenseMatrix) -> Matrix:
        builder = CoordinateMatrixBuilder(matrix.size)
        for i in range(matrix.size()):
            for j in range(matrix.size()):
                if matrix.get(i, j) == 0:
                    continue
                builder.set(i, j, matrix.get(i, j))
        return builder.get()

    def transform_to_dense(self, matrix: CoordinateMatrix) -> Matrix:
        builder = DenseMatrixBuilder(matrix.size)
        for coordinate in matrix.coordinates:
            builder.set(coordinate.i, coordinate.j, coordinate.value)
        return builder.get()
