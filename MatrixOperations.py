from Matrix_implementations.Dense_matrix import DenseMatrix
from Matrix_implementations.CoordinateMatrix import CoordinateMatrix
from Coordinate import Coordinate


class MatrixOperations:
    def multiply_dense_matrix(a: DenseMatrix, b: DenseMatrix) -> DenseMatrix:
        size = a.size()
        values = [[0] * size for _ in range(size)]

        for i in range(size):
            for j in range(size):
                s = 0
                for k in range(size):
                    s += a.get(i, k) * b.get(k, j)
                values[i][j] = s

        return DenseMatrix(values)

    def multiply_coordinate_matrices(a: CoordinateMatrix, b: CoordinateMatrix) -> CoordinateMatrix:
        size = a.size
        result_coordinates = []

        for i in range(size):
            for j in range(size):
                s = sum(a.get(i, k) * b.get(k, j) for k in range(size))
                if s != 0:
                    result_coordinates.append(Coordinate(i, j, s))

        return CoordinateMatrix(size, result_coordinates)

