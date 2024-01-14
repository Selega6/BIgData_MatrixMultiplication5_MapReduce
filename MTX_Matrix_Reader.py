from typing import List
from Matrix import Matrix
from Matrix_reader import MatrixReader
from Coordinate import Coordinate
from Matrix_builder_implementations.Coordinate_matrix_builder import CoordinateMatrixBuilder
from Matrix_builder_implementations.Sparse_matrix_builder import SparseMatrixBuilder

class MTXMatrixReader(MatrixReader):
    def read(self, path: str) -> List[Coordinate]:
        with open(path, 'r') as file:
            lines = file.readlines()

        coordinates = []
        for line in lines:
            if self.eliminate_comments(line):
                continue

            tokenizer = line.split()
            coordinate = self.set_coordinates(tokenizer)
            coordinates.append(coordinate)

        return coordinates

    def create_matrix(self, coordinates: List[Coordinate]) -> Matrix:
        size = coordinates[0].i
        builder = CoordinateMatrixBuilder(size)

        for coordinate in coordinates[1:]:
            builder.set(coordinate.i, coordinate.j, coordinate.value)

        return builder.get()

    @staticmethod
    def set_coordinates(tokenizer):
        row = int(tokenizer[0])
        col = int(tokenizer[1])
        value = int(tokenizer[2])
        return Coordinate(row, col, value)

    @staticmethod
    def eliminate_comments(line):
        return line.startswith("%") or line.startswith("%%")
