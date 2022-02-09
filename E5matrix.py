class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [[int(elem) for elem in row.split(' ') ] for row in matrix_string.split('\n')]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [row[index - 1] for row in self.matrix]



m = Matrix("9 8 7\n5 3 2\n6 6 7")
print (m.matrix)
print (m.row(2))
print (m.column(1))