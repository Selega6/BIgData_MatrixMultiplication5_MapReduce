from MTX_Matrix_Reader import MTXMatrixReader
from Matrix_implementations.CoordinateMatrix import CoordinateMatrix
import subprocess


class Controller:
    def __init__(self, mtx_matrix_reader, path):
        self.reader = mtx_matrix_reader
        self.path = path

    def write_matrix(self, matrix, file):
        with open(file, "w") as file:
            file.write(f"{matrix.size} {matrix.size} {len(matrix.coordinates)}\n")

            for coordinate in matrix.coordinates:
                file.write(f"{coordinate.i} {coordinate.j} {coordinate.value}\n")

    def run(self, nameA, nameB):
        coordinates = self.reader.read(self.path)
        res = self.reader.create_matrix(coordinates)
        res2 = res.transpose()
        self.write_matrix(res2, nameB)
        self.write_matrix(res, nameA)
        command = ["python", "MatrixMultiplicationMapReduce.py", nameA, nameB]
        subprocess.run(command)




