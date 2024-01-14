import numpy as np

class Matrix_generator:
    def __init__(self):
        self.matrix = None
        self.size = None

    def generate(self, size):
        self.size = size
        self.matrix = np.random.randint(0, 10, size=(size, size))
        return self.matrix

    def write(self, file_path):
        with open(file_path, 'w') as file:
            file.write(f"{self.size} {self.size} {np.count_nonzero(self.matrix)}\n")

            for i in range(self.size):
                for j in range(self.size):
                    file.write(f"{i} {j} {self.matrix[i, j]}\n")

        print(f"Matrix saved in: {file_path}")