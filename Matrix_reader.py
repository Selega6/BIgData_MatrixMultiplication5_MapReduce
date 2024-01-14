from typing import List
from Matrix import Matrix
from Coordinate import Coordinate


class MatrixReader:
    def read(self, path: str) -> List[Coordinate]:
        raise NotImplementedError("Subclasses must implement this method")

    def create_matrix(self, coordinates: List[Coordinate]) -> Matrix:
        raise NotImplementedError("Subclasses must implement this method")
