#!/usr/bin/python3
import sys

def is_valid(board, row, col, N):
    # Check row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col, N):
    # Base case: all queens are placed
    if col == N:
        solution = []
        for row in range(N):
            for c in range(N):
                if board[row][c] == 1:
                    solution.append([row, c])
        return [solution]

    solutions = []
    for row in range(N):
        if is_valid(board, row, col, N):
            board[row][col] = 1
            for solution in solve_n_queens(board, col + 1, N):
                solutions.append(solution)
            board[row][col] = 0

    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * N for _ in range(N)]
    solutions = solve_n_queens(board, 0, N)
    for solution in solutions:
        print(solution)
