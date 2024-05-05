import random
import numpy as np

class Sudoku:
    def __init__(self, size):
        if size < 1:
            raise ValueError("Size must be greater than 0, but got {}".format(size))
        if size > 4:
            raise ValueError("Size must be less than or equal to 4, but got {}".format(size))
        self.size = size
        self.sudoku = [[0 for _ in range(size)] for _ in range(size)]

    def print(self):
        for row in self.sudoku:
            print(' '.join(map(str, row)))

    def is_valid(self, row, col, num):
        if num in self.sudoku[row]:
            return False
        for r in range(self.size):
            if self.sudoku[r][col] == num:
                return False

        block_size = int(self.size**0.5)
        start_row, start_col = (row // block_size) * block_size, (col // block_size) * block_size
        for r in range(start_row, start_row + block_size):
            for c in range(start_col, start_col + block_size):
                if self.sudoku[r][c] == num:
                    return False
        return True

    def solve(self):
        empty_cell = self.find_empty()
        if not empty_cell:
            return True
        row, col = empty_cell
        for num in range(1, self.size + 1):
            if self.is_valid(row, col, num):
                self.sudoku[row][col] = num
                if self.solve():
                    return True
                self.sudoku[row][col] = 0
        return False

    def find_empty(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.sudoku[i][j] == 0:
                    return (i, j)
        return None

    def generate(self, start_row, start_col):
        self.solve()
        self.shuffle_board()

    def shuffle_board(self, start_ro=0, start_col=0):
        nums = list(range(1, self.size + 1))
        random.shuffle(nums)
        for i in range(self.size):
            for j in range(self.size):
                self.sudoku[i][j] = nums[self.sudoku[i][j] - 1]

    def plot(self):
        grid = np.array(self.sudoku)
        plt.figure(figsize=(self.size, self.size))
        plt.title("Sudoku")
        plt.imshow(grid, cmap='viridis', interpolation='nearest')

        for i in range(self.size):
            for j in range(self.size):
                plt.text(j, i, grid[i, j], ha='center', va='center', color='black')

        plt.xticks([])
        plt.yticks([])
        plt.show()
