class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        row_arr = self.matrix_string.splitlines()[index - 1].split()
        return [int(num) for num in row_arr]

    def column(self, index):
        seperate_row = self.matrix_string.splitlines()
        row_list = [row.split() for row in seperate_row]
        return [int(col[index-1]) for col in row_list]

    def __repr__(self):
        return self.matrix_string
