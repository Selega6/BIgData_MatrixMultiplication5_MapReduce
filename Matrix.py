class Matrix:
    def size(self):
        raise NotImplementedError("Subclasses must implement this method")

    def get(self, i, j):
        raise NotImplementedError("Subclasses must implement this method")
