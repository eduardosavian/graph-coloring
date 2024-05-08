import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
import subprocess

class SudokuGUI:
    def __init__(self, master):
        self.master = master
        self.n = 0
        self.start_row = 0
        self.start_col = 0
        self.master.title("Sudoku Solver")

        self.size_label = tk.Label(self.master, text=f"Enter size of Sudoku board (1-16):")
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

            if self.n < 1 or self.n > 16:
                raise ValueError("Size must be between 1 and 16.")

            # Run the executable with arguments
            result = subprocess.run([exe_path, str(self.n), str(self.start_row), str(self.start_col)],
                                    capture_output=True, text=True)

            # Separate the output into grids
            separate = result.stdout.replace('\n', '').strip().split('-')
            sepate_array1 = separate[0].split(';')
            sepate_array2 = separate[1].split(';')

            array1 = np.array([list(map(int, row.split(','))) for row in sepate_array1])
            array2 = np.array([list(map(int, row.split(','))) for row in sepate_array2])

            # Create figure and subplots
            fig, axs = plt.subplots(1, 2, figsize=(12, 6))

            # Plot Array 1 (Grid 1)
            axs[0].imshow(array1, cmap='viridis', interpolation='nearest')
            for i in range(self.n):
                for j in range(self.n):
                    axs[0].text(j, i, array1[i, j], ha='center', va='center', color='black')

            axs[0].set_title(f'Sudoku Grid 1 (Size: {self.n}x{self.n})')
            axs[0].axis('off')  # Turn off axis

            # Plot Array 2 (Grid 2)
            axs[1].imshow(array2, cmap='viridis', interpolation='nearest')
            for i in range(self.n):
                for j in range(self.n):
                    axs[1].text(j, i, array2[i, j], ha='center', va='center', color='black')

            axs[1].set_title(f'Sudoku Grid 2 (Size: {self.n}x{self.n})')
            axs[1].axis('off')  # Turn off axis

            plt.tight_layout()
            plt.show()

        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except FileNotFoundError:
            messagebox.showerror("Error", f"The executable '{exe_path}' was not found.")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Failed to run '{exe_path}': {e}")

def main():
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
