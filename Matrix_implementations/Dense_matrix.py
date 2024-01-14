from Matrix import Matrix


class DenseMatrix(Matrix):
    def __init__(self, values):
        self.values = values

    def size(self):
        return len(self.values)

    def get(self, i, j):
        return self.values[i][j]

    def print_matrix(self):
        for i in range(len(self.values)):
            row = [self.get(i, j) for j in range(len(self.values))]
            print(row)

    def transpose(self):
        transposed_values = [[0] * len(self.values) for _ in range(len(self.values))]
        for i in range(len(self.values)):
            for j in range(i, len(self.values)):
                transposed_values[i][j] = self.values[j][i]
                transposed_values[j][i] = self.values[i][j]
        return DenseMatrix(transposed_values)
