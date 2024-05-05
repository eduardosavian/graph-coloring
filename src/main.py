from sudoku import Sudoku

def main():
    size = 4
    sudoku = Sudoku(size)
    sudoku.print() 
    sudoku.plot()



if __name__ == "__main__":
    main()
