from menu import SudokuGUI
import tkinter as tk

def main():
    root = tk.Tk()
    sudoku_gui = SudokuGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
