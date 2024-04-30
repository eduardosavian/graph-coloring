import tkinter as tk
from tkinter import messagebox

class SudokuGUI:
    def __init__(self, root, n=3):
        self.root = root
        self.n = n  # Size of Sudoku board (n x n)

        self.board = [[tk.StringVar() for _ in range(n)] for _ in range(n)]

        self.create_widgets()

    def create_widgets(self):
        # Create n x n grid of entry widgets for Sudoku input
        for i in range(self.n):
            for j in range(self.n):
                entry = tk.Entry(self.root, width=4, font=('Helvetica', 14), textvariable=self.board[i][j], justify='center')
                entry.grid(row=i, column=j, padx=3, pady=3)

        # Button to display the entered Sudoku puzzle
        show_button = tk.Button(self.root, text='Show Sudoku', command=self.show_sudoku)
        show_button.grid(row=self.n, columnspan=self.n, pady=10)

    def show_sudoku(self):
        # Retrieve the Sudoku puzzle from the entry widgets
        puzzle = [[self.board[i][j].get() or ' ' for j in range(self.n)] for i in range(self.n)]

        # Display the entered Sudoku puzzle
        messagebox.showinfo('Entered Sudoku', self.format_sudoku(puzzle))

    def format_sudoku(self, puzzle):
        # Format the Sudoku puzzle for display
        return '\n'.join([' '.join(row) for row in puzzle])
