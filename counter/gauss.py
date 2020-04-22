def list_sum_and_prod(li, an_li):
    s = 0
    for i in range(len(li)):
        s += li[i] * an_li[i]
    return s


class SLAU:
    def __init__(self, matrix):
        self.original_matrix = matrix
        self.matrix = matrix
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])
        self.swap_count = 0
        self.det = None
        self.solution = None

        if self.cols != self.rows + 1:
            raise ValueError('num of cols need to be same as num of rows + 1')
        for row in self.matrix:
            if len(row) != self.cols:
                raise ValueError('all rows len need to be similar')

    def get_main_row(self, col, row_from):
        row_num = row_from
        for row in range(row_from, self.rows):
            if abs(self.matrix[row][col]) > abs(self.matrix[row_num][col]):
                row_num = row
        return row_num

    def get_main_col(self, row, col_from):
        col_num = col_from
        for col in range(col_from, self.cols - 1):
            if abs(self.matrix[row][col]) > abs(self.matrix[row][col_num]):
                col_num = col
        return col_num

    def swap_rows(self, row_1, row_2):
        if row_1 != row_2:
            self.matrix[row_1], self.matrix[row_2] = self.matrix[row_2], self.matrix[row_1]
            self.swap_count += 1

    def swap_cols(self, col_1, col_2):
        if col_1 == self.cols - 1 or col_2 == self.cols - 1:
            raise ValueError("You can't swap with last column")
        if col_1 != col_2:
            for row in self.matrix:
                row[col_1], row[col_2] = row[col_2], row[col_1]
                self.swap_count += 1

    def sum_rows(self, row_to, row_from, k=1):
        for i in range(self.cols):
            self.matrix[row_to][i] += self.matrix[row_from][i] * k

    def prod_row(self, row, num):
        if num != 1:
            self.matrix[row] = [item * num for item in self.matrix[row]]

    def make_triangle(self):
        det = 1
        for k in range(self.rows):
            self.swap_rows(self.get_main_row(k, k), k)
            det *= self.matrix[k][k]
            if det == 0:
                self.det = det
                break
            for n in range(k + 1, self.rows):
                self.sum_rows(n, k, (-1) * self.matrix[n][k] / self.matrix[k][k])
        self.det = det if self.swap_count % 2 == 0 else - det

    def solve(self):
        if self.det:
            solution = [None for _ in range(self.rows)]
            for row in range(self.rows - 1, -1, -1):
                s = 0
                for col in range(row + 1, self.rows):
                    s += self.matrix[row][col] * solution[col]
                solution[row] = (self.matrix[row][-1] - s) / self.matrix[row][row]
            self.solution = solution

    def get_difference(self):
        if self.solution:
            return [row[-1] - list_sum_and_prod(row[:-1], self.solution) for row in self.original_matrix]
        else:
            return None

    def __str__(self):
        return '\n'.join(
            [' '.join((' ' if item >= 0 else '') + '%5.3f' % item for item in row) for row in self.matrix]) + '\n'
