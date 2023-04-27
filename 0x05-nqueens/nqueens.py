#!/usr/bin/python3
"""
N queens
"""
import sys


def nqueens(N):
    def is_valid(board, row, col):
        for r, c in board:
            if r == row or c == col or abs(r - row) == abs(c - col):
                return False
        return True

    def backtrack(board, row):
        if row == N:
            print_solution(board)
        else:
            for col in range(N):
                if is_valid(board, row, col):
                    board.append((row, col))
                    backtrack(board, row+1)
                    board.pop()

    def print_solution(board):
        print(','.join(str(c+1) for r, c in board))

    if not isinstance(N, int):
        print('N must be a number')
        sys.exit(1)
    if N < 4:
        print('N must be at least 4')
        sys.exit(1)

    backtrack([], 0)

if len(sys.argv) != 2:
    print('Usage: nqueens N')
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print('N must be a number')
    sys.exit(1)

nqueens(N)
