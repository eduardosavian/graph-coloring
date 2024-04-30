import math
import networkx as nx
import matplotlib.pyplot as plt

def is_valid(board, row, col, num):
    # Verifica se é seguro colocar 'num' na posição (row, col) do tabuleiro
    N = len(board)
    # Verifica se 'num' já está na mesma linha ou coluna
    for i in range(N):
        if board[row][i] == num or board[i][col] == num:
            return False
    # Verifica se 'num' já está na mesma sub-grade NxN
    sqrt_N = int(math.sqrt(N))
    start_row, start_col = (row // sqrt_N) * sqrt_N, (col // sqrt_N) * sqrt_N
    for i in range(start_row, start_row + sqrt_N):
        for j in range(start_col, start_col + sqrt_N):
            if board[i][j] == num:
                return False
    return True

def solve_sudoku(board, start_row, start_col):
    # Implementa o algoritmo de backtracking para resolver o Sudoku
    N = len(board)
    if start_row == N:  # Todas as posições foram preenchidas
        return True
    next_row = start_row if start_col < N - 1 else start_row + 1
    next_col = (start_col + 1) % N
    if board[start_row][start_col] != 0:
        return solve_sudoku(board, next_row, next_col)
    for num in range(1, N + 1):
        if is_valid(board, start_row, start_col, num):
            board[start_row][start_col] = num
            if solve_sudoku(board, next_row, next_col):
                return True
            board[start_row][start_col] = 0  # Backtracking
    return False

def print_board(board):
    # Imprime o tabuleiro formatado
    for row in board:
        print(' '.join(map(str, row)))

def draw_sudoku_graph(board, start_row, start_col):
    # Cria um grafo correspondente ao tabuleiro de Sudoku
    N = len(board)
    G = nx.Graph()
    # Adiciona os vértices ao grafo
    for i in range(N):
        for j in range(N):
            G.add_node((i, j), color='white' if (i, j) != (start_row, start_col) else 'red')
    # Adiciona as arestas ao grafo
    for i in range(N):
        for j in range(N):
            for k in range(j + 1, N):
                if board[i][j] != 0 and board[i][k] != 0:
                    G.add_edge((i, j), (i, k))
                if board[j][i] != 0 and board[k][i] != 0:
                    G.add_edge((j, i), (k, i))
    # Define as posições dos vértices para desenhar o grafo
    pos = {(i, j): (j, -i) for i in range(N) for j in range(N)}
    # Obtém as cores dos vértices do grafo
    node_colors = [node[1]['color'] for node in G.nodes(data=True)]
    # Desenha o grafo
    nx.draw(G, pos=pos, with_labels=False, node_size=400, node_color=node_colors, edge_color='gray', linewidths=1, font_size=10)
    plt.show()

def main():
    while True:
        try:
            N = int(input("Digite a ordem do tabuleiro de Sudoku (N x N): "))
            if N < 1 or N > 16 or math.isqrt(N) ** 2 != N:
                raise ValueError("A ordem do tabuleiro deve ser um número inteiro com raiz quadrada exata até 16.")
            break
        except ValueError as e:
            print(e)
    
    board = [[0] * N for _ in range(N)]

    while True:
        try:
            start_row = int(input(f"Digite a linha de início (0 a {N-1}): "))
            start_col = int(input(f"Digite a coluna de início (0 a {N-1}): "))
            if 0 <= start_row < N and 0 <= start_col < N:
                break
            else:
                raise ValueError(f"Os valores de início devem estar dentro da faixa de 0 a {N-1}.")
        except ValueError as e:
            print(e)

    if solve_sudoku(board, start_row, start_col):
        print("\nTabuleiro de Sudoku resolvido:")
        print_board(board)
        draw_sudoku_graph(board, start_row, start_col)
    else:
        print("\nNão foi possível resolver o tabuleiro de Sudoku com as configurações fornecidas.")

if __name__ == "__main__":
    main()
