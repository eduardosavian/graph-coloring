from sudoku import Sudoku

def main():
    size = 5
    sudoku_game = Sudoku(size)
    print("Sudoku gerado:")
    sudoku_game.print()


if __name__ == "__main__":
    main()
