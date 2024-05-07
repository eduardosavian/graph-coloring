import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
from sudoku import Sudoku

class SudokuGUI:
    def __init__(self, master):
        self.master = master
        self.n = 0
        self.start_row = 0
        self.start_col = 0
        self.master.title("Sudoku Solver")

        self.size_label = tk.Label(master, text="Enter size of Sudoku board (e.g., 4 for 4x4):")
        self.size_label.pack()
        self.size_entry = tk.Entry(master)
        self.size_entry.pack()

        self.row_label = tk.Label(master, text="Enter starting row (0-indexed):")
        self.row_label.pack()
        self.row_entry = tk.Entry(master)
        self.row_entry.pack()

        self.col_label = tk.Label(master, text="Enter starting column (0-indexed):")
        self.col_label.pack()
        self.col_entry = tk.Entry(master)
        self.col_entry.pack()

        self.plot_button = tk.Button(master, text="Plot Sample Sudoku", command=self.plot_sample_sudoku)
        self.plot_button.pack()

    def plot_sample_sudoku(self):
        try:
            self.n = int(self.size_entry.get())
            self.start_row = int(self.row_entry.get())
            self.start_col = int(self.col_entry.get())

            if self.n < 1 or self.n > 4:
                raise ValueError("Size must be between 1 and 4.")
            if self.start_row < 0 or self.start_row >= self.n or self.start_col < 0 or self.start_col >= self.n:
                raise ValueError("Starting row or column is out of range for the specified size.")

            sudoku = Sudoku(self.n)
            self.plot_sudoku_board(sudoku)

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def plot_sudoku_board(self, sudoku):
        sudoku.generate(self.start_row, self.start_col)
        grid = np.array(sudoku.grid)
        plt.figure(figsize=(self.n, self.n))
        plt.title("Sample Sudoku ({}x{})".format(self.n, self.n))
        plt.imshow(grid, cmap='viridis', interpolation='nearest')

        for i in range(self.n):
            for j in range(self.n):
                plt.text(j, i, grid[i, j], ha='center', va='center', color='black')

        plt.xticks([])
        plt.yticks([])
        plt.show()