import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
import subprocess
import json

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
    # Path to your executable file
        exe_path = r'libs\sudoku_graph_coloration.exe'

        try:
            self.n = int(self.size_entry.get())
            self.start_row = int(self.row_entry.get())
            self.start_col = int(self.col_entry.get())

            if self.n < 1 or self.n > 9:
                raise ValueError("Size must be between 1 and 9.")

            # Run the executable with arguments
            result = subprocess.run([exe_path, str(self.n), str(self.start_row), str(self.start_col)],
                                    capture_output=True, text=True)

            # Parse the output strings to extract Sudoku grids
            sudoku_grids = []
            for line in result.stdout.strip().split('\n'):
                if line.startswith('"graph":'):
                    sudoku_grid = json.loads("{" + line.strip()[:-1] + "}")["graph"]
                    sudoku_grids.append(sudoku_grid)

            # Plot Sudoku grids using matplotlib
            plt.figure(figsize=(12, 6))
            for i, sudoku_grid in enumerate(sudoku_grids):
                plt.subplot(1, len(sudoku_grids), i + 1)
                plt.imshow(sudoku_grid, cmap='viridis', interpolation='nearest')
                plt.title(f'Sudoku Grid {i + 1} (Size: {self.n}x{self.n})')
                plt.axis('off')  # Turn off axis
                plt.colorbar()  # Show color bar for reference

            plt.tight_layout()
            plt.show()

        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except FileNotFoundError:
            messagebox.showerror("Error", f"The executable '{exe_path}' was not found.")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Failed to run '{exe_path}': {e}")
        except json.JSONDecodeError as je:
            messagebox.showerror("Error", f"Failed to parse JSON output: {je}")


def main():
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
