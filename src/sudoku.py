import random
import numpy as np
import matplotlib.pyplot as plt

class Sudoku:
    def __init__(self, size):
        if size < 1:
            raise ValueError("Size must be greater than 0, but got {}".format(size))
        if size > 16:
            raise ValueError("Size must be less than or equal to 16, but got {}".format(size))
        self.size = size
        self.grid = [[0 for _ in range(size)] for _ in range(size)]

    def is_valid(self, row, col, num):
        if num in self.grid[row]:
            return False
        for r in range(self.size):
            if self.grid[r][col] == num:
                return False

        block_size = int(self.size**0.5)
        start_row, start_col = (row // block_size) * block_size, (col // block_size) * block_size
        for r in range(start_row, start_row + block_size):
            for c in range(start_col, start_col + block_size):
                if self.grid[r][c] == num:
                    return False
        return True

    def solve(self):
        empty_cell = self.find_empty()

        if not empty_cell:
            return True
        row, col = empty_cell
        for num in range(1, self.size + 1):
            if self.is_valid(row, col, num):
                self.grid[row][col] = num
                if self.solve():
                    return True
                self.grid[row][col] = 0
        return False

    def find_empty(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == 0:
                    return (i, j)
        return None

    def set_value(self, row, col, value):
        if 1 <= value <= self.size:
            self.grid[row][col] = value
        else:
            raise ValueError("Value must be between 1 and {}, but got {}".format(self.size, value))

    def generate_and_propagate(self, start_row, start_col):
        # Set the starting point
        if not (0 <= start_row < self.size and 0 <= start_col < self.size):
            raise ValueError("Invalid starting point.")

        # Solve the Sudoku puzzle starting from the specified point
        self.solve_from(start_row, start_col)

        # Apply adjacency propagation
        self.propagate_adjacency()

    def solve_from(self, row, col):
        # Solve the Sudoku puzzle starting from a specific point (recursive)
        if row == self.size:
            return True

        next_row = row if col < self.size - 1 else row + 1
        next_col = (col + 1) % self.size

        if self.grid[row][col] != 0:
            return self.solve_from(next_row, next_col)

        for num in range(1, self.size + 1):
            if self.is_valid(row, col, num):
                self.grid[row][col] = num
                if self.solve_from(next_row, next_col):
                    return True
                self.grid[row][col] = 0

        return False

    def propagate_adjacency(self):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

        # Iterate over each cell in the grid
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] != 0:
                    num = self.grid[i][j]
                    # Propagate the number to adjacent cells
                    for d in directions:
                        ni, nj = i + d[0], j + d[1]
                        if 0 <= ni < self.size and 0 <= nj < self.size and self.grid[ni][nj] == 0:
                            self.grid[ni][nj] = num  # Set adjacent cell to the same number

    def plot(self):
        grid = np.array(self.grid)
        plt.figure(figsize=(self.size, self.size))
        plt.title("Sudoku")
        plt.imshow(grid, cmap='viridis', interpolation='nearest')

        for i in range(self.size):
            for j in range(self.size):
                plt.text(j, i, grid[i, j], ha='center', va='center', color='black')

        plt.xticks([])
        plt.yticks([])
        plt.show()

size = 3
sudoku = Sudoku(size)

start_row, start_col = 2, 2
initial_value = 1
sudoku.set_value(start_row, start_col, initial_value)

sudoku.generate_and_propagate(start_row, start_col)
sudoku.plot()
