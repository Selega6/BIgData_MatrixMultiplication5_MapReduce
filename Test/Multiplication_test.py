import time

from MTX_Matrix_Reader import MTXMatrixReader
from Test.Controller import Controller
from MatrixOperations import MatrixOperations
from Random_matrix_generator import Matrix_generator
from Matrix_transformations import MatrixTransformations

class Test:
    def __init__(self):
        self.reader = MTXMatrixReader()
        self.path = "../Matrices/Test_sparseA.txt"
        self.controller = Controller(self.reader, self.path)

    def test_equal(self):
        matrixA = self.reader.create_matrix(self.reader.read(self.path))
        matrixB = matrixA.transpose()
        matrixC = MatrixOperations.multiply_coordinate_matrices(matrixA, matrixB)
        matrixD = self.reader.create_matrix(self.reader.read("../MultiplicationResult.txt"))
        for i in range(len(matrixC.coordinates)):
            for j in range(len(matrixD.coordinates)):
                if matrixC.coordinates[i].i == matrixD.coordinates[j].i and matrixC.coordinates[i].j == matrixD.coordinates[j].j:
                    if matrixC.coordinates[i].value != matrixD.coordinates[j].value:
                        print("Test failed")
                        return
        print("Test passed")

    def test_speed(self, matrix1, matrix2, output):
        start_time = time.time()
        self.controller.run(matrix1, matrix2)
        end_time = time.time()
        elapsed_time = end_time - start_time
        elapsed_time_seconds = int(elapsed_time)
        print("Elapsed time for Map_Reduce:", elapsed_time_seconds, "seconds")
        matrixA = self.reader.create_matrix(self.reader.read(self.path))
        matrixB = matrixA.transpose()
        matrixA = MatrixTransformations().transform_to_dense(matrixA)
        matrixB = MatrixTransformations().transform_to_dense(matrixB)
        start_time = time.time()
        matrixC = MatrixOperations.multiply_dense_matrix(matrixA, matrixB)
        end_time = time.time()
        elapsed_time = end_time - start_time
        elapsed_time_seconds = int(elapsed_time)
        print("Elapsed time for sequential:", elapsed_time_seconds, "seconds")


if __name__ == "__main__":
    test = Test()
    #test.test_equal()
    #test.test_speed("../Matrices/Test_equalA.txt", "../Matrices/Test_equalB.txt", "../Matrices/Equal_Multiplication_Result.txt")
    generator = Matrix_generator()
    A = generator.generate(2048)
    generator.write("../Matrices/Test_sparseA.txt")
    B = A.transpose()
    generator.write("../Matrices/Test_sparseB.txt")
    test.test_speed("../Matrices/Test_sparseA.txt", "../Matrices/Test_sparseB.txt", "../Matrices/Speed_Multiplication_Result.txt")
