from Matrix import Matrix


class MatrixBuilder:
    def set(self, i: int, j: int, value: int) -> None:
        raise NotImplementedError("Subclasses must implement this method")

    def get(self) -> Matrix:
        raise NotImplementedError("Subclasses must implement this method")
